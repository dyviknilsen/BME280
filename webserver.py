# BME280 Indoor Climate Presentation Page by Jonas Dyvik Nilsen
# Importing required libraries
import usocket as socket
import time
from machine import Pin, I2C
import BME280

# Defining sensor variables
i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
bme = BME280.BME280(i2c=i2c)

# Script
# Reads the BME280 sensors and defines various values, strings and colors every time a new HTTP request is recieved.
def script():
    # Defining global variables
    global temp_float
    global humi_float
    global pres_float
    global temp_color
    global temp_status
    global humi_color
    global humi_status
    global pres_color
    global graphic_temp
    global graphic_humi
    global graphic_pres

    # Defining float values based on sensor readings
    temp_float = float(bme.temperature)
    humi_float = float(bme.humidity)
    pres_float = float(bme.pressure)

    # Defining the color and written status of the temperature bar based on the current temperature
    if temp_float < 17:
        temp_color = "#3333ff"
        temp_status = "cold"
    elif temp_float < 19:
        temp_color = "#3366ff"
        temp_status = "slightly cold"
    elif temp_float < 25:
        temp_color = "#29cd29"
        temp_status = "good"
    elif temp_float < 27:
        temp_color = "#ff6633"
        temp_status = "slightly hot"
    else:
        temp_color = "#ff3333"
        temp_status = "hot"

    # Defining the color and written status of the air humidity bar based on the current humidity percentage
    if humi_float < 30:
        humi_color = "#ff3333"
        humi_status = "low"
    elif humi_float < 50:
        humi_color = "#29cd29"
        humi_status = "good"
    else:
        humi_color = "#ff3333"
        humi_status = "high"

    # Defining the color of the atmospheric pressure bar
    pres_color = "#a8a8a8"

    # Defining values for the temperature bar, which measures from -40C (practically -39C, to stop the bar from not showing any color at or below -40C) to +60C
    # Includes fail-safe
    if temp_float < -39:
        graphic_temp = 1
    elif temp_float > 60:
        graphic_temp = 100
    else:
        graphic_temp = (temp_float+40)

    # Defining values for the air humidity bar, which measures from 0% (practically 1%, to stop the bar from not showing any color at or below 1%) to 100%
    # Includes fail-safe
    if humi_float < 1:
        graphic_humi = 1
    elif humi_float > 100:
        graphic_humi = 100
    else:
        graphic_humi = humi_float

    # Defining values for the atmospheric pressure bar, which measures from 0hPa (practically 50hPa, to stop the bar from not showing any color at or below 50hPa) to 5000hPa
    # Includes fail-safe
    if pres_float < 50:
        graphic_pres = 1
    elif pres_float > 5000:
        graphic_pres = 100
    else:
        graphic_pres = pres_float/20

# Index
# Retrieves an HTML document from folder, and inserts global variables from script
# HTML document retrieves favicon and stylesheet from https://dyviknilsen.no/
def index():
    header = 'HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    raw_html = open("index.html", "rt")
    html = raw_html.read().format(temp_status=temp_status, temp=temp_float, temp_color=temp_color, graphic_temp=graphic_temp, humi_status=humi_status, humi=humi_float, humi_color=humi_color, graphic_humi=graphic_humi, pres=pres_float, pres_color=pres_color, graphic_pres=graphic_pres)
    return header + html

# Web Server
# Listens for HTTP request, runs the script and responds with the index page
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    script()
    response = index()
    conn.send(response)
    conn.close()
