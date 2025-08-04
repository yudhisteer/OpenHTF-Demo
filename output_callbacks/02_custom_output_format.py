import openhtf as htf

def custom_output_callback(test_record):
    with open("./custom_output.txt", "w") as f:
        f.write("Custom Output\n")
        f.write(f"DUT ID: {test_record.dut_id}\n")
        f.write(f"Outcome: {test_record.outcome}\n")
        for phase in test_record.phases:
            f.write(f"Phase: {phase.name}\n")

def get_sn(test):
    test.test_record.dut_id = "SN1234"
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(get_sn)
    test.add_output_callbacks(custom_output_callback)
    test.execute()

if __name__ == "__main__":
    main()
