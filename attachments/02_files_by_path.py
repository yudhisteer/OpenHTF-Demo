import openhtf as htf

def phase_file_attachment(test):
    test.attach_from_file("test_result.json")
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_file_attachment)
    test.execute(lambda: "PCB0001")

if __name__ == "__main__":
    main()
