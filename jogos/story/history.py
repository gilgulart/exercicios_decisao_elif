import random
from jogos.systems.prompt import type_text


def history(weapon, enemy):
    print(f"""
            Você encontra um {enemy}!
            suas pernas tremem na presença desta criatura mítica
            e agora restam poucas opções:
        ---------------------------------------------------------------
            1. Lutar com sua {weapon}
            2. Tentar fugir
            3. Oferecer comida ao {enemy}
          """)
    
def toFight(weapon, enemy):
    print(f"""
            Num ato de bravura e heroísmo, você alcança a sua {weapon}
            e parte para cima do {enemy} furioso!
            É hora de testar sua sorte, qual será o seu destino?
        ---------------------------------------------------------------
            
          """)
    
    # se o ataque for ...: ex. acerta o braço do inimigo
    # lógica da luta
    
def toEscape():
    print(f""" 
            # texto fuga 
          """)
    
def beFriendly():
    print(""" 
          # texto opção amigável
          """)