import openhtf as htf
from openhtf.util import configuration

# Declare the firmware_path key
configuration.CONF.declare("firmware_path")

# Load configuration from an external YAML file
with open("config.yaml", "r") as yamlfile:
    configuration.CONF.load_from_file(yamlfile)

def flash_firmware(test):
    firmware_path = configuration.CONF.firmware_path
    print(f"Flashing firmware from: {firmware_path}")

def main():
    test = htf.Test(flash_firmware)
    test.execute(test_start=lambda: "SN1234")

if __name__ == "__main__":
    main()
