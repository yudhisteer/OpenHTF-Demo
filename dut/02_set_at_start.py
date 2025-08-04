from openhtf import Test, PhaseResult

def power_on(test):
    print("DUT ID:", test.test_record.dut_id)
    return PhaseResult.CONTINUE

def main():
    test = Test(power_on)
    test.execute(lambda: 'SN1234') # Set at start

if __name__ == '__main__':
    main()
