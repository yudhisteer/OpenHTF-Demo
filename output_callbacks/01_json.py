from openhtf import Test, PhaseResult
from openhtf.output.callbacks import json_factory

def get_sn(test):
    test.test_record.dut_id = 'SN1234'
    return PhaseResult.CONTINUE

def main():
    test = Test(get_sn)
    # Exports results to JSON with pretty-printing
    test.add_output_callbacks(json_factory.OutputToJSON("test_result.json", indent=2))
    test.execute()

if __name__ == "__main__":
    main()
