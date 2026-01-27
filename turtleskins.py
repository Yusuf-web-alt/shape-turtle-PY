from turtle import *
import time

googoo = ["arrowd", "classic", "turtle", "circle", "square"]

def front():
    left(360 / 4)

def back():
    right(360 / 4)

def setup():
    hideturtle()
    penup()
    fd(-221)
    front()

setup()

for shapetester in googoo:
    shape(shapetester)
    stamp()
    back()
    fd(100)
    front()