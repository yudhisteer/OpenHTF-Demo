import openhtf as htf
from openhtf.output.callbacks import json_factory

class ExamplePlug(htf.plugs.BasePlug):
    def __init__(self):
        self.logger.info("Initialization")

    def tearDown(self):
        self.logger.info("Teardown phase")

    def do_something(self):
        self.logger.debug("Plug debugging details...")

@htf.plugs.plug(my_plug=ExamplePlug)
def phase_test(test, my_plug):
    test.logger.info("Test phase started.")
    test.logger.warning("Warning in test phase: Potential issue.")
    try:
        raise ValueError("Error occurred in test phase.")
    except ValueError as e:
        test.logger.error(f"Test phase error: {e}")
    my_plug.do_something()

def main():
    test = htf.Test(phase_test)
    test.add_output_callbacks(json_factory.OutputToJSON("test_result.json", indent=2)) # Exports results to JSON with pretty-printing
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()

