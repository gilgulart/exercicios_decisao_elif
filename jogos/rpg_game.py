from getChoice import getChoice
from introHistory import introHistory
from history import history, toFight
from colorama import Fore, Style, init
import pyfiglet
import os

title = pyfiglet.figlet_format("""
                               Mundo de
                                Eldoria """)
print(title)

init()
  
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
