import openhtf as htf

def phase_attachment(test):
    # Attach a binary log with the identifier "test_attachment"
    test.attach("test_attachment", "This is test log data.".encode("utf-8"))
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_attachment)
    test.execute(lambda: "PCB0001")

if __name__ == "__main__":
    main()
