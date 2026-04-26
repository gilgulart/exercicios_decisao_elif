from jogos.characters.rpg_game_person import Person
from jogos.characters.rpg_boss import bossesFaceis, bossesMedios, bossesDificeis, bossesLendarios
from jogos.systems.map import showMap_Boss
from jogos.systems.rpg_combat import combate
from jogos.systems.getChoice import choiceMap_Boss
from jogos.utils.transition import transition
from jogos.utils.prompt import type_text
from colorama import Fore
import random
import time
 
COMBATES_PARA_BOSS_FINAL = 10
 
REGIOES = {
    1: {
        "nome": "Floresta Antiga",
        "pool": bossesFaceis,
        "intro": """
Outrora viva com o canto dos pássaros e o sussurro das folhas, a Floresta Antiga
guardava paz sob suas copas imensas.
Agora, entre raízes retorcidas e sombras profundas, algo observa em silêncio...""",
    },
    2: {
        "nome": "Pântano Arcano",
        "pool": bossesFaceis + bossesMedios,
        "intro": """
As águas escuras do Pântano Arcano já refletiram estrelas e lua cheia.
Hoje apenas névoas inquietas dançam sobre a lama,
escondendo segredos que não deveriam ser despertados...""",
    },
    3: {
        "nome": "Montanhas Geladas",
        "pool": bossesMedios + bossesDificeis,
        "intro": """
As Montanhas Geladas se erguem como gigantes de pedra e gelo,
desafiando qualquer viajante a provar seu valor.
Cada passo é uma conquista, cada rajada de vento uma prova —
apenas os mais determinados ousam continuar a escalada.""",
    },
    4: {
        "nome": "Terras Vulcânicas",
        "pool": bossesDificeis + bossesLendarios,
        "intro": """
Nas Terras Vulcânicas, o próprio chão parece rejeitar aqueles que ousam atravessá-lo.
Rios de lava cortam o caminho, o ar queima nos pulmões e o horizonte é tomado por fogo e cinzas
— como se o mundo gritasse que ali não há vitória possível.""",
    },
}
 
def resetar_boss(boss):
    from jogos.characters.rpg_boss import todosBosses
    for b in todosBosses:
        if b.nome == boss.nome:
            boss.vida = b.vida
            boss.derrotado = False
            break
    return boss
 
def sortear(pool: list):
    boss = random.choice(pool)
    return resetar_boss(boss)
 
def exploration(player: Person, combates: int) -> int:
    while True:
        boss_liberado = combates >= COMBATES_PARA_BOSS_FINAL
        showMap_Boss(boss_liberado)
        choice = choiceMap_Boss(boss_liberado)
 
        if choice == 5:
            type_text(Fore.RED + """
O horizonte racha. Um rugido que faz a terra tremer ecoa por toda Eldoria.
A hora da verdade chegou — o Boss Final aguarda na Região Desconhecida.""" + Fore.RESET)
            transition(.15)
 
            boss = sortear(bossesLendarios)
            combate(player, boss)
            combates += 1
            break
 
        regiao = REGIOES[choice]
        type_text(regiao["intro"])
        transition(.2)
 
        boss = sortear(regiao["pool"])
        combate(player, boss)
        combates += 1
 
        time.sleep(0.8)
 
    return combates