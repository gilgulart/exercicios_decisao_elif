import sys
import time
import keyboard
from jogos.utils.transition import transition

skip_pressed = False

# funcao para ler o enter
def skip(event):
    global skip_pressed
    if event.name == "enter":
        skip_pressed = True

keyboard.on_press(skip)

def type_text(text, delay=0.05):
    global skip_pressed
    skip_pressed = False

    for char in text:
        # se o enter for acionado o texto que estiver passando vai ser pulado
        if skip_pressed:    
            transition(0.2)
            delay == 0.0001   
            sys.stdout.write(text)
            sys.stdout.flush()
            time.sleep(delay)
            return       

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print()