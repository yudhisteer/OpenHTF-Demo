import openhtf as htf

@htf.PhaseOptions()
def check_condition(test):
    print("Checking condition")
    return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(requires_state=True)
def conditional_phase(test_state):
    check_condition(test_state)  # Manually invoke another phase

def main():
    test = htf.Test(conditional_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
