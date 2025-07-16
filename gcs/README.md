# Capability Granularity Mapping Artifact
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This artifact is part of the CBSoft 2025 Artifacts Festival and is designed to support the Capability Granularity Mapping Questionnaire. It aligns with the Granularity Classification Spectrum (GCS) and provides a structured approach to evaluate and document software capabilities and their implementation units.

## Purpose

The artifact aims to:
- Facilitate the identification and classification of software capabilities.
- Provide a systematic inventory of implementation units.
- Map implementation units to deployables and analyze their distribution across GCS levels.
- Highlight heterogeneity hotspots and identify risks.
- Suggest actionable steps for improvement.


## How to Use

To effectively utilize this artifact, follow these steps:

1. **Clone the Repository**: Clone the repository containing this artifact to your local machine.
   ```bash
   git clone https://github.com/yanjustino/cbsoft-20205-artifacts-festival.git
   ```

2. **Navigate to the Artifact Directory**: Move to the `gcs` directory where the artifact is located.
   ```bash
   cd gcs
   ```

3. **Review the Templates**:
   - Open the [template-assessment.md](./template-assessment.md) file to evaluate the granularity of software capabilities.
   - Open the [template-mapping.md](./template-mapping.md) file to map implementation units to deployables.


4. **Fill in the Templates**: Replace all `<!-- TODO -->` placeholders with the relevant information.
5. **Commit Changes**: Save your changes and commit them to the repository with a meaningful message.
6. **Repeat Periodically**: Perform periodic assessments and save new versions in dated folders to track progress over time.


## Application of Assessment

The `template-assessment.md` file provides a structured questionnaire to evaluate the granularity of software capabilities based on the Granularity Classification Spectrum (GCS). This template is designed to help architects and engineers:

1. **Locate Capabilities**: Identify where a capability lies on the GCS spectrum, ranging from Monolith to Nanoservice/FaaS.
2. **Score Dimensions**: Evaluate dimensions such as business scope, deployment scope, independence, internal complexity, organizational factors, and performance.
3. **Map Results**: Use the scoring table to map the capability to its corresponding GCS level.

### How to Use the Template

1. **Open the Template**: Navigate to the `gcs` directory and open the `template-assessment.md` file.
2. **Answer Questions**: For each question, tick the alternative that best describes the capability today and record its score.
3. **Calculate Total**: Sum the points to determine the GCS level using the scoring table provided in the template.
4. **Document Findings**: Save the completed assessment in a dated folder for future reference.

### Example Workflow

1. Clone the repository:
   ```bash
   git clone https://github.com/yanjustino/cbsoft-20205-artifacts-festival.git
   ```

2. Navigate to the `gcs` directory:
   ```bash
   cd gcs
   ```

3. Open the template:
   ```bash
   nano template-assessment.md
   ```

4. Fill out the questionnaire and save changes.

5. Commit the completed assessment:
   ```bash
   git add template-assessment.md
   git commit -m "Completed Granularity Assessment for <Capability>"
   ```

## Application of Mapping

The `template-mapping.md` file provides a structured approach to map implementation units to deployables and analyze their distribution across the Granularity Classification Spectrum (GCS). This template is designed to help architects and engineers:

1. **Map Units**: Identify where each implementation unit runs and its corresponding GCS level.
2. **Analyze Pipelines**: Evaluate the type of pipeline (shared, semi-independent, or independent) and data access patterns.
3. **Assess Metrics**: Document size (LOC/MB) and latency (p95) for each unit.

### How to Use the Template

1. **Open the Template**: Navigate to the `gcs` directory and open the `template-mapping.md` file.
2. **Fill in the Mapping Table**: Replace all `<!-- TODO -->` placeholders with the relevant information for each implementation unit.
3. **Document Findings**: Save the completed mapping in a dated folder for future reference.

### Example Workflow

1. Clone the repository:
   ```bash
   git clone https://github.com/yanjustino/cbsoft-20205-artifacts-festival.git
   ```

2. Navigate to the `gcs` directory:
   ```bash
   cd gcs
   ```

3. Open the template:
   ```bash
   nano template-mapping.md
   ```

4. Fill out the mapping table and save changes.

5. Commit the completed mapping:
   ```bash
   git add template-mapping.md
   git commit -m "Completed Mapping for Implementation Units"
   ```

### Contribution to CBSoft 2025

This template supports the CBSoft 2025 Artifacts Festival by providing a replicable artifact for mapping implementation units to deployables. It promotes transparency, reuse, and continuous improvement in software engineering research.

