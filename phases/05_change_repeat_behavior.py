import openhtf as htf
import random

@htf.PhaseOptions(force_repeat=True, repeat_limit=3)
def repeat_phase(test):
    print("Repeating phase...")
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(repeat_on_timeout=True)
def timeout_phase(test):
    print("Timeout phase executed.")
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(stop_on_measurement_fail=True)
def random_fail_phase(test):
    if random.choice([True, False]):
        print("Random fail phase succeeded.")
        return htf.PhaseResult.CONTINUE
    else:
        print("Random fail phase failed.")
        return htf.PhaseResult.STOP

# This test won't be run if random_fail_phase is FAIL.
def always_true_phase(test):
    print("Always true phase executed.")
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(repeat_phase, timeout_phase, random_fail_phase, always_true_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
