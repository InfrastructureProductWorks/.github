# Customer Adoption Evidence

Customer update evaluation and customer adoption are separate events.

The portfolio-wide `iaap-customer-adoption-evidence/v1` contract records the evidence created **after** a customer has explicitly authorized and verified an update. It does not authorize the update itself.

## Required chain

`Prior selection -> Documented candidate -> Customer-controlled authorization -> Adopted selection -> Verification -> Retained rollback target`

The evidence binds:

- product and distribution/update surface;
- prior accepted version and SHA-256 digest;
- adopted version and SHA-256 digest;
- candidate version/digest;
- release documentation reference and documentation digest/revision;
- compatibility classification and authority-change flag;
- a customer-owned change/authorization reference;
- post-adoption verification results; and
- the retained rollback version/digest.

The validator rejects:

- unknown products or fields;
- malformed or unbounded versions/digests;
- a `BLOCKED` candidate represented as adopted;
- adopted identity that differs from the candidate;
- missing customer authorization;
- verification that does not exactly match the adopted artifact;
- missing/changed rollback identity; and
- any attempt to set `evidenceAuthority` to true.

## Product use

Guard, Forge, Console, Storefront, and Assurance may emit this same evidence shape after their product-specific customer adoption process. Product-specific records can add separate evidence, but they should not weaken this common chain.

This contract supports auditability and rollback. It does not provide approval, merge, apply, deployment, provisioning, privilege, payment, legal, compliance, pilot, production, or customer-change authority.
