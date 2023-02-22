from microbit import *
import random
import radio
radio.on()
radio.config(channel=43)
display.show(Image.ARROW_N)
menssagem = "3"
while not button_a.is_pressed() and mensagem != "1":
    menssagem = radio.receive()
if button_a.was_pressed():
    radio.sand("1")
    player = 1
else:
    player = 2
display.scroll("p"+str(player)+"coloca os barco")
selection = False
while selection is False:
    mapajogador = [[0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,]]

    direcao = random.choice(["H", "V"])
    if direcao == "H":
        navioX = random.randint(0, 2)
        navioY = random.randint(0, 4)
        mapajogador[navioX][navioY] = 1
        mapajogador[navioX + 1][navioY] = 1
        mapajogador[navioX + 2][navioY] = 1
    else:
        navioX = random.randint(0, 2)
        navioY = random.randint(0, 4)
        mapajogador[navioX][navioY] = 1
        mapajogador[navioX][navioY + 1] = 1
        mapajogador[navioX][navioY + 2] = 1

    naviosjogador = 3

    while naviosjogador < 6:
        navioX = random.randint(0,4)
        navioY = random.randint(0,4)
        if mapajogador[navioX][navioY] == 0:
            mapajogador[navioX][navioY] = 1
            naviosjogador += 1

    display.clear()

    for ledy in ragne(5):
        for ledx in range (5):
            if mapajogador[ledx][ledy] == 1:
                display.set_pixel(ledx, ledy, 9)
    while not button_a.was_pressed() and selection is False:
        if button_b.was_pressed():
            selection = True
display.clear()

mapainimigo =     [[0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,],
                   [0, 0, 0, 0, 0,]]


    naviosinimigos = 6

