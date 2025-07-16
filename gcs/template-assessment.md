# Granularity Assessment Questionnaire  
*(Based on the **Granularity Classification Spectrum – GCS**)*  

---

### Purpose  
Help architects and engineers locate a **capability** along the GCS granularity spectrum, which ranges from **Monolith** to **Nanoservice / FaaS**.  

### How to use  
For each question, tick the alternative that best describes the capability **today** and record its score. When finished, sum the points and use the table at the end to find the corresponding GCS level.

---

## Questions

| # | Dimension | Question | Alternatives **(points)** |
|---|-----------|----------|---------------------------|
| **A&nbsp;·&nbsp;Business Scope** ||||
| 1 | Functional breadth | How many **primary business responsibilities** does the capability contain? | a) More than 3 (0)<br>b) 2–3 (1) <br>c) Exactly 1, cohesive (2) <br>d) A single, well-defined function (3) |
| **B&nbsp;·&nbsp;Deployment Scope** ||||
| 2 | Deployment form | How is the capability **packaged and deployed**? | a) Part of one large artefact with several capabilities (0) <br>b) Single modular application, but no independent deployment (1) <br>c) Stand-alone service (container/VM) (2) <br>d) Serverless function / FaaS (3) |
| 3 | Release frequency | The capability is released… | a) Together with a large batch of features (0) b) With 2–3 related capabilities (1) c) Independently (2) d) On demand / event-triggered (3) |
| **C&nbsp;·&nbsp;Independence & Coupling** ||||
| 4 | Database ownership | Does the capability have its **own database/schema**? | a) Shared with several functions (0) b) Shared DB, but separate schemas (1) c) Exclusive database (2) d) Stores only transient or no state (3) |
| 5 | External integrations | **Number of integration points** required for its main logic | a) ≥ 6 (0) b) 3–5 (1) c) 1–2 (2) d) 0 (3) |
| **D&nbsp;·&nbsp;Internal Complexity** ||||
| 6 | Code size ¹ | Approximate lines of code | a) > 25 k (0) b) 10–25 k (1) c) 3–10 k (2) d) < 3 k (3) |
| 7 | Cohesion | Classes / modules address… | a) Heterogeneous business domains (0) b) A broad but related domain (1) c) A focused domain with few variations (2) d) One specialised function (3) |
| **E&nbsp;·&nbsp;Organisation & Teams** ||||
| 8 | Team ownership | How many **teams maintain** this capability? | a) More than 3 (0) b) 2–3 (1) c) A dedicated team (2) d) Less than one FTE; maintained “as code” (3) |
| 9 | Decision autonomy | To evolve the capability, the team depends on… | a) Central governance + multiple approvals (0) b) 2–3 groups (1) c) Only its Product Owner (2) d) Automation & feature flags (3) |
| **F&nbsp;·&nbsp;Performance & Cost** ||||
| 10 | Scalability | The component scales… | a) Only together with the whole system (0) b) With 2–3 related services (1) c) Independently (2) d) Elastically per invocation (3) |
| 11 | Operational overhead | Current fragmentation incurs **coordination cost** that is… | a) Low because everything is local (0) b) Medium (1) c) Noticeable but controlled (2) d) High; remote calls dominate **(subtract 1 point)** |

> ¹ Code size may be replaced by **LOC**, **CYC**, or similar metrics recommended in the study.

---

## Scoring & GCS Mapping
![alt text](fig3.png)
1. **Add up** the points (maximum = 31).  
2. **Locate** the total in the table below.

| Total | GCS Level | Quick interpretation |
|-------|-----------|----------------------|
| 0–5   | **Monolithic** | Capability is part of one big block – consider initial extraction. |
| 6–9   | **Modular Monolith** | Clear internal boundaries but no independent deployment. |
| 10–13 | **Service-Based** | Still large services; early sub-domain hints, low isolation. |
| 14–17 | **Microservice – Extended** | One capability per service; few external dependencies. |
| 18–22 | **Microservice – Intermediate** | Service covers a cohesive subset; integrates with several peers. |
| 23–26 | **Microservice – Focused** | Isolated function, high cohesion and independence. |
| 27–31 | **Nanoservice / FaaS** | Maximum fragmentation, event-driven execution – watch for saturation. |

---

## Additional Usage Guidelines

* **Triangulate metrics.** Combine this questionnaire with size (NMS/TMS), effort (EST/ACT/EFT), operation (NCH/FCH), code (LOC/CYC/COV) and cost (CST) indicators suggested in the article to strengthen the diagnosis.  
* **Repeat periodically.** GCS supports **continuous granularity reviews** as the architecture evolves.  
* **Watch for saturation.** Scores in the 23–31 range, coupled with sharp increases in Remote Invocation Intensity (RVI) or Elasticity (E), may signal **granularity saturation**, calling for service consolidation.

---
