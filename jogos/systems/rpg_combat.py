from jogos.characters.rpg_boss import *
from jogos.characters.rpg_game_person import *
from jogos.items.rpg_equipament import *
from jogos.systems.getChoice import getChoice
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.arts.ascii_arts import gameOver

import random
import time


def combat(player: Person, boss: Boss):
    type_text(f"{boss.introducao}")
    type_text(f"Prepare-se para enfrentar: {boss.nome}")
    
   
    # LOOP DO COMBATE
    
    while player.hp > 0 and boss.vida > 0:
        boss.hpBoss()
        print(f"Seu HP: {player.hp} | ATK: {player.dano} | DEF: {player.resistencia}\n")
        
        print("""
        1- Atacar
        2- Usar item
        3- Fugir""")
        
        choice = None
        
        if choice == 1:
            # calcular dano do jogador no Boss
            pass
            
        elif choice == 2:
            player.mochilaItens()
            player.escolherItem()
            
        elif choice == 3:
          #Lógica fuga
            pass
        
        #Turno do boss
        if boss.vida > 0:
            #calcular dano do boss
            pass
        
    if boss.vida <= 0:
        # marcar boss.derrotado = True
        # dar experiência ao jogador: player.experienciaAtual += boss.valorExperiencia
        # chamar player.atualizar() para verificar level up
        # mostrar loot do boss
        pass

    elif player.hp <= 0:
        gameOver()
        time.sleep(3)
        exit()
        