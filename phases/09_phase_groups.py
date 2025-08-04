import openhtf as htf
from openhtf.util import units

def setup_phase(test):
    print("Running setup phase")
    return htf.PhaseResult.CONTINUE

def first_measurement_phase(test):
    print("Running first measurement phase")
    return htf.PhaseResult.CONTINUE

def second_measurement_phase(test):
    print("Running second measurement phase")
    return htf.PhaseResult.STOP

def teardown_phase(test):
    print("Running teardown phase")
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(
        htf.PhaseGroup(
            setup=[setup_phase], # Setup phase runs first
            main=[first_measurement_phase, second_measurement_phase], # Main phases run next
            teardown=[teardown_phase], # Teardown phase runs last
        )
    )
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
