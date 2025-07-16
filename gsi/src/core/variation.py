from src.core.metrics import Metric
from src.core.weight import Weight

class Variation:
    def __init__(self, weight: Weight, period="", tms=0, nms=0, tmb=0, eft=0, fch=0, loc=0,
                 cyc=0, cov=0, cst=0):
        self.weight = weight
        self.period = period
        self.tms = tms  # total microservices
        self.tmb = tmb  # team member variation
        self.nms = nms  # microservice granularity variation
        self.eft = eft  # effort variation
        self.fch = fch  # frequent change variation
        self.loc = loc  # LoC variation
        self.cyc = cyc  # Cycle Complexity variation
        self.cov = cov  # Coverage Variation
        self.cst = cst  # Infrastructure Cost variation

        self.granularity = nms / weight.total  # rvi of granularity
        self.effort = (tmb + eft) / weight.total  # rvi of process
        self.operation = fch / weight.total  # rvi of operation
        self.code = (loc + cyc + cov) / weight.total  # rvi of code
        self.financial = cst / weight.total  # rvi of finance
        self.total = (nms + (tmb + eft) + fch + (loc + cyc + cov) + cst) / weight.total

    @staticmethod
    def create(current: Metric, previous: Metric, weight: Weight):
        e = 10e-6

        def calculate(c, p): return (c - p) / (p + e)

        return Variation(
            weight=weight,
            period=current.period,
            tms=current.tms,
            tmb=calculate(current.tmb, previous.tmb) * weight.tmb,
            nms=calculate(current.nms, previous.nms) * weight.nms,
            eft=calculate(current.eft, previous.eft) * weight.eft,
            fch=calculate(current.fch, previous.fch) * weight.fch,
            loc=calculate(current.loc, previous.loc) * weight.loc,
            cyc=calculate(current.cyc, previous.cyc) * weight.cyc,
            cov=calculate(current.cov, previous.cov) * weight.cov,
            cst=calculate(current.cst, previous.cst) * weight.cst
        )

    def to_string(self):
        def format_value(value, size): 
            return f"|{f'{round(value, 4):.4f}'.rjust(size)}"

        print(f"{self.period.center(9)}" +
              format_value(self.nms, 9) +
              format_value(self.eft, 9) +
              format_value(self.tmb, 9) +
              format_value(self.fch, 9) +
              format_value(self.loc, 9) +
              format_value(self.cyc, 9) +
              format_value(self.cov, 9) +
              format_value(self.cst, 9)
              )