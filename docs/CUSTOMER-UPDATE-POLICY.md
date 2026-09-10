# Documentation-First Customer Update Policy

**Owner:** Infrastructure Product Works™  
**Applies to:** customer-impacting updates across the Infrastructure Product Works portfolio  
**Portfolio alignment:** `O5`, `KR5.1`-`KR5.3`, `EP-07`, with the distribution-contract intent of `DAS-01` and distribution-evidence intent of `DAS-08`  
**Posture:** `CONTINUE_VALIDATION`

## Policy

Infrastructure Product Works uses a documentation-first update model.

A customer-impacting software, policy, schema, integration, contract, configuration, packaging, or evaluation-behavior change is not ready for customer distribution until the customer-facing documentation for that change is complete, versioned, reviewable, and published as part of the release record.

Documentation is part of the product contract. It is not an after-the-fact release artifact.

## Required sequence

The governed customer-update sequence is:

`Documentation -> Candidate Release -> Compatibility Validation -> Customer Review -> Customer-Authorized Adoption -> Verification`

Publication of documentation or a candidate does not authorize installation or activation. A customer-controlled installation remains on its selected version until the customer takes the documented adoption action.

## Required release documentation

Before a customer-impacting update is offered for adoption, its release documentation must identify:

1. what is changing and why;
2. the affected product, component, engine, policy bundle, schema, contract, configuration, or package versions;
3. whether evaluation, governance, security, permissions, authority boundaries, compatibility, or externally observable behavior changes;
4. compatibility with supported prior versions and any prerequisites;
5. required and optional customer actions;
6. installation or adoption instructions;
7. upgrade instructions;
8. rollback instructions and the retained rollback target;
9. uninstall or removal considerations where applicable;
10. known limitations and unsupported conditions;
11. artifact versions, source revision, and cryptographic digests where the distribution surface supports them;
12. the documentation revision associated with the release; and
13. the release or effective date.

If an item does not apply, the documentation should say so rather than silently omit a material lifecycle or authority question.

## Customer control

Infrastructure Product Works must not treat publication of a new release as customer authorization to adopt it.

Where the product supports customer-pinned deployment or configuration, the selected version and integrity reference should remain in customer-controlled configuration or source control. Upgrades and rollbacks should therefore be explicit, reviewable customer actions.

A hosted product may receive provider-operated maintenance that does not alter the documented customer contract. Any change that alters customer-visible behavior, deterministic evaluation semantics, supported contracts, permissions, data handling, or authority boundaries is a customer-impacting update and is subject to this policy before the changed behavior is presented as a supported release.

## Guard-specific semantic updates

For IaaP Guard™, changes to the deterministic evaluation engine and changes to policy or rule bundles should be independently identifiable when practical. Release documentation must make clear whether an update changes only runtime implementation or changes evaluation/governance semantics.

A Guard update that can change a previously supported evaluation outcome must document that behavioral difference before customer adoption. The preferred adoption pattern is version-pinned and customer-controlled, with compatibility validation before the selected version changes.

The hosted GitHub App must not gain repository content-write, merge, deployment, provisioning, remediation, cloud-credential, or equivalent operational authority merely to automate customer upgrades.

## Preview and candidate documentation

Documentation may be published before candidate software so customers can review an upcoming change early. Preview documentation must be clearly identified as preview material and must not be represented as a supported stable release.

Stable distribution must not precede the release documentation required by this policy.

## Compatibility and rollback

Every supported update path must state the compatibility boundary and a rollback procedure or explicitly document why rollback is not applicable.

Rollback instructions must identify what is restored, what customer-owned state is retained, and any evidence or configuration that must remain available to reproduce the prior state.

## Release evidence

Where supported by the distribution surface, the release record should bind:

- product and component versions;
- source revision;
- artifact digest;
- policy or rule-bundle version and digest when independently versioned;
- documentation revision;
- compatibility result or evidence reference; and
- the customer-controlled adoption record or equivalent change record when such evidence is produced by the customer environment.

This binding is intended to make it possible to answer not only which software a customer selected, but also which documentation and behavioral contract described that selection.

## Historical documentation

Documentation for prior supported releases must remain available for audit, compatibility review, rollback, and evidence reconstruction. Historical release documentation should not be silently rewritten to describe later behavior.

Corrections to historical documentation should be additive and traceable.

## Portfolio scope

This policy applies to customer-impacting update surfaces for IaaP Guard, IaaP Forge, IaaP Console, Backstage-based storefront surfaces, IaaP Assurance, embedded Composite AI capabilities, and future Infrastructure Product Works products or distribution surfaces.

Each product may use a different packaging and installation model. The documentation-first lifecycle and customer-control boundary remain common.

## Authority boundary

This policy does not add credentials, repository permissions, cloud access, deployment capability, approval authority, merge authority, provisioning authority, remediation authority, spending authority, production authorization, or compliance authorization.

It does not convert roadmap intent into operational authority. Product-specific release gates and accepted evidence remain controlling.
