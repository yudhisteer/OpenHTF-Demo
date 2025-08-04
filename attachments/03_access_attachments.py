import openhtf as htf

def phase_attachment(test):
    # Attach some data
    test.attach("test_attachment", "Attachment data".encode("utf-8"))

    # Retrieve and print the attached data
    test_attachment = test.get_attachment("test_attachment")
    print(test_attachment.data)

    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(phase_attachment)
    test.execute(lambda: "PCB0001")

if __name__ == "__main__":
    main()
