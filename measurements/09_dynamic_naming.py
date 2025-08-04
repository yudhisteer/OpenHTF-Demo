import openhtf as htf

@htf.measures(
    htf.Measurement("test_result_{level}")
    .with_args(level="high")
    .equals(True)
)
def phase_test(test):
    test.measurements.test_result_high = True

def main():
    test = htf.Test(phase_test)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
