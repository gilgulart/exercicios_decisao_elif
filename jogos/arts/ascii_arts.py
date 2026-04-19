import pyfiglet
from colorama import Fore, init

init()

# print(pyfiglet.FigletFont.getFonts())
def title():
    title = pyfiglet.figlet_format("MUNDO DE ELDORIA", font="epic")
    print(Fore.YELLOW + title)
    