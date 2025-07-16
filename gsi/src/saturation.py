import csv

from core.utils.printer import Printer
from core.elasticity import Elasticity
from core.variation import Variation
from core.metrics import Metric
from core.weight import Weight

class Saturation:
    @staticmethod
    def execute(inputs: iter(type[Metric])):
        weight = Weight()
        variations = Saturation.calculate_variations(inputs, weight)
        elasticity = Saturation.calculate_elasticity(variations)
        Printer.print(inputs, variations, weight, elasticity)


    @staticmethod
    def calculate_variations(metrics: iter(type[Metric]), weight: Weight):
        """Calculate relative variation indices for the given core."""
        rates = []
        for i, current in enumerate(metrics):
            previous = metrics[i - 1] if i > 0 else None
            rates.append(
                Variation.create(current, previous, weight) if previous else Variation(weight, current.period)
            )
        return rates

    @staticmethod
    def calculate_elasticity(rates: iter(type[Variation])):
        """Calculate saturation values for the given rates."""
        result = []
        for i, current in enumerate(rates):
            previous = rates[i - 1] if i > 0 else None
            result.append(
                Elasticity.create(current, previous) if previous else Elasticity(current.period)
            )
        return result

    @staticmethod
    def load_metrics_from_csv(file: str):
        """Load core data from CSV file and return list of Metric objects."""
        result = []
        with open(file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                metric = Metric(
                    period=row['period'],
                    nms=int(row['nms']),
                    tms=int(row['tms']),
                    tmb=int(row['tmb']),
                    est=float(row['est']),
                    act=float(row['act']),
                    eft=float(row['eft']),
                    nch=int(row['nch']),
                    fch=float(row['fch']),
                    loc=int(row['loc']),
                    cyc=int(row['cyc']),
                    cov=float(row['cov']),
                    cst=float(row['cst'])
                )
                result.append(metric)
        return result