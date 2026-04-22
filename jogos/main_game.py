from jogos.arts.ascii_arts import title
from jogos.systems.getChoice import getChoice, choiceMap_Boss
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_game_person import Person
from jogos.characters.rpg_boss import bossesFaceis
from jogos.systems.rpg_combat import combate
from jogos.systems.exploration import exploration, resetar_boss
 
from colorama import Fore, init
import random
import time
 



init()



def prologo(player: Person):    
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
        
        
        
def main():
    title()
    
    type_text(Fore.WHITE + """
    O mundo de Eldoria é feito para os heróis corajosos,
    escolha o herói que te representa:""")

    player = Person()
    player.mostrar()
    time.sleep(2.5)
    transition(.2)
    
    prologo(player)
    boss_intro = resetar_boss(random.choice(bossesFaceis))
    combate(player, boss_intro)
    combates = 1
    
    combates = exploration(player, combates)    
        
    


if __name__ == "__main__":
    main()
    