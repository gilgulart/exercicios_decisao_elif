from jogos.systems.getChoice import getChoice
from jogos.story.introHistory import introHistory
from jogos.story.history import history, toFight
from jogos.characters.rpg_game_person import createPerson
from colorama import Fore, init
import pyfiglet
import os

init()

title = Fore.GREEN + pyfiglet.figlet_format("""Mundo de Eldoria """)
print(title)

player = createPerson()
  
introHistory()
choice = getChoice()
os.system("cls")


if choice == 1:
  history("AK-47","dragão")
  getChoice()
  os.system("cls")
  
  if choice == 1:
    # luta
    toFight()
  # elif choice == 2:
  #   # fuga
  # else:
  #   # oferecer comida  
