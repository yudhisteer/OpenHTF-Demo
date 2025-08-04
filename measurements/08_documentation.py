import openhtf as htf

@htf.measures(
    htf.Measurement("temperature")
    .in_range(0, 100)
    .doc("This measurement tracks the ambient temperature during the test.")
)
def phase_temperature(test):
    test.measurements.temperature = 25

def main():
    test = htf.Test(phase_temperature)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
