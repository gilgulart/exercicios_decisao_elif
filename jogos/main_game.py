from jogos.arts.ascii_arts import title
from jogos.systems.getChoice import getChoice
from jogos.systems.map import showMap, choiceMap
from jogos.systems.prompt import type_text
from jogos.story.introHistory import introHistory
from jogos.story.history import history, toFight
from jogos.characters.rpg_game_person import createPerson

from colorama import Fore, init
import pyfiglet
import os


init()

title()

type_text("Atravesse os reinos, enfrente as sombras, conquiste a vida")


# os.system("cls")

# player = createPerson()  
