from openhtf import Test, PhaseResult
from openhtf.plugs import user_input

def power_on(test):
    return PhaseResult.CONTINUE

def main():
    test = Test(power_on)
    test.execute(test_start=user_input.prompt_for_test_start()) # Prompt at start

if __name__ == '__main__':
    main()
