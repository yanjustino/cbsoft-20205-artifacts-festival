from src.core.elasticity import Elasticity


def print_line(): print(f"{'+'.rjust(10, '-')}" * 11)


class ElasticityPrinter:
    def __init__(self, saturation: iter(type[Elasticity])):
        self.saturation = saturation

    def print(self):
        print()
        self.print_header()
        for sat in self.saturation:
            sat.to_string()
        print_line()
        self.print_footer()

    @staticmethod
    def print_header():
        print("Granularity Saturation Index".ljust(50))
        print_line()

        print(f"{'Quarter'.center(9)}|"
              f"{'TMS'.rjust(9)}|"
              f"{'RVI GRA'.rjust(9)}|"
              f"{'RVI EFT'.rjust(9)}|"
              f"{'RVI OPE'.rjust(9)}|"
              f"{'RVI COD'.rjust(9)}|"
              f"{'RVI FIN'.rjust(9)}|"
              f"{'RVI TOT'.rjust(9)}|"
              f"{'𝓔'.rjust(9)}|"
              f"{'𝓔n'.rjust(9)}|"
              f"{'class'.center(9)}")

        print_line()

    @staticmethod
    def print_footer():
        print("TMS = Total of Microservice; GRA = Granularity; PRO = Process; OPE = Operation; COD = Code;")
        print("FIN = Financial; TOT = Total")


        print()
        print("Elasticity..: \033[33m𝓔 = ∆ln(IRC)/∆ln(MSA)\033[0m".ljust(70))
        print("Elasticity..: \033[33m𝓔n = tanh(𝓔)\033[0m".ljust(70))
        print()
        print("CLASSIFICATION".ljust(70))
        print("(H) = \033[33m tanh(𝓔) > 0.75      | High Variation Zone\033[0m".ljust(70))
        print("(R) = \033[33m 0 < tanh(𝓔) <= 0.75 | Reduced Variation Zone\033[0m".ljust(70))
        print("(S) = \033[33m tanh(𝓔) < 0.10      | Saturation Zone\033[0m".ljust(70))
        print("(A) = \033[33m tanh(𝓔) < 0.00      | Adverse Effect Zone\033[0m".ljust(70))
        print()
