import openhtf as htf
import random

def first_phase(test):
    print("Running first phase")
    return htf.PhaseResult.CONTINUE

# Will always fail, but only runs if a condition is met
@htf.PhaseOptions(run_if=lambda: random.choice([True, False]))
def conditional_fail_phase(test):
    # This phase will run conditionally based on the run_if option is True
    print("Running conditional fail phase")
    return htf.PhaseResult.STOP

# Will run if the conditional_fail_phase is not executed
def last_phase(test):
    print("Running last phase")
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(first_phase, conditional_fail_phase, last_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
