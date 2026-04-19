from jogos.systems.getChoice import getChoice
from jogos.systems.map import showMap, choiceMap
from jogos.story.introHistory import introHistory
from jogos.story.history import history, toFight
from jogos.characters.rpg_game_person import createPerson

from colorama import Fore, init
import pyfiglet
import os


init()

player = createPerson()  
