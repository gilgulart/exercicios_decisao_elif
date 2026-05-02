from jogos.characters.rpg_boss import *
from jogos.characters.rpg_game_person import *
from jogos.items.rpg_equipament import *
from jogos.systems.getChoice import getChoice
import random
import time
import math
from jogos.arts.ascii_arts import gameOver
from jogos.falas.escolherHistoria import historia


def dado(minimo, maximo):
    # efeito de contagem
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")
    # efeito de números mudando
    for _ in range(10):
        n = random.randint(minimo, maximo)
        print(f"\rNúmero: {n}", end="", flush=True)
        time.sleep(0.1)

    # resultado final
    resultado = random.randint(minimo, maximo)
    print(f"\rResultado final: {resultado}     ")

    return resultado

def calcularDano(atacante, defensor):
    rolagem = dado(1, 20)
    print(f"Dado rolado: {rolagem}")

    danoBase = atacante.dano - 100 / (100 - defensor.resistencia)

    if danoBase < 0:
        danoBase = 0

    if rolagem <= 5:
        print(f"{atacante.nome} errou o ataque!")
        return 0
    elif rolagem <= 14:
        return int(danoBase * 1.4)
    elif rolagem <= 17:
        return int(danoBase * 1.6)
    elif rolagem <= 19:
        return int(danoBase * 1.8)
    else:
        return int(danoBase * 2.2)


def turnoJogador(player: Person, boss: Boss, item: Item = None):
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
        print("Você fugiu do combate!")
        player.hp = 0 

def turnoBoss(player: Person, boss: Boss):
    boss.informacoesBoss()
    if boss.vida > 0:
        danoBoss = calcularDano(boss, player)
        danoBoss = math.ceil(danoBoss)
        player.hp -= danoBoss
        print(f"{boss.nome} causou {danoBoss} de dano em você!")

def combate(player: Person, boss: Boss):
    while player.hp > 0 and boss.vida > 0:
        turnoBoss(player, boss)
        if player.hp > 0:
            turnoJogador(player, boss)
    if player.hp <= 0:
        gameOver()
        exit()
    elif boss.vida <= 0:
        if boss == gilbertoPombo:
            historia.PosSegundaLuta(player)
            boss.derrotado = True
            player.experienciaAtual += boss.valorExperiencia
            player.atualizar()
        else:       
            print(f"Parabéns! Você derrotou {boss.nome} e ganhou {boss.valorExperiencia} de experiência!\n {boss.loot.nomeItem} adicionado à mochila.")
            boss.derrotado = True
            player.experienciaAtual += boss.valorExperiencia
            player.atualizar()
            
