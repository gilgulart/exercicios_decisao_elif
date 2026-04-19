from jogos.systems.getChoice import getChoice
from colorama import Fore, init

init()

def showMap():
    
       print("""
Este é o mundo mágico de Eldoria, escolha o seu caminho com sabedoria...
             
╔════════════════════ MAPA DO MUNDO: ELDORIA ═══════════════════╗

                     🌾 PLANÍCIES DOURADAS
                               │
                               │
                     🌲 floresta antiga
                               │
                               │
     🧙 Pântano Arcano ───── Estrada dos Reinos ─────  🏔 Montanhas Geladas
                               │
                               │
                         🌋 Terras Vulcânicas
                               │
                               │
                         ☠ Região Desconhecida

╚═══════════════════════════════════════════════════════════════╝
""")




def choiceMap():
    print(Fore.YELLOW + """
╔════════════════════ MAPA DO MUNDO: ELDORIA ═══════════════════╗

                     🌾 PLANÍCIES DOURADAS
                               │
                               │
                (1) 🌲 floresta antiga
                               │
                               │
(2) 🧙 Pântano Arcano ───── Estrada dos Reinos ───── (3) 🏔 Montanhas Geladas
                               │
                               │
                        (4) 🌋 Terras Vulcânicas
                               │
                               │
                         ☠ Região Desconhecida


Escolha para onde viajar:

1 - Planícies Douradas
2 - Pântano Arcano
3 - Montanhas Geladas
4 - Terras Vulcânicas

0 - Sair do jogo

╚═══════════════════════════════════════════════════════════════╝
""")


if choice == 1:
    print("história Planícies douradas + combate")
    
elif choice == 2:
    print("história Pântano Arcano + combate")

elif choice == 3:
    print("história Montanhas Geladas + combate")

elif choice == 4:
    print("história Terras Vulcânicas + combate")

elif choice == 0:
    exit()