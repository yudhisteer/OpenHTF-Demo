import openhtf as htf
from openhtf.util import units

def MyPhaseFunction(test):
    """Define the function without any htf decorators that need to change at runtime"""
    test.measurements.resistance = 10.5

def main():
    # Get measurement limits dynamically at runtime
    min_ohms = 5
    max_ohms = 17  # These could come from configuration, user input, etc.

    # Create the measurement with dynamic parameters
    my_measurement = (htf.Measurement('resistance')
                      .with_units('ohm')
                      .in_range(minimum=min_ohms, maximum=max_ohms))

    # Apply the decorator as a callable to create the phase
    my_phase = htf.measures(my_measurement)(MyPhaseFunction)

    # Use the dynamically created phase in your test
    test = htf.Test([my_phase])
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
