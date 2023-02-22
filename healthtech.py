from microbit import *

quant_agua = 2000
intervalo_agua = 6
intervalo_ativi = 5
intervalo_mensg = 1
atividade_fisica = False
tempo_inicio = 0

while True:
    
    tempo_atual = running_time()
    
    if button_a.is_pressed:
        quant_agua = quant_agua - 200
        
    if button_b.is_pressed:
        display.scroll("Parabens voce completou o exercicio diario! Saude!")
        sleep(6000)
        display.clear()
        atividade_fisica = True
        
    if quant_agua = 0:
        display.scroll("Parabens voce completou a meta de agua diaria")
        sleep(6000)
        display.clear()
        
    tempo_passado = ((((tempo_atual - tempo_inicio) / 1000) / 60) / 60)
    
    if tempo_passado == intervalo_mensg:
        display.scroll("Você está indo bem, continue assim")
        sleep(5000)
        display.clear()
        display.show(Image.HAPPY)
        sleep(2000)
        display.clear()
        intervalo_mensg += 1
        
    if tempo_passado == intervalo_agua:
        if quant_agua > 0:
            display.scroll("BEBA AGUA")
            sleep(5000)
            display.clear()
            intervalo_agua += 6
    
    if tempo_passado == intervalo_ativi:
        if atividade_fisica == False:
            display.scroll("Não esqueca a atividade fisica")
            sleep(5000)
            display.clear()
            intervalo_ativi += 5
            
    if tempo_passado == 24:
        tempo_inicio = running_time()
    

        
    
        
  
    
    
    