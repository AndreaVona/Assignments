# generate random floating point values
from random import seed
from random import random
# seed random number generator
seed(1)

class SensorTemperature:

    def __init__(self, exists):
        self.__exists = exists

    def sendData(self):
        value = (random()*100)-50
        value = str(round(value, 2))
        value = float(value)
        return value

class SensorHumidity:

    def __init__(self, exists):
        self.__exists = exists

    def sendData(self):
        value = (random()*100)
        value = str(round(value, 2))
        value = float(value)
        return value

class SensorWindDirection:

    def __init__(self, exists):
        self.__exists = exists

    def sendData(self):
        value = (random()*360)
        value = str(round(value, 2))
        value = float(value)
        return value

class SensorWindIntensity:

    def __init__(self, exists):
        self.__exists = exists

    def sendData(self):
        value = (random()*100)
        value = str(round(value, 2))
        value = float(value)
        return value

class SensorRainHeight:

    def __init__(self, exists):
        self.__exists = exists

    def sendData(self):
        value = (random()*50)
        value = str(round(value, 2))
        value = float(value)
        return value