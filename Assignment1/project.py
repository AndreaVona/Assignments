#!/usr/bin/env python
import signal #just for testing purposes
import sys

import paho.mqtt.client as mqtt
import time,json

# generate random floating point values
from random import seed
from random import random
# seed random number generator
seed(1)

#
from sensors import *

# Creating Sensors for Environmental Station 1
temperatureSensor1 = SensorTemperature(True)
humiditySensor1 = SensorHumidity(True)
windDirSensor1 = SensorWindDirection(True)
windIntSensor1 = SensorWindIntensity(True)
rainHeightSensor1 = SensorRainHeight(True)

# Creating Sensors for Environmental Station 2
temperatureSensor2 = SensorTemperature(True)
humiditySensor2 = SensorHumidity(True)
windDirSensor2 = SensorWindDirection(True)
windIntSensor2 = SensorWindIntensity(True)
rainHeightSensor2 = SensorRainHeight(True)

# just some logs to check everything is working
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  
def on_disconnect(client, userdata, rc):
   print("client disconnected ok")
def on_publish(client, userdata, mid):
    print("In on_pub callback mid= "  ,mid)
count=0 # keeps track of the number of publish


mqtt.Client.connected_flag=False    #create flag in class
mqtt.Client.suppress_puback_flag=False


client1 = mqtt.Client("python1")     #create new instance of the mqtt client
client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_publish = on_publish

client2 = mqtt.Client("python1")     #create new instance of the mqtt client
client2.on_connect = on_connect
client2.on_disconnect = on_disconnect
client2.on_publish = on_publish

broker="demo.thingsboard.io"
port =1883
topic="v1/devices/me/telemetry"

#need to edit user name 
username="nPYOEsgYdx73gcVU2VFR" #Station-1 id token
password=""
client1.username_pw_set(username, password)
client1.connect(broker,port)      #establish connection with client1

#need to edit user name 
username2="FvEzUeX949r31crGraJG" #Station-2 id toke
password2=""
client2.username_pw_set(username2, password2)
client2.connect(broker,port)      #establish connection with client2

while not client1.connected_flag and not client2.connected_flag: #wait in loop
   client1.loop()
   client2.loop()
   time.sleep(1)
time.sleep(3)

data=dict()     #data who is to be modified at each iteration with random values

# handler of sig_int for making sure that
# the clients would disconnect 
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    client1.disconnect()
    client2.disconnect()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


while True:
    data["temperature"]=temperatureSensor1.sendData()
    data["humidity"]=humiditySensor1.sendData()
    data["windDirection"]=windDirSensor1.sendData()
    data["windIntensity"]=windIntSensor1.sendData()
    data["rainHeight"]=rainHeightSensor1.sendData()
    data_out=json.dumps(data) # creates a string JSON object
    print("publish topic",topic, "data out= ",data_out)
    ret=client1.publish(topic,data_out,0)    # client1 (station-1) publishes data to topic

    time.sleep(3)
    client1.loop()
    
    # it's the same but for client2 (Station-2)
    data["temperature"]=temperatureSensor2.sendData()
    data["humidity"]=humiditySensor2.sendData()
    data["windDirection"]=windDirSensor2.sendData()
    data["windIntensity"]=windIntSensor2.sendData()
    data["rainHeight"]=rainHeightSensor2.sendData()
    data_out=json.dumps(data)
    print("publish topic",topic, "data out= ",data_out)
    ret=client2.publish(topic,data_out,0)

    time.sleep(3)
    client2.loop()  
