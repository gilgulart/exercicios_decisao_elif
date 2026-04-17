from getChoice import getChoice
from introHistory import introHistory
from history import history, toFight

  
introHistory()
choice = getChoice()


if choice == 1:
  history("AK-47","dragão")
  getChoice()
  
  if choice == 1:
    # luta
    toFight()
  # elif choice == 2:
  #   # fuga
  # else:
  #   # oferecer comida  
