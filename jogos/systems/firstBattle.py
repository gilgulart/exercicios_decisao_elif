from jogos.characters.rpg_boss import *
from jogos.characters.rpg_game_person import *
from jogos.items.rpg_equipament import *
from jogos.systems.getChoice import getChoice
from jogos.systems.rpg_combat import calcularDano, turnoBoss
from jogos.falas.escolherHistoria import historia
from jogos.arts.ascii_arts import gameOver

def turnoJogadorPrimeiraBatalha(player: Person, boss: Boss, item: Item = None):
    if player.itemAtual:
        player.itemAtual.efeitoPorTurno(player)
    else:
        pass
    print(f"""
        ================================================================================  
          Seu HP: {player.hp} 
          ATK: {player.dano} 
          DEF: {player.resistencia}
        ================================================================================ 
""")
        
    print("""
    1- Atacar
    2- Trocar item
    3- Fugir""")
    
    choice = getChoice()
    
    if choice == 1:
        danoJogador = calcularDano(player, boss)
        danoJogador = math.ceil(danoJogador)
        boss.vida -= danoJogador
        print(f"Você causou {danoJogador} de dano em {boss.nome}!")

    elif choice == 2:
        player.mochilaItens()
        player.escolherItem()
        
    elif choice == 3:
        gameOver()
        exit()

def primeiroCombate(player: Person, boss: Boss):
    while player.hp > 0 and boss.vida > 0:
        turnoBoss(player, boss)
        if player.hp > 0:
            turnoJogadorPrimeiraBatalha(player, boss)
    if player.hp <= 0:
        if player.classe == "Orc":
                player.hp = 150
        elif player.classe == "Mago":
                player.hp = 80
        elif player.classe == "Arqueiro":
                player.hp = 100
        historia.PosPrimeiraLuta(player)
    elif boss.vida <= 0:
        print(f"Parabéns! Você derrotou {boss.nome} e ganhou {boss.valorExperiencia} de experiência!\n {boss.loot.nomeItem} adicionado à mochila.")
        boss.derrotado = True
        player.experienciaAtual += boss.valorExperiencia
        player.atualizar()
        
