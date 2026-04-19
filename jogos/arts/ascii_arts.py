import pyfiglet
import time
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from colorama import Fore, init

init()

def title():
    title = pyfiglet.figlet_format("MUNDO DE ELDORIA", font="epic")
    print(Fore.YELLOW + title)
    type_text("Atravesse os reinos, enfrente as sombras, conquiste a vida")
    
    time.sleep(2)
    transition()