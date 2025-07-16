class Weight:
    """Class to represent weights for different software core."""

    nms: int = 1  # amount of microservices weight
    tmb: int = 1  # team members weight
    eft: int = 1  # effort weight
    fch: int = 1  # frequency of changes weight
    loc: int = 1  # lines of code weight
    cyc: int = 1  # cyclomatic complexity weight
    cov: int = -1  # coverage weight
    cst: int = 1  # cost weight

    @property
    def total(self) -> int:
        """Calculate total weight from all components."""
        return self.nms + self.tmb + self.eft + self.fch + self.loc + self.cyc + self.cov + self.cst

    @staticmethod
    def _format_value(value: int, width: int) -> str:
        """Format a numeric value for display."""
        return f"|{str(value).rjust(width)}"

    def to_string(self) -> str:
        """Return a formatted string representation of the weights."""
        result = f"{'𝑤'.center(9)}"
        result += self._format_value(self.nms, 9)
        result += self._format_value(self.tmb, 9)
        result += self._format_value(self.eft, 9)
        result += self._format_value(self.fch, 9)
        result += self._format_value(self.loc, 9)
        result += self._format_value(self.cyc, 9)
        result += self._format_value(self.cov, 9)
        result += self._format_value(self.cst, 9)
        return result

    def print_weights(self) -> None:
        """Print the formatted weights to console."""
        print(self.to_string())