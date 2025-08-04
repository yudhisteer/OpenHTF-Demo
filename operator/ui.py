import openhtf as htf
from openhtf.output.servers import station_server
from openhtf.output.web_gui import web_launcher
from openhtf.plugs import user_input
from openhtf.util import configuration
from openhtf.plugs.user_input import UserInput

CONF = configuration.CONF


@htf.measures(htf.Measurement("hello_world_measurement"))
def hello_world(test):
    test.logger.info("Hello World!")
    test.measurements.hello_world_measurement = "Hello Again!"


@htf.plug(user_input=UserInput)
def prompt_operator_next(test, user_input):
  is_connected = user_input.prompt(
      message="Click Okay when the LED turn on",
      text_input=False, # Button prompt from operator
  )


@htf.measures(
    htf.Measurement("led_color").with_validator(
        lambda color: color in ["Red", "Green", "Blue"]
    )
)
@htf.plug(user_input=UserInput)
def prompt_operator_led_color(test, user_input):
    led_color = user_input.prompt(
        message="What is the LED color? (Red/Green/Blue)",
        text_input=True,  # Text prompt from operator
    )
    test.measurements.led_color = led_color


def main():
    CONF.load(station_server_port="4444")
    with station_server.StationServer() as server:
        web_launcher.launch("http://localhost:4444")
        test = htf.Test(
            hello_world,
            prompt_operator_next,
            prompt_operator_led_color)
        test.add_output_callbacks(server.publish_final_state)
        test.execute(test_start=user_input.prompt_for_test_start())


if __name__ == "__main__":
    main()
