from jogos.arts.ascii_arts import title
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_game_person import Person
from jogos.characters.rpg_boss import gilbertoPombo
from jogos.systems.exploration import exploration
from colorama import Fore, init
from jogos.systems.firstBattle import primeiroCombate
from jogos.falas.escolherHistoria import historia
import time
 
init()

def prologo(player: Person):    
    dialogos = []

    dialogos.append(f"""
    Era uma vez {player.um} {player.menino} chamado {player.nome} que nasceu na região mais bela e majestosa do mundo de Eldoria,
    chamada Planície Dourada. {player.eleMaisculo} era {player.conhecido} como uma pessoa corajosa e bastante alegre.""")

    dialogos.append(f"""
    Em um certo dia, o céu, que estava claro e ensolarado, ficou escuro e nublado. 
    Foi só então que uma criatura colossal desceu do céu com suas enormes asas,
    trazendo caos e destruição, cuspindo chamas para todos os lados.""")
    
    dialogos.append(f"""
    Assim que as pessoas o avistam, já o reconhecem das lendas: seu nome é Gilberto, o Pombo""")

    dialogos.append(f"""Diante desse caos, e sabendo que alguém precisava detê-lo antes que
    destruísse toda a Planície Dourada,
    {player.o} {player.menino} pegou seus equipamentos e desafiou a fera para um combate.""")    
    
    for d in dialogos:
        type_text(d)
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
    transition(.2)
    primeiroCombate(player, gilbertoPombo)
    transition(.2)
    
    combates = 0
    combates = exploration(player)  
    
    


if __name__ == "__main__":
    main()
    