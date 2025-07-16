

class Metric:
    """Class to represent software development core for a specific period."""

    def __init__(self,
        period: str = "",
        nms: int = 0,
        tms: int = 0,
        tmb: int = 0,
        est: float = 0.0,
        act: float = 0.0,
        eft: float = 0.0,
        nch: int = 0,
        fch: float = 0.0,
        loc: int = 0,
        cyc: int = 0,
        cov: float = 0.0,
        cst: float = 0.0,
    ):
        self.period = period
        self.nms = nms
        self.tms = tms
        self.tmb = tmb
        self.est = est
        self.act = act
        self.eft = eft
        self.nch = nch
        self.fch = fch
        self.loc = loc
        self.cyc = cyc
        self.cov = cov
        self.cst = cst

    def to_string(self) -> str:
        """Return a formatted string representation of the core."""
        def format(value, size):
            return f"|{str(f'{value:.2f}').rjust(size)}"

        return (
            f"{self.period.center(9)}"
            + format(self.nms, 10)
            + format(self.tms, 9)
            + format(self.tmb, 9)
            + format(self.est, 9)
            + format(self.act, 9)
            + format(self.eft, 9)
            + format(self.nch, 9)
            + format(self.fch, 9)
            + format(self.loc, 9)
            + format(self.cyc, 9)
            + format(self.cov, 9)
            + format(self.cst, 10)
        )

    def print_metrics(self) -> None:
        """Print the formatted core to console."""
        print(self.to_string())