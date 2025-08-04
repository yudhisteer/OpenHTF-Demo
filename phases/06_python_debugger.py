import openhtf as htf

@htf.PhaseOptions(run_under_pdb=True, timeout_s=20)
def first_phase(test):
    print("First phase executed.")
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(first_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()

