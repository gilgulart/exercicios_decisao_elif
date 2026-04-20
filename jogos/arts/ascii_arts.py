import pyfiglet
import time
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from colorama import Fore, init
import shutil

WIDTH = shutil.get_terminal_size().columns

init()

def title():
    title = pyfiglet.figlet_format("MUNDO DE ELDORIA", font="epic")
    print(Fore.YELLOW + title.center(WIDTH))
    type_text("Atravesse os reinos, enfrente as sombras, conquiste a vida")
    
    time.sleep(2)
    transition(0.2)
    
def gameOver():
    gameOver = pyfiglet.figlet_format("GAME OVER", font="epic")
    print(Fore.RED + gameOver.center(WIDTH))
    type_text("Você morreu.")
    
    