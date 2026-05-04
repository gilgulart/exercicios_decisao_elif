from jogos.characters.rpg_game_person import Person
from jogos.characters.rpg_boss import bossesFaceis, bossesMedios, bossesDificeis, bossesLendarios, gilbertoPombo, todosBosses
from jogos.systems.map import showMap_Boss
from jogos.systems.rpg_combat import combate
from jogos.systems.getChoice import choiceMap_Boss
from jogos.utils.transition import transition
from jogos.utils.prompt import type_text
from colorama import Fore
from jogos.falas.escolherHistoria import historia
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
 
def sortear(pool: list):
    disponiveis = [b for b in pool if not b.derrotado]

    if not disponiveis:
        return None

    return random.choice(disponiveis)
 
def exploration(player: Person) -> int:
    combates = 0
    while any(not b.derrotado for b in todosBosses):
            boss_liberado = combates >= COMBATES_PARA_BOSS_FINAL
            showMap_Boss(boss_liberado)
            choice = choiceMap_Boss(boss_liberado)
    
            if choice == 5:
                if gilbertoPombo.derrotado:
                    type_text("Você já derrotou o Boss Final.")
                    continue
                type_text(Fore.RED + """
    O horizonte racha. Um rugido que faz a terra tremer ecoa por toda Eldoria.
    A hora da verdade chegou — o Boss Final aguarda na Região Desconhecida.""" + Fore.RESET)
                transition(.15)
    
                boss = gilbertoPombo
                historia.PreSegundaLuta(player)
                combate(player, boss)
                combates += 1
                continue

            regiao = REGIOES[choice]
            boss = sortear(regiao["pool"])

            if boss is None:
                 type_text("Você já derrotou todos os bosses dessa região")
                 transition(.2)
                 continue
            
            type_text(regiao["intro"])
            transition(.2)
            combate(player, boss)
            combates+=1

    type_text("Parabéns, você derrotou todos os monstros de Eldoria, o reino agora está livre de todo o mal, muito obrigado")

    return combates