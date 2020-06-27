
from sense_hat import SenseHat
from sensor_store import SensorStore
import time
from gpiozero import CPUTemperature
import screen

hat = SenseHat()
db = SensorStore('store.db')

sleep_between_readings = 300


def display_message(text):
    '''Prints a scrolling message to sense hat display'''
    text_color = (50, 50, 50)
    text_background = (0, 0, 0)
    hat.show_message(text, 0.1, text_color, text_background)


def write_temp_to_db():
    temp = round(hat.get_temperature_from_pressure(), 2)
    db.write_sensor_reading(temp, "TEMP")
    print(f'Temp: {temp}')


def write_pressure_to_db():
    pressure = round(hat.get_pressure(), 2)
    db.write_sensor_reading(pressure, 'PRESSURE')
    print(f'Pressure: {pressure}')


def write_cpu_to_db():
    cpu_temp = round(CPUTemperature().temperature, 2)
    db.write_sensor_reading(cpu_temp, "CPU")
    print(f'CPU Temp: {cpu_temp}')


if __name__ == '__main__':
    display_message('Starting Up')
    print('Starting weather station')
    while True:
        write_temp_to_db()
        write_pressure_to_db()
        write_cpu_to_db()
        screen.set_color_pulse(color_name='blue')
        time.sleep(sleep_between_readings)
