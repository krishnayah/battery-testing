import time
import requests
import psutil

LOW = 20
HIGH = 80

on_url = "https://api-v2.voicemonkey.io/trigger?token=GIBBERISH58e70e19&device=turn-on-smart-plug"
off_url = "https://api-v2.voicemonkey.io/trigger?token=GIBBERISH&device=turn-off-smart-plug"

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return int(battery.percent)

def power_on():
    requests.get(on_url)

def power_off():
    requests.get(off_url)


while True:

    while True:
        time.sleep(30)
        battery = get_battery_percentage()
        print(battery)
        if battery >= HIGH:

            power_off()

        elif battery <= LOW:
            power_on()


