import openhtf as htf
import logging

# Define a test phase that logs information
@htf.measures(htf.Measurement('temperature').with_units('C'))
def temperature_measurement(test):
    test.logger.info('Temperature measurement started.')
    test.measurements.temperature = 25
    test.logger.info('Temperature measurement completed.')

def main():
    # Get the OpenHTF logger
    logger = logging.getLogger('openhtf')

    # Create a custom log format with additional details:
    # - %(asctime)s: Adds a timestamp to each log message.
    # - %(name)s: Includes the name of the logger (in this case, 'openhtf').
    # - %(levelname)s: Logs the level of the message (INFO, DEBUG, WARNING, ERROR, etc.).
    # - %(lineno)d: Adds the line number where the log was created.
    # - %(message)s: The actual log message.
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | [%(levelname)s] | Line: %(lineno)d | %(message)s'
    )

    # Create a stream handler that will output logs to the console (stdout)
    handler = logging.StreamHandler()

    # Apply the custom format to the handler
    handler.setFormatter(formatter)

    # Attach the handler to the logger
    logger.addHandler(handler)

    # Set the logging level to INFO (it will log INFO, WARNING, and ERROR messages)
    logger.setLevel(logging.INFO)

    test = htf.Test(temperature_measurement)
    test.execute(test_start=lambda: 'SN1234')

if __name__ == '__main__':
    main()
