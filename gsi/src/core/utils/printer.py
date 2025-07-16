from src.core.utils.printer_metrics import MetricOutput
from src.core.utils.printer_variation import VariationOutput
from src.core.utils.printer_elasticity import ElasticityPrinter

class Printer:
    @staticmethod
    def print(inputs, grow, weight, saturation):
        MetricOutput(inputs).print()
        VariationOutput(grow, weight).print()
        ElasticityPrinter(saturation).print()