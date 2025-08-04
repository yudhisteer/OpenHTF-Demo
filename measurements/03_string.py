import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement("firmware_version")
    .equals("1.2.4")
)
def phase_firmware(test):
    print("Measuring firmware version...")
    test.measurements.firmware_version = "1.2.4"

def main():
    test = htf.Test(phase_firmware)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
