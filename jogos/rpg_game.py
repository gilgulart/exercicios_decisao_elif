from getChoice import getChoice
from introHistory import introHistory
  
choice = getChoice()
  
  
if choice == 1:
      print("""
            
            
            Você encontra um Lobo gigante!
            suas pernas tremem na presença desta criatura mítica
            e agora restam poucas opções:
        ---------------------------------------------------------------
            1. Lutar com sua espada
            2. Tentar fugir
            3. Oferecer comida ao lobo
            """)
      getChoice()
  
introHistory()
mainHistory()