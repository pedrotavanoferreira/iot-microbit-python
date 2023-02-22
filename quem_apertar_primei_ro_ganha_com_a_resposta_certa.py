from microbit import *
import random

valendo = False
apertouantes = False
pin8.write_digital(0)
pin14.write_digital(0)

while True:
    if button_a.is_pressed():
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        display.clear()
        valendo = False
        apertouantes = False
        tempo = random.randint(1, 6000)
        sleep(tempo)
        if apertouantes is False:
            valendo = True
            if pin1.is_touched() or pin2.is_touched():
                display.show(Image.NO)
                break
            display.show(Image.ARROW_N)
            sleep(1000)
    while pin1.is_touched():
        if valendo is True:
            valendo = False
            pin8.write_digital(1)
            display.show(Image.ARROW_E)
            sleep(1000)
            pin8.write_digital(0)
            display.clear()

    while pin2.is_touched():
        if valendo is True:
            valendo = False
            pin14.write_digital(1)
            display.show(Image.ARROW_W)
            sleep(1000)
            pin14.write_digital(0)
            display.clear()



