from src.core.metrics import Metric


def print_header():
    def print_line():
        print(f"{'+'.rjust(10, '-')}"
              f"{'+'.rjust(21, '-')}"
              f"{'+'.rjust(40, '-')}"
              f"{'+'.rjust(20, '-')}"
              f"{'+'.rjust(30, '-')}"
              f"{''.rjust(10, '-')}")

    print()
    print("Metrics".ljust(120))
    print_line()

    print(f"{'Period'.rjust(9)}|"
          f"{'Granularity'.center(20)}|"
          f"{'Effort'.center(39)}|"
          f"{'Operation'.center(19)}|"
          f"{'Code'.center(29)}|"
          f"{'Financial'.rjust(10)}")

    print_line()

    print(f"{''.center(9)}|"
          f"{'NMS'.rjust(10)}|"
          f"{'TMS'.rjust(9)}|"
          f"{'TMB'.rjust(9)}|"
          f"{'EST'.rjust(9)}|"
          f"{'ACT'.rjust(9)}|"
          f"{'EFT'.rjust(9)}|"
          f"{'CHG'.rjust(9)}|"
          f"{'CHG'.rjust(9)}|"
          f"{'LOC'.rjust(9)}|"
          f"{'CYC'.rjust(9)}|"
          f"{'COV'.rjust(9)}|"
          f"{'CST'.rjust(10)}")


def print_bottom_line():
    print(f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(10, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(9, '-')}+"
          f"{'-'.rjust(10, '-')}")


def print_footer():
    print(
          'NMS = Microservice; '
          'TMB = Team Members; '
          'EST = Estimated; '
          'ACT = Actual; '
          'EFT = Effort; '
          'CHG = Change; '
    )

    print(
          'LOC = Line of Code; '
          'CYC = Cyclomatic Complexity; '
          'COV = Code Coverage; '
          'CST = Infrastructure cost;'
    )


class MetricOutput:
    def __init__(self, metrics: iter(type[Metric])):
        self.metrics = metrics

    def print(self):
        print_header()
        print_bottom_line()
        for metric in self.metrics:
            metric.print_metrics()
        print_bottom_line()
        print_footer()
        print()

