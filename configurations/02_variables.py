import openhtf as htf
from openhtf.util import configuration

# Define firmware_path configuration
configuration.CONF.declare(
    "firmware_path",
    default_value="path/to/firmware_v1.0.0.bin",
    description="Path to the firmware file",
)

def flash_firmware(test):
    firmware_path = configuration.CONF.firmware_path
    print(f"Flashing firmware from: {firmware_path}")

def main():
    test = htf.Test(flash_firmware)
    test.execute(test_start=lambda: "SN1234")

if __name__ == "__main__":
    main()
