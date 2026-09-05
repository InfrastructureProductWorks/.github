<p align="center">
  <img src="https://raw.githubusercontent.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/main/docs/assets/showcase/iaap-hero.svg" alt="Infrastructure Product Works — Infrastructure-as-a-Product architecture" width="100%"/>
</p>

<h1 align="center">Infrastructure Product Works™</h1>

<p align="center"><strong>IaaS is what we buy; Infrastructure-as-a-Product is what we build.</strong></p>

<p align="center">
Governed infrastructure products for regulated enterprises.<br/>
Deterministic policy • bounded AI • multi-cloud control • human authority • verifiable evidence
</p>

<p align="center">
  <a href="https://github.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product"><strong>Explore the IaaP thesis</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/InfrastructureProductWorks/iaap-guard"><strong>View IaaP Guard</strong></a>
</p>

---

## The product boundary comes first

Infrastructure Product Works is building a governed **Infrastructure-as-a-Product (IaaP)** model for organizations that need cloud speed without surrendering architecture discipline, portability, traceability, or human control.

Developers should order an infrastructure outcome through a stable product contract. The machinery behind that contract can evolve across AWS, Azure, GCP, Kubernetes, Crossplane, GitHub, and approved enterprise tooling without turning every application team into an infrastructure integration team.

<p align="center">
  <img src="https://raw.githubusercontent.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/main/docs/assets/showcase/iaap-drive-thru-product-model.webp" alt="Developers order infrastructure outcomes rather than assembling the underlying ingredients" width="92%"/>
</p>

<p align="center"><em>Developers order the outcome — not the ingredients.</em></p>

---

## One governed product system

```mermaid
flowchart LR
    DEV[Developer / Product Team]
    EXP[Storefront • API • CLI • Conversation]
    GUARD[IaaP Guard™\nDeterministic architecture + evidence]
    HUMAN[Authorized Human Review]
    FORGE[IaaP Forge™\nBounded product proposal]
    CONTROL[Crossplane / Product Control Plane]
    CLOUD[AWS • Azure • GCP • Approved On-Prem]
    ASSURE[IaaP Assurance™\nAuthority • Custody • Continuous Assurance]

    DEV --> EXP
    EXP --> GUARD
    GUARD --> HUMAN
    HUMAN --> FORGE
    FORGE --> CONTROL
    CONTROL --> CLOUD
    GUARD --> ASSURE
    FORGE --> ASSURE
    CLOUD --> ASSURE

    classDef experience fill:#0D2438,stroke:#38BDF8,stroke-width:2px,color:#F8FAFC
    classDef guard fill:#0B2F2D,stroke:#14B8A6,stroke-width:2px,color:#F8FAFC
    classDef authority fill:#3B2010,stroke:#FB923C,stroke-width:2px,color:#F8FAFC
    classDef forge fill:#26163F,stroke:#A855F7,stroke-width:2px,color:#F8FAFC
    classDef control fill:#10294B,stroke:#3B82F6,stroke-width:2px,color:#F8FAFC
    classDef assurance fill:#35132D,stroke:#EC4899,stroke-width:2px,color:#F8FAFC
    class DEV,EXP experience
    class GUARD guard
    class HUMAN authority
    class FORGE forge
    class CONTROL,CLOUD control
    class ASSURE assurance
```

The architecture deliberately separates **experience, validation, approval, generation, reconciliation, and assurance**. AI can interpret, propose, explain, diagnose, and assemble evidence — but deterministic controls and authorized people remain the decision boundary.

---

## Portfolio

| Product / capability | Responsibility | Public posture |
|---|---|---|
| **AI-Powered Infrastructure-as-a-Product** | Thesis, reference architecture, governance model, roadmap context, and sanitized portfolio evidence | **Public** |
| **IaaP Guard™** | GitHub-native deterministic architecture and evidence guard | **Public** |
| **IaaP Forge™** | Converts accepted intent and evidence into bounded infrastructure-product proposals and lifecycle artifacts | Private implementation |
| **IaaP Console™** | Customer-hosted assessment, evidence, planning, selection, and lifecycle experience | Private implementation |
| **IaaP Assurance™** | Authority, custody, safeguard continuity, rollback evidence, and continuous assurance | Private implementation |
| **Storefront & integration proofs** | Product discovery, handoff integrity, selection evidence, interoperability, and negative testing | Internal / bounded proof |

<p align="center">
  <img src="https://raw.githubusercontent.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/main/docs/assets/showcase/portfolio-system.svg" alt="Infrastructure Product Works bounded product portfolio" width="96%"/>
</p>

---

## What distinguishes the model

| Principle | What it means in practice |
|---|---|
| **Product contract first** | Consumers depend on a stable infrastructure product interface — not a Terraform workspace, provider implementation, portal, module, or pipeline. |
| **Deterministic gates before AI authority** | AI can assist the lifecycle, but schemas, policy, tests, evidence, and authorized human approval decide what is valid. |
| **Multi-cloud by contract** | Provider-specific implementations remain replaceable behind stable product contracts rather than leaking into the consumer boundary. |
| **Evidence is part of the product** | Architecture decisions, validation results, approvals, digests, custody references, and lifecycle state are retained as evidence. |
| **Progressive modernization** | Legacy systems can remain authoritative while replacement capabilities move onto governed modern infrastructure products by bounded business capability. |
| **Fail closed** | Missing, altered, mismatched, unauthorized, or unsafe evidence does not silently become permission to proceed. |

---

## Evidence over assertion

<p align="center">
  <img src="https://raw.githubusercontent.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/main/docs/assets/showcase/evidence-chain.svg" alt="Evidence-first Infrastructure-as-a-Product lifecycle" width="96%"/>
</p>

A claim is only as strong as the reproducible evidence chain behind it. Infrastructure Product Works treats validation, approval, reconciliation, observed state, and custody evidence as first-class parts of the product lifecycle.

---

## Public starting points

<table>
<tr>
<td width="50%" valign="top">

### AI-Powered Infrastructure-as-a-Product

The public architecture and strategy front door: thesis, reference architecture, governance, product model, roadmap context, modernization position, and sanitized evidence.

**[Open the repository →](https://github.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product)**

</td>
<td width="50%" valign="top">

### IaaP Guard™

The supported GitHub-native architecture and evidence guard. Deterministic checks evaluate whether infrastructure is actually being designed and governed as a product.

**[Open IaaP Guard →](https://github.com/InfrastructureProductWorks/iaap-guard)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Enterprise Azure Governance

Enterprise governance patterns and reference work supporting policy, platform, and cloud-control thinking.

**[Open the repository →](https://github.com/InfrastructureProductWorks/enterprise-azure-governance)**

</td>
<td width="50%" valign="top">

### Portfolio architecture

Private and internal repositories hold bounded implementation, assurance, integration, and product-development work. Public repositories carry the architecture, supported public products, sanitized evidence, and claim boundaries.

**[Explore the organization →](https://github.com/InfrastructureProductWorks?tab=repositories)**

</td>
</tr>
</table>

---

## Progressive modernization

The intended destination is not a prettier legacy runtime. The goal is **measurable transfer of business capability and data authority** from legacy estates into governed, portable infrastructure products.

<p align="center">
  <img src="https://raw.githubusercontent.com/InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/main/docs/assets/showcase/progressive-legacy-modernization.svg" alt="Progressive legacy modernization through governed infrastructure products" width="96%"/>
</p>

Infrastructure Product Works therefore supports a staged model: **stabilize → coexist → transfer → retire**. Application teams remain responsible for business meaning, data migration, equivalence, cutover, and retirement decisions; the infrastructure-product system provides the governed destination and evidence chain.

---

## Current claim boundary

The portfolio contains supported public software alongside private and internal research, integration, and assurance work. Published proofs are intentionally bounded unless a repository explicitly states otherwise.

> A synthetic or bounded **PASS** means that the stated contract and evidence relationships were demonstrated under the published test conditions. It does **not** by itself claim production readiness, customer deployment, certification, an ATO, autonomous infrastructure authority, or unrestricted access to live enterprise systems.

---

<details>
<summary><strong>Design principles in one minute</strong></summary>

- Stable product contracts outlive provider-specific implementations.
- Backstage or another experience layer is replaceable.
- Crossplane is a reference product control plane, not the consumer-facing product boundary.
- GitHub governs change, review, traceability, and evidence.
- Deterministic policy and tests decide validity.
- Authorized people approve material changes.
- Cloud-native IAM and platform controls remain the ultimate enforcement boundary.
- AI remains bounded by those controls rather than becoming an independent authority.

</details>

---

<h3 align="center">Build infrastructure that behaves like a product.</h3>
<p align="center"><strong>Portable. Governed. Measurable. Provable.</strong></p>
