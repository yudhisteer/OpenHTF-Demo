import openhtf as htf
from openhtf import PhaseNameCase

@htf.PhaseOptions(name="new_phase_name", phase_name_case=PhaseNameCase.CAMEL)
def example_phase(test):
    print()
    return htf.PhaseResult.CONTINUE

def main():
  test = htf.Test(example_phase)
  test.execute(lambda: "SN1234")

if __name__ == '__main__':
  main()
