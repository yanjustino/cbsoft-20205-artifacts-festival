import math

from src.core.variation import Variation


class Elasticity:
    def __init__(self, period="", tms=0., rvi=0., gra=0., eft=0., ope=0., cod=0., fin=0., elt=0., eln=0.):
        self.period = period # period
        self.tms = tms # total of microservices
        self.gra = gra # rvi of granularity
        self.eft = eft # rvi of process
        self.ope = ope # rvi of operation
        self.cod = cod # rvi of code
        self.fin = fin # rvi of financial
        self.rvi = rvi # rvi total
        self.elt = elt # elasticity
        self.eln = eln # elasticity normalized
        self.cls = ""

        self.cls = "(U)"
        if elt > 0.75:
            self.cls = "(H)"
        if 0 < elt <= 0.75:
            self.cls = "(R)"
        if elt < 0.1:
            self.cls = "(S)"
        if elt < 0:
            self.cls = "(A)"


    def to_string(self):
        def format_value(value, size): 
            return f"|{f'{round(value, 2):.2f}'.rjust(size)}"

        print(f"{self.period.center(9)}" +
              format_value(self.tms, 9) +
              format_value(self.gra, 9) +
              format_value(self.eft, 9) +
              format_value(self.ope, 9) +
              format_value(self.cod, 9) +
              format_value(self.fin, 9) +
              format_value(self.rvi, 9) +
              format_value(self.elt, 9) +
              format_value(self.eln, 9) +
              f"|\033[33m{f'{self.cls}'.center(9)}\033[0m"
              )

    @staticmethod
    def create(current: Variation, previous: Variation):
        e = 10e-6

        # LOGARITHMIC
        delta_rvi = math.log(current.total + e) - math.log(previous.total + e)
        delta_msa = math.log(current.tms + e) - math.log(previous.tms + e)
        elast_tot = (delta_rvi / delta_msa)
        elast_tot_normalized = math.tanh(elast_tot)

        return Elasticity(
            period=current.period,
            tms=current.tms,
            gra=current.granularity,
            eft=current.effort,
            ope=current.operation,
            cod=current.code,
            fin=current.financial,
            rvi=current.total,
            elt=elast_tot,
            eln=elast_tot_normalized,
        )
