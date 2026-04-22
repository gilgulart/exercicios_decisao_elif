from jogos.characters.rpg_boss import *
from jogos.characters.rpg_game_person import *
from jogos.items.rpg_equipament import *
from jogos.systems.getChoice import getChoice
import random
import time
import math
from jogos.arts.ascii_arts import gameOver


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

    danoBase = atacante.dano - defensor.resistencia

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

def turnoJogador(jogador: Person, boss: Boss):
    print(f"""
        ================================================================================  
          Seu HP: {jogador.hp} 
          ATK: {jogador.dano} 
          DEF: {jogador.resistencia}
        ================================================================================ 
""")
        
    print("""
    1- Atacar
    2- Trocar item
    3- Fugir""")
    
    choice = getChoice()
    
    if choice == 1:
        danoJogador = calcularDano(jogador, boss)
        danoJogador = math.ceil(danoJogador)
        boss.vida -= danoJogador
        print(f"Você causou {danoJogador} de dano em {boss.nome}!")

    elif choice == 2:
        jogador.mochilaItens()
        jogador.escolherItem()
        
    elif choice == 3:
        print("Você fugiu do combate!")
        jogador.hp = 0 

def turnoBoss(jogador: Person, boss: Boss):
    boss.informacoesBoss()
    if boss.vida > 0:
        danoBoss = calcularDano(boss, jogador)
        danoBoss = math.ceil(danoBoss)
        jogador.hp -= danoBoss
        print(f"{boss.nome} causou {danoBoss} de dano em você!")

def combate(jogador: Person, boss: Boss):
    while jogador.hp > 0 and boss.vida > 0:
        turnoBoss(jogador, boss)
        if jogador.hp > 0:
            turnoJogador(jogador, boss)
    if jogador.hp <= 0:
        gameOver()
        exit()
    elif boss.vida <= 0:
        print(f"Parabéns! Você derrotou {boss.nome} e ganhou {boss.valorExperiencia} de experiência!\n {boss.loot.nomeItem} adicionado à mochila.")
        boss.derrotado = True
        jogador.experienciaAtual += boss.valorExperiencia
        jogador.atualizar()
        
