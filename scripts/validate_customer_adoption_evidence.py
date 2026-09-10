from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

PRODUCTS = {"iaap-guard", "iaap-forge", "iaap-console", "iaap-storefront", "iaap-assurance"}
DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
SEMVER = re.compile(r"(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})")
TOP_KEYS = {
    "schemaVersion", "product", "surface", "priorSelection", "adoptedSelection", "candidate",
    "customerAuthorization", "verification", "rollback", "evidenceAuthority"
}


class EvidenceError(ValueError):
    pass


def exact(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise EvidenceError(f"{label} must contain exactly the supported fields")
    return value


def version(value: Any, label: str) -> str:
    if not isinstance(value, str) or SEMVER.fullmatch(value) is None:
        raise EvidenceError(f"{label} must be bounded canonical SemVer")
    return value


def digest(value: Any, label: str) -> str:
    if not isinstance(value, str) or DIGEST.fullmatch(value) is None:
        raise EvidenceError(f"{label} must be sha256:<64 lowercase hex>")
    return value


def selection(value: Any, label: str) -> dict[str, str]:
    item = exact(value, {"version", "digest"}, label)
    return {"version": version(item["version"], f"{label}.version"), "digest": digest(item["digest"], f"{label}.digest")}


def validate(value: Any) -> dict[str, Any]:
    evidence = exact(value, TOP_KEYS, "customer adoption evidence")
    if evidence["schemaVersion"] != "iaap-customer-adoption-evidence/v1":
        raise EvidenceError("unsupported evidence schema")
    if evidence["product"] not in PRODUCTS:
        raise EvidenceError("unsupported product")
    if not isinstance(evidence["surface"], str) or not evidence["surface"] or len(evidence["surface"]) > 128:
        raise EvidenceError("surface must be non-empty and bounded")

    prior = selection(evidence["priorSelection"], "priorSelection")
    adopted = selection(evidence["adoptedSelection"], "adoptedSelection")

    candidate = exact(evidence["candidate"], {"version", "digest", "documentationRef", "documentationRevision", "compatibility", "authorityChange"}, "candidate")
    version(candidate["version"], "candidate.version")
    digest(candidate["digest"], "candidate.digest")
    digest(candidate["documentationRevision"], "candidate.documentationRevision")
    if not isinstance(candidate["documentationRef"], str) or not candidate["documentationRef"] or len(candidate["documentationRef"]) > 512:
        raise EvidenceError("candidate.documentationRef must be non-empty and bounded")
    if candidate["compatibility"] not in {"COMPATIBLE", "REVIEW_REQUIRED"}:
        raise EvidenceError("adopted candidate cannot be BLOCKED")
    if not isinstance(candidate["authorityChange"], bool):
        raise EvidenceError("candidate.authorityChange must be boolean")
    if adopted["version"] != candidate["version"] or adopted["digest"] != candidate["digest"]:
        raise EvidenceError("adopted selection must equal the documented candidate")

    authorization = exact(evidence["customerAuthorization"], {"recorded", "method", "reference"}, "customerAuthorization")
    if authorization["recorded"] is not True or authorization["method"] != "CUSTOMER_CONTROLLED_CHANGE":
        raise EvidenceError("customer authorization must be explicitly recorded")
    if not isinstance(authorization["reference"], str) or not authorization["reference"] or len(authorization["reference"]) > 512:
        raise EvidenceError("customer authorization reference must be non-empty and bounded")

    verification = exact(evidence["verification"], {"status", "verifiedVersion", "verifiedDigest", "checks"}, "verification")
    if verification["status"] != "PASS":
        raise EvidenceError("only verified PASS adoption evidence is accepted")
    if version(verification["verifiedVersion"], "verification.verifiedVersion") != adopted["version"]:
        raise EvidenceError("verification version must equal adopted selection")
    if digest(verification["verifiedDigest"], "verification.verifiedDigest") != adopted["digest"]:
        raise EvidenceError("verification digest must equal adopted selection")
    checks = verification["checks"]
    if not isinstance(checks, list) or not 1 <= len(checks) <= 32 or len(set(checks)) != len(checks):
        raise EvidenceError("verification.checks must contain 1-32 unique checks")
    if any(not isinstance(item, str) or not item or len(item) > 128 for item in checks):
        raise EvidenceError("verification checks must be non-empty bounded strings")

    rollback = exact(evidence["rollback"], {"retained", "version", "digest"}, "rollback")
    if rollback["retained"] is not True:
        raise EvidenceError("rollback target must be retained")
    rollback_selection = {"version": version(rollback["version"], "rollback.version"), "digest": digest(rollback["digest"], "rollback.digest")}
    if rollback_selection != prior:
        raise EvidenceError("rollback target must equal the prior accepted selection")

    if evidence["evidenceAuthority"] is not False:
        raise EvidenceError("adoption evidence cannot grant authority")
    return evidence


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("usage: validate_customer_adoption_evidence.py <evidence.json>", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(args[0]).read_text(encoding="utf-8"))
        validate(payload)
        print("customer adoption evidence: PASS")
        return 0
    except (OSError, json.JSONDecodeError, EvidenceError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
