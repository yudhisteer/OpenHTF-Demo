import openhtf as htf

def phase_one(test):
    print("Executing phase one")
    print("DUT ID:", test.test_record.dut_id) # DUT ID: SN1234
    return htf.PhaseResult.CONTINUE

def phase_two(test):
    print("Executing phase two")
    print("DUT ID:", test.test_record.dut_id) # DUT ID: SN1234
    return htf.PhaseResult.STOP

def main():
    test = htf.Test(phase_one, phase_two)
    result = test.execute(lambda: "SN1234")
    print("Test passed:", result) # True if all phases passed

if __name__ == '__main__':
    main()
