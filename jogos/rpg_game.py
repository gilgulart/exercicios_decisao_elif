from getChoice import getChoice
from introHistory import introHistory
from history import history, toFight
from colorama import Fore, Style, init
from rpg_game_person import createPerson
import pyfiglet
import os

init()

title = pyfiglet.figlet_format("""Mundo de Eldoria """)
print(title)

createPerson()
  
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
