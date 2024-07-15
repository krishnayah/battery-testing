import time
import requests
import psutil
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://v8-3.foldingathome.org/machines")

LOW = 3
HIGH = 75

on_url = "https://api-v2.voicemonkey.io/trigger?token=e193146cf5cf43339a19aa5556506bd0_14122fd974d7274e08d46f0258e70e19&device=turn-on-smart-plug"
off_url = "https://api-v2.voicemonkey.io/trigger?token=e193146cf5cf43339a19aa5556506bd0_14122fd974d7274e08d46f0258e70e19&device=turn-off-smart-plug"

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return int(battery.percent)

def power_on():
    requests.get(on_url)

def power_off():
    requests.get(off_url)


def turn_folding_on():
    driver.get("https://v8-3.foldingathome.org/machines")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/a[1]").click()

def turn_folding_off():
    driver.get("https://v8-3.foldingathome.org/machines")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/a[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/a[1]").click()

minutes = 0
interval = 30
while True:
    battery = get_battery_percentage()
    print(battery)
    # log battery and time to log.csv
    with open('log.csv', 'a') as f:
        f.write(f"{minutes},{battery}\n")

    if battery >= HIGH:
        power_off()
        turn_folding_on()


    elif battery <= LOW:
        power_on()
        turn_folding_off()

    time.sleep(interval)
    minutes += interval / 60
