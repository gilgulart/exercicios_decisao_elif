from jogos.arts.ascii_arts import title
from jogos.systems.getChoice import getChoice, choiceMap
from jogos.systems.map import showMap
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_boss import bossesFaceis, bossesMedios, bossesDificeis, bossesLendarios
from jogos.characters.rpg_game_person import Person
from jogos.systems.rpg_combat import combate

from colorama import Fore, init
import pyfiglet
import os
import time
import random



init()


def main():
    
    title()
    
    type_text(Fore.WHITE + """
    O mundo de Eldoria é feito para os heróis corajosos,
    escolha o herói que te representa:""")

    player = Person()
    player.mostrar()
    time.sleep(2.5)
    transition(.2)
    
    if player.genero == "Masculino":
        type_text("""
    Era uma vez um menino que nasceu na região mais bela e majestosa do mundo de Eldoria,
    chamada Planície Dourada. Ele era conhecido como uma pessoa corajosa e bastante alegre.""")
        transition(.2)
        
        type_text("""
    Em um certo dia, o céu, que estava claro e ensolarado, ficou escuro e nublado. 
    Foi só então que uma criatura colossal desceu do céu com suas enormes asas,
    trazendo caos e destruição, cuspindo chamas para todos os lados.""")
        transition(.2)
    
        type_text("""
    Assim que as pessoas o avistam, já o reconhecem das lendas: seu nome é Gilberto, o Pombo.""")
        transition(.2)
        
        type_text("""
    Diante desse caos, e sabendo que alguém precisava detê-lo antes que
    destruísse toda a Planície Dourada,
    o menino pegou seus equipamentos e desafiou a fera para um combate.""")
        transition(.2)

    else:
        type_text("""
    Era uma vez uma menina que nasceu na região mais bela e majestosa do mundo de Eldoria,
    chamada Planície Dourada. Ela era conhecida como uma pessoa corajosa e bastante alegre.""")
        transition(.2)
    
        type_text("""
    Em um certo dia, o céu, que estava claro e ensolarado, ficou escuro e nublado. 
    Foi só então que uma criatura colossal desceu do céu com suas enormes asas,
    trazendo caos e destruição, cuspindo chamas para todos os lados.""")
        transition(.2)

        type_text("""
    Assim que as pessoas o avistam, já o reconhecem das lendas: seu nome é Gilberto, o Pombo.""")
        transition(.2)

        type_text("""
    Diante desse caos, e sabendo que alguém precisava detê-lo antes que
    destruísse toda a Planície Dourada,
    a menina pegou seus equipamentos e desafiou a fera para um combate.""")
        transition(.2)
        
        
    boss = random.choice(bossesFaceis)
    combate(player, boss)
        
    
    showMap()
    choice = choiceMap()
    
    if choice == 1:
      boss = random.choice(bossesFaceis)
      
      type_text("""
Outrora viva com o canto dos pássaros e o sussurro das folhas, a Floresta Antiga guardava paz sob suas copas imensas.
Agora, entre raízes retorcidas e sombras profundas, algo observa em silêncio...""")
      #fácil
      combate(player, boss)
    
    elif choice == 2:
        boss = random.choice(bossesFaceis)
        
        type_text(""" 
As águas escuras do Pântano Arcano já refletiram estrelas e lua cheia.
Hoje apenas névoas inquietas dançam sobre a lama, escondendo segredos que não deveriam ser despertados...""")
        #fácil
        combate(player, boss)

    elif choice == 3:
        boss = random.choice(bossesMedios)
        
        type_text("""
As Montanhas Geladas se erguem como gigantes de pedra e gelo, desafiando qualquer viajante a provar seu valor.
Cada passo é uma conquista, cada rajada de vento uma prova — apenas os mais determinados ousam continuar a escalada.""")
        #médio
        combate(player, boss)

    elif choice == 4:
        boss = random.choice(bossesDificeis)
        
        type_text("""
Nas Terras Vulcânicas, o próprio chão parece rejeitar aqueles que ousam atravessá-lo.
Rios de lava cortam o caminho, o ar queima nos pulmões e o horizonte é tomado por fogo e cinzas
como se o mundo gritasse que ali não há vitória possível.""")

        combate(player, boss)
        
    


if __name__ == "__main__":
    main()
    