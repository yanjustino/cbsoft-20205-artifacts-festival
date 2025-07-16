# Granularity Saturation Index (GSI)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the research artifact for the Granularity Saturation Index (GSI), a composite instrument used in Granulify—an approach for continuous management of microservice granularity. The GSI classifies granularity evolution into distinct zones, indicating whether architectural changes lead to improvements, stagnation, or degradation.

## Abstract

The Granularity Saturation Index (GSI) provides a quantitative framework for evaluating microservice architectural trends and identifying critical saturation points in service granularity. Through continuous monitoring of weighted variations across multiple software engineering dimensions, GSI enables dynamic adjustment of granularity levels, balancing modularity, performance, and operational cost.

## Core Concepts

The GSI consists of two main aggregated indicators:

### Relative Variation Index (RVI)
- **Purpose**: Quantifies weighted relative variations across different software engineering dimensions
- **Dimensions**: Granularity, development effort, operations, code quality, and financial aspects
- **Calculation**: For metric j in quarter i: `γji = (xji − xji−1) / (xji−1 + ϵ)`
- **Weighting**: Each metric receives directional weights indicating positive/negative impact

### Elasticity (E)
- **Purpose**: Measures sensitivity of RVI variations relative to changes in microservice count
- **Formula**: Ratio between logarithmic growth rates of total variation (RVI) and microservice count over time
- **Zones**:
  - **High Variation Zone (E > 1)**: Architectural instability and overhead
  - **Reduced Variation Zone (0 < E < 1)**: System approaching structural balance
  - **Saturation Zone (E ≈ 0)**: Stabilization point reached
  - **Adverse Effect Zone (E < 0)**: Quality degradation requiring intervention

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Installation

```bash
# Clone the repository
git clone https://github.com/yanjustino/cbsoft-2025-artifacts-festival.git
cd gsi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from saturation import Saturation

# Load metrics from a CSV file
metrics = Saturation.load_metrics_from_csv('data/metrics.csv')

# Execute saturation analysis
Saturation.execute(metrics)
```

### Input Data Format

The tool expects CSV data with the following structure:
- Metric values across different quarters
- Multiple dimensions: granularity, effort, operations, code, financial
- Microservice count (NMS) for elasticity calculation

### Expected Output

The tool provides:
- RVI calculations for each dimension and quarter
- Total RVI aggregation across all dimensions
- Elasticity values indicating architectural behavior
- Zone classification (High Variation, Reduced Variation, Saturation, Adverse Effect)
- Visual trends and saturation point identification

## Project Architecture

```
├── src/
│   ├── saturation.py      # Main GSI orchestration class
│   ├── core/
│   │   ├── metric.py      # Metric data structure
│   │   ├── variation.py   # RVI calculation logic
│   │   ├── elasticity.py  # Elasticity computation
│   │   ├── weights.py     # Directional weight utilities
│   │   └── utils/
│   │       └── printer.py # Result formatting and display
├── data/                  # Example microservice metric datasets
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Algorithm Overview

1. **Data Loading**: Processes microservice metrics across quarters and dimensions
2. **RVI Calculation**: Computes weighted relative variations for each dimension
3. **Elasticity Analysis**: Measures RVI sensitivity to microservice count changes
4. **Zone Classification**: Categorizes architectural behavior into distinct zones
5. **Saturation Detection**: Identifies critical points for granularity management

## Research Context

This tool supports research in microservice architecture evolution, particularly for:
- Continuous monitoring of service granularity effectiveness
- Identifying optimal fragmentation levels in microservice systems
- Supporting architectural decision-making through quantitative analysis
- Evaluating the impact of granularity changes on system quality

## Case Study Results

Application in a real-world project demonstrated:
- **Exploratory Phase (23Q2-23Q4)**: High elasticity (E = 1.73) indicating structural exploration
- **Production Deployment (24Q1+)**: Negative elasticity (E = -8.15, -3.47) revealing adverse effects
- **Zone Transitions**: Clear identification of architectural behavior changes over time

## Artifact Evaluation

This artifact is designed for:
- **Functional**: Complete GSI calculation and zone classification
- **Reusable**: Applicable to various microservice architecture studies
- **Available**: Open source implementation with example datasets
- **Documented**: Comprehensive methodology and usage guidelines

## Citation

If you use this tool in your research, please cite:

```bibtex
@misc{gsi-granulify-2025,
  title={Granularity Saturation Index (GSI): A Tool for Microservice Granularity Management},
  author={Your Name},
  year={2025},
  url={https://github.com/yanjustino/cbsoft-2025-artifacts-festival}
}
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit changes (`git commit -am 'Add new GSI analysis method'`)
4. Push to branch (`git push origin feature/new-analysis`)
5. Create Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For questions about this artifact, the GSI methodology, or the underlying Granulify approach, please open an issue in this repository.