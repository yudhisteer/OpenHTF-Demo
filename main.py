import openhtf as htf

def hello_world(test):              # Define "hello_world" phase
    print('Hello world!')
    return htf.PhaseResult.CONTINUE # Continue to next phase

def main():
    test = htf.Test(hello_world)    # Define test with hello_world
    test.execute(lambda: "SN1234")  # Execute with DUT serial

if __name__ == '__main__':
    main()                          # Run main function
