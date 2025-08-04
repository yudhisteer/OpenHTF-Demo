import openhtf as htf

@htf.measures(
    htf.Measurement("is_led_switch_on")
    .equals(True)
)
def phase_led(test):
    print("Checking LED switch status...")
    test.measurements.is_led_switch_on = True

def main():
    test = htf.Test(phase_led)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
