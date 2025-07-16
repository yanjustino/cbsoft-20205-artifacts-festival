from saturation import Saturation

# Load metrics from a CSV file
metrics = Saturation.load_metrics_from_csv('data/metrics.csv')

# Execute saturation analysis
Saturation.execute(metrics)