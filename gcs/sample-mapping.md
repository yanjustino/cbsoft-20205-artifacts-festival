# Capability Granularity Mapping Questionnaire  
_(compatible with the Granularity Classification Spectrum – **GCS**)_

---

## 1 · Capability Identification
| Field | Value |
|-------|-------|
| **Capability Name** | Investment Services |
| **Business Objective (1 sentence)** | Provide end-to-end services for investors: portfolio handling, trade processing, regulatory compliance and market-data-driven decision support. |
| **Stakeholders / Responsible Teams** | Trading Core – *Team Delta* · Investor Experience – *Team Sigma* · Risk & Compliance – *Team Lambda* |

---

## 2 · Inventory of Implementation Units  

| # | Unit Type (FN/FaaS) | Name | Description | Team | Usage Freq. | Change Freq. <br>(deploys / yr) | Dependencies | FaaS only → Runtime / Trigger / Timeout-Mem |
|---|---------------------|------|-------------|------|------------|---------------------------------|--------------|-------------------------------------------|
| 1 | **FN** | Portfolio Management | Manages investor portfolios and holdings inside the core platform. | Delta | **High** | 3 | Oracle, MQ | – |
| 2 | **FN** | Client Investment Services | Exposes SOAP/REST façade for client apps to query portfolios. | Sigma | High | 6 | Oracle, Redis | – |
| 3 | **FN** | Transaction Logging | Persists every trade / cash movement for auditing. | Lambda | High | 12 | PostgreSQL | – |
| 4 | **FN** | Asset Registration Management | Maintains static data of tradable assets. | Delta | Medium | 8 | PostgreSQL, Kafka | – |
| 5 | **FN** | Position Aggregation | Aggregates intraday positions across asset classes. | Delta | High | 20 | Redis, Kafka | – |
| 6 | **FN** | Position Maintenance | Updates positions after each trade settlement. | Delta | High | 24 | Kafka | – |
| 7 | **FN** | Investor Profile Management | Stores risk appetite and suitability data. | Sigma | Medium | 18 | MongoDB | – |
| 8 | **FaaS** | `positionEventConsumer()` | Consumes position events from Kafka topic. | Delta | High | 30 | Kafka | Java • Event • 256 MB / 60 s |
| 9 | **FaaS** | `positionEventPublisher()` | Publishes enriched position events to downstream topics. | Delta | High | 30 | Kafka | Java • Event • 256 MB / 60 s |
| 10 | **FaaS** | `assetValidation()` | Validates asset codes against reference data. | Lambda | High | 40 | DynamoDB | Node • HTTP • 128 MB / 30 s |
| 11 | **FaaS** | `investorDataEnrichment()` | Adds KYC/KYB data to trade message. | Lambda | Medium | 20 | DynamoDB | Python • Event • 256 MB / 45 s |
| 12 | **FaaS** | `positionWorkflowOrchestrator()` | Coordinates multi-step settlement workflow. | Delta | High | 26 | Step Functions | Python • Event • 512 MB / 120 s |
| 13 | **FaaS** | `portfolioRiskEvaluation()` | Calculates VaR on intraday snapshots. | Lambda | Medium | 12 | S3, EMR | Go • Schedule • 768 MB / 300 s |
| 14 | **FaaS** | `complianceRuleValidator()` | Applies rule engine to trade events. | Lambda | High | 36 | Rules API | Java • Event • 256 MB / 60 s |
| 15 | **FaaS** | `marketDataSync()` | Streams market prices into cache. | Sigma | High | 48 | WebSocket API | Node • Schedule • 256 MB / 90 s |

---

## 3 · Mapping to Deployables  
![alt text](fig3.png)

| Unit (Name) | Deployable (name / ID) | GCS Level | Pipeline | Data Access | Size | Latency p95 (ms) |
|-------------|------------------------|-----------|----------|-------------|------|------------------|
| Portfolio Management | `investment-core.jar` | **G1 – Modular Monolith** | Shared | Global Schema | 68 k LOC | 500 |
| Client Investment Services | `client-invest-svc:2.3.0` | **G2 – Service-Based** | Semi | Shared Schema | 30 k LOC | 320 |
| Transaction Logging | `translog-svc:1.6.1` | **G3 – Extended Microservice** | Indep. | DB-per-Service | 14 k LOC | 210 |
| Asset Registration Management | `asset-reg-svc:1.4.2` | **G3 – Extended Microservice** | Indep. | DB-per-Service | 12 k LOC | 200 |
| Position Aggregation | `position-agg-svc:2.1.0` | **G4 – Intermediate Microservice** | Indep. | Redis | 9 k LOC | 160 |
| Position Maintenance | `position-maint-svc:1.0.3` | **G5 – Focused Microservice** | Indep. | Kafka | 6 k LOC | 120 |
| Investor Profile Management | `investor-profile-svc:1.2.5` | **G5 – Focused Microservice** | Indep. | MongoDB | 7 k LOC | 130 |
| `positionEventConsumer()` | `arn:aws:lambda:positionEventConsumer` | **G6 – FaaS** | Indep. | Kafka | 0.7 k LOC | 85 |
| `positionEventPublisher()` | `arn:aws:lambda:positionEventPublisher` | **G6 – FaaS** | Indep. | Kafka | 0.7 k LOC | 90 |
| `assetValidation()` | `arn:aws:lambda:assetValidation` | **G6 – FaaS** | Indep. | DynamoDB | 0.6 k LOC | 100 |
| `investorDataEnrichment()` | `arn:aws:lambda:investorDataEnrichment` | **G6 – FaaS** | Indep. | DynamoDB | 0.8 k LOC | 110 |
| `positionWorkflowOrchestrator()` | `arn:aws:lambda:positionWorkflowOrchestrator` | **G6 – FaaS** | Indep. | Step Functions | 1.0 k LOC | 95 |
| `portfolioRiskEvaluation()` | `arn:aws:lambda:portfolioRiskEval` | **G6 – FaaS** | Indep. | S3 | 1.2 k LOC | 220 |
| `complianceRuleValidator()` | `arn:aws:lambda:complianceRuleValidator` | **G6 – FaaS** | Indep. | Rules API | 0.9 k LOC | 105 |
| `marketDataSync()` | `arn:aws:lambda:marketDataSync` | **G6 – FaaS** | Indep. | WS API | 0.8 k LOC | 115 |

---

## 4 · Consolidation & Analysis

### 4.1 Distribution of Units by GCS Level
| GCS Level | Units |
|-----------|-------|
| **G0 – Monolith** | 0 |
| **G1 – Modular Monolith** | **1** |
| **G2 – Service-Based** | **1** |
| **G3 – Extended Microservice** | **2** |
| **G4 – Intermediate Microservice** | **1** |
| **G5 – Focused Microservice** | **2** |
| **G6 – FaaS / Nanoservice** | **8** |

### 4.2 Heterogeneity Hotspots
- **Trade lifecycle** spans **G1**, **G3**, **G4**, **G5** and multiple **G6** functions → complex orchestration & potential latency.
- Position data inconsistently updated by **Position Maintenance** (G5) and **positionEventPublisher()** (G6) → risk of eventual-consistency bugs.

### 4.3 Identified Risks
- [x] Chained latency across five GCS levels  
- [x] Data duplication between monolith schema and microservice databases  
- [ ] Multiple teams on the same deployable  
- Other: observability gaps in legacy monolith

### 4.4 Suggested Actions
1. Gradually extract **Portfolio Management** into a microservice to reduce reliance on the monolith.  
2. Consolidate event consumer/publisher Lambdas into a single streaming application to minimise hop count.  
3. Introduce end-to-end tracing (OpenTelemetry) to quantify latency across G1-G6 interactions.

---

> **Note** –  Figures and metrics are illustrative, derived directly from the granularity breakdown in the referenced table. Replace with empirical data from your system for real assessments.