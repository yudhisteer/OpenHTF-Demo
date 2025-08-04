from openhtf import plugs
import random
import openhtf as htf

class MultimeterPlug(plugs.BasePlug):
    def __init__(self):
        # Simulate connecting to the multimeter
        self.connected = True

    def tearDown(self):
        # Automatically called by OpenHTF after the test to clean up
        self.connected = False

    def measure_voltage(self):
        # Simulate voltage measurement
        return random.uniform(0, 10)

    def measure_current(self):
        # Simulate current measurement
        return random.uniform(0, 2)



@htf.plug(multimeter=MultimeterPlug)
def phase_test(test, multimeter):
    # Use the plug to measure voltage and current
    voltage = multimeter.measure_voltage()
    print("Measured Voltage:", voltage)
    current = multimeter.measure_current()
    print("Measured Current:", current)

def main():
    test = htf.Test(phase_test)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
