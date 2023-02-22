from microbit import *
import random
import radio

def explosion(x, y):
    for z in range(3):
        for brilho in range(9, 2, -1):
            display.set_pixel(x, y, brilho)
            sleep(60)
            
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

    for ledy in range(5):
        for ledx in range(5):
            if mapajogador[ledx][ledy] == 1:
                display.set_pixel(ledx, ledy, 9)
                
    while not button_a.was_pressed() and selection is False:
        if button_b.was_pressed():
            selection = True
display.clear()
    
    
mapainimigo = [[0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0,],
               [0, 0, 0, 0, 0,]]
                   
    
naviosinimigos = 6


# LOOP PRINCIPAL

primeiro_movimento = True
while naviosjogador > 0 and naviosinimigos > 0:
    
    if (player == 1 and primeiro_movimento is True) or primeiro_movimento is False:
        display.scroll("P"+str(player))
        x = 0
        y = 0
        x_dir = 1
        y_dir = 0
        
        # escolheu o tiro
        while True: 
            display.clear()
            for ledy in range(5):
                for ledx in range(5):
                    if mapainimigo[ledx][ledy] == 2:
                        display.set_pixel(led_x, led_y, 3)
                    if enemy_map[led_x][led_y] == 3:
                        display.set_pixel(led_x, led_y, 9)
                        
            for pisca in range(5):
                display.set_pixel(x, y, 9)
                sleep(50)
                display.set_pixel(x, y, 0)
                sleep(50)
                
            if button_a.was_pressed():
                if x_dir == 1:
                    x_dir = 0
                    y_dir = 1
                else:
                    x_dir = 1
                    y_dir = 0
            if button_b.was_pressed():
                break
            
            x += x_dir
            y += y_dir
            if x > 4:
                x = 0
            if y > 4:
                y = 0
        
        for brilho in range(9, 1, -1):
            display.set_pixel(x, y, brilho)
            sleep(50)
                        
        radio.send("FIRE")
        radio.send(str(x))
        radio.send(str(y))
        
        while radio.receive() != "ECHO":
            sleep(10)
        
        sleep(1000)
        
        if radio.receive() == "HIT":
            explosion(x, y)
            display.set_pixel(x, y, 9)
            naviosinimigos -= 1
            mapainimigo[x][y] = 3
        else:
            mapainimigo[x][y] = 2
        
        sleep(1000)
        
    # turno inimigo 
    
    if naviosinimigos > 0:
        if player == 1:
            display.scroll("P2")
        else:
            display.scroll("P1")
            
        display.clear()
        
        
        for ledy in range(5):
                for ledx in range(5):
                    if player_map[led_x][led_y] == 1.:
                        display.set_pixel(led_x, led_y, 9)
                    if player_map[led_x][led_y] == 2:
                        display.set_pixel(led_x, led_y, 3)
                        
        
        while radio.receive() != "FIRE":
            sleep(10)
        
        sleep(1000)
        x = -1
        while x < 0:
            mensagem = radio.receive()
            for i in range(5):
                if mensagem == str(i):
                    x = i
        y = -1
        while y < 0:
            mensagem = radio.receive()
            for i in range(5):
                if mensagem == str(i):
                    y = i
        
        for brilho in range(9, 1, -1):
            display.set_pixel(x, y, brilho)
            sleep(50)
            
        radio.send("ECHO")
        
        if mapajogador[x][y] == 1:
            radio.send("HIT")
            explosion(x,y)
            naviosjogador -= 1
        else: 
            radio.send("MISS")
        
        mapajogador[x][y] = 2
        sleep(1000)
        
    primeiro_movimento = False
    

if naviosjogador > 0:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
    
    
