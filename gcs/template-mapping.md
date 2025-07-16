# Capability Granularity Mapping Questionnaire  
_(compatible with the Granularity Classification Spectrum – GCS)_

---

## 1 · Capability Identification
| Field               | Value to fill in        |
|---------------------|-------------------------|
| **Capability Name** | <!-- TODO --> |
| **Business Objective (1 sentence)** | <!-- TODO --> |
| **Stakeholders / Responsible Teams** | <!-- TODO --> |

---

## 2 · Inventory of Implementation Units  
> [!TIP]  
> Fill **one row per unit** (Business Functionality — **FN** — or **FaaS** Function).

| # | Unit Type (FN/FaaS) | Name | Description | Team | Usage Frequency (High/Med/Low) | Change Frequency (deploys / year) | Dependencies | FaaS only → Runtime / Trigger / Timeout-Memory |
|---|---------------------|------|-------------------|------|--------------------------------|-----------------------------------|--------------|-----------------------------------------------|
| 1 | <!-- TODO -->       | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |
| 2 |                     |               |               |           |                                |                                   |              |                                               |
| … |                     |               |               |           |                                |                                   |              |                                               |

---

## 3 · Mapping to Deployables  
![alt text](fig3.png)

> [!TIP]  
> Copy each unit from Section 2 and indicate **where** it runs.

| Unit (Name) | Deployable (name/ID) | GCS Level (G0–G6) | Pipeline (Shared / Semi / Indep.) | Data Access | Size (LOC/MB) | Latency p95 (ms) |
|-------------|----------------------|-------------------|------------------------------------|-------------|---------------|------------------|
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |
|               |                      |                   |                                    |             |               |                  |
| …             |                      |                   |                                    |             |               |                  |

---

## 4 · Consolidation & Analysis

### 4.1 Distribution of Units by GCS Level
- **G0 (Monolith)**: __
- **G1 (Modular Monolith)**: __
- **G2 (Service-Based)**: __
- **G3 (Microservice-Extended)**: __
- **G4 (Microservice-Intermediate)**: __
- **G5 (Microservice-Focused)**: __
- **G6 (FaaS / Nanoservice)**: __

### 4.2 Heterogeneity Hotspots
<!-- List business rules / units that appear at different GCS levels -->
- …

### 4.3 Identified Risks
- [ ] Chained latency  
- [ ] Data sharing across levels  
- [ ] Multiple teams on the same deployable  
- Other: ___________________________________________________________

### 4.4 Suggested Actions
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

---

> **How to use this template**  
> 1. Copy the file into your study’s GitHub repository.  
> 2. Replace all “<!-- TODO -->” markers and empty cells with real values.  
> 3. Commit with a clear message, e.g., “Granularity Report – \<Capability\>”.  
> 4. Repeat the assessment periodically and save new versions in dated folders.

<!-- End of template -->