import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement('resistance')
    .with_units('ohm')
    .in_range(minimum=5, maximum=17, marginal_minimum=9, marginal_maximum=11)
)
def phase_marginal(test):
  test.measurements.resistance = 13

def main():
    test = htf.Test(phase_marginal)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
