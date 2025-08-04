from openhtf import Test, PhaseResult

def get_sn(test):
    test.test_record.dut_id = 'SN1234' # Set during test
    return PhaseResult.CONTINUE

def main():
    test = Test(get_sn)
    test.execute()

if __name__ == '__main__':
    main()
