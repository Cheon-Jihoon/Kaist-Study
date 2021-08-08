from cs1robots import *

# create_world()
load_world(r'C:\Users\c_zho\Desktop\wolrds\harvest3.wld')

hubo = Robot()
hubo.set_trace("blue")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def pick_beeper():
    if hubo.on_beeper():
        hubo.pick_beeper()


hubo.move()
pick_beeper()

for i in range(2):
    for i in range(5):
        hubo.move()
        pick_beeper()

    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    pick_beeper()

    for i in range(5):
        hubo.move()
        pick_beeper()

    turn_right()
    hubo.move()
    turn_right()
    pick_beeper()

for i in range(5):
    hubo.move()
    pick_beeper()

hubo.turn_left()
hubo.move()
hubo.turn_left()
pick_beeper()

for i in range(5):
    hubo.move()
    pick_beeper()