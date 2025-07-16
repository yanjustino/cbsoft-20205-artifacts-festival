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

## Structure

The artifact includes the following sections:
1. **Capability Identification**: Captures the name, business objective, and responsible teams for each capability.
2. **Inventory of Implementation Units**: Documents each unit's type, name, description, team, usage frequency, change frequency, dependencies, and runtime details (for FaaS).
3. **Mapping to Deployables**: Maps units to deployables, indicating their GCS level, pipeline type, data access, size, and latency.
4. **Consolidation & Analysis**: Analyzes the distribution of units by GCS level, identifies heterogeneity hotspots, and outlines risks and suggested actions.

## Usage

To use this artifact:
1. Replace all `<!-- TODO -->` markers in the questionnaire with real values.
2. Follow the tips provided in each section to ensure accurate and comprehensive documentation.
3. Commit the completed questionnaire to your repository with a clear message, e.g., "Granularity Report – <Capability>".
4. Repeat the assessment periodically and save new versions in dated folders.

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

3. **Review the Questionnaire**: Open the [survey-000](./survey-000.md) file and review the template provided.

> [!TIP]  
> You can also use the [survey-001](./survey-001.md) file as an example for filling out the questionnaire.

4. **Fill in the Template**: Replace all `<!-- TODO -->` placeholders with the relevant information for your study.

5. **Commit Changes**: Save your changes and commit them to the repository with a meaningful message.
   ```bash
   git add survey-000.md
   git commit -m "Completed Capability Granularity Mapping for <Capability>"
   ```

6. **Repeat Periodically**: Perform periodic assessments and save new versions in dated folders to track progress over time.

7. **Share Results**: Share the completed artifact with your team or submit it for evaluation as part of CBSoft 2025.

## Contribution to CBSoft 2025

This artifact contributes to the CBSoft 2025 Artifacts Festival by promoting Open Science and enabling transparency, replication, validation, and reuse of research findings. It adheres to the guidelines for artifact submission and badging, ensuring it is both available and functional.

