import openhtf as htf
from openhtf.util import units

@htf.measures(
    htf.Measurement("temperature")     # Declares the measurement name
    .in_range(0, 100)                  # Defines the validator
    .with_units(units.DEGREE_CELSIUS)  # Specifies the unit
    .with_precision(1)                 # Rounds to 1 decimal place
)

def phase_temperature_pass(test):
    print("Starting temperature measurement phase valid")
    test.measurements.temperature = 25 # Set the temperature value to 25°C

def phase_temperature_fail(test):
    print("Starting temperature measurement phase invalid")
    test.measurements.temperature = 125  # Set the temperature value to 125°C (invalid)

def main():
    test = htf.Test(phase_temperature_pass, 
                    phase_temperature_fail)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
