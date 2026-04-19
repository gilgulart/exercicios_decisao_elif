from jogos.arts.ascii_arts import title
from jogos.systems.getChoice import getChoice
from jogos.systems.map import showMap, choiceMap
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.story.introHistory import introHistory
from jogos.story.history import history, toFight
from jogos.characters.rpg_game_person import Person

from colorama import Fore, init
import pyfiglet
import os


init()
def main():
    
    title()
    
    type_text(Fore.WHITE + """
O mundo de Eldoria é feito para os heróis corajosos,
    escolha o herói que te representa:
          """)

    player = Person()
    player.mostrar()


    # os.system("cls")

    # player = createPerson()  


if __name__ == "__main__":
    main()