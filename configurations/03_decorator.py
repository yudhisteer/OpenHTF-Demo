import openhtf as htf
from openhtf.util import configuration

configuration.CONF.declare("phase_variance")
configuration.CONF.load(phase_variance=4)

@configuration.CONF.save_and_restore(phase_variance=55) # Decorator
def phase_one(test):
    phase_variance_to_print = configuration.CONF.phase_variance
    print(f"Value during phase one: {phase_variance_to_print}")

def phase_two(test):
    phase_variance_to_print = configuration.CONF.phase_variance
    print(f"Value during phase two: {phase_variance_to_print}")

def main():
    test = htf.Test(phase_one, phase_two)
    test.execute(test_start=lambda: "SN1234")

if __name__ == "__main__":
    main()
