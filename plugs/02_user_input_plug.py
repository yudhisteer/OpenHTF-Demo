import openhtf as htf
from openhtf.plugs.user_input import UserInput

@htf.measures(
    htf.Measurement("led_color")
    .with_validator(lambda color: color in ["Red", "Green", "Blue"])
)
@htf.plug(user_input=UserInput)
def prompt_operator_led_color(test, user_input):
    # text_input defaults to False when not specified
    led_color = user_input.prompt(
        message="What is the LED color? (Red/Green/Blue)",
        text_input=True  # Displays a text input field where the operator types a response
    )
    test.measurements.led_color = led_color

def main():
    test = htf.Test(prompt_operator_led_color)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()
