import openhtf as htf
import random

# Always pass
def phase_pass(test):
    return htf.PhaseResult.CONTINUE

# Retries on failure
def phase_retry(test):
    if random.choice([True, False]): # Randomly decide to pass or fail
        print("Phase retry passed")
        return htf.PhaseResult.CONTINUE
    else:
        print("Phase retry failed, will repeat")
        # This will cause the phase to repeat
        return htf.PhaseResult.REPEAT

# Fail and stop the test
def phase_fail(test):
    return htf.PhaseResult.STOP

def main():
    test = htf.Test(phase_pass, phase_retry, phase_fail)
    test.execute(lambda: "SN1234")

if __name__ == '__main__':
    main()
