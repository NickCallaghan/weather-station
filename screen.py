from sense_hat import SenseHat
import time

hat = SenseHat()

colors = {
    'red': (100, 0, 0),
    'green': (0, 100, 0),
    'blue': (0, 0, 100),
    'white': (100, 100, 100)
}


def set_color_pulse(color_name='white', pulse_time=2):

    if colors[color_name]:
        hat.clear(colors[color_name])
        time.sleep(pulse_time)
        hat.clear()
