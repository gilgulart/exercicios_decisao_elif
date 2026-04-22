from colorama import Fore, init

init()


def showMap():
    print(Fore.YELLOW + """
╔════════════════════ MAPA DO MUNDO: ELDORIA ═══════════════════╗
 
                     🌾 PLANÍCIES DOURADAS
                               │
                               │
                (1) 🌲 Floresta Antiga
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
 
1 - Floresta Antiga
2 - Pântano Arcano
3 - Montanhas Geladas
4 - Terras Vulcânicas
 
0 - Sair do jogo
 
╚═══════════════════════════════════════════════════════════════╝
""")


def showMap_Boss(boss_liberado: bool):
    opcao5 = (
        Fore.RED + "5 - ☠  Região Desconhecida  [BOSS FINAL DESBLOQUEADO!]" + Fore.YELLOW
        if boss_liberado
        else Fore.LIGHTBLACK_EX + "5 - ☠  Região Desconhecida  [BLOQUEADO]" + Fore.YELLOW
    )
 
    print(Fore.YELLOW + f"""
╔════════════════════ MAPA DO MUNDO: ELDORIA ═══════════════════╗
 
                     🌾 PLANÍCIES DOURADAS
                               │
                               │
                (1) 🌲 Floresta Antiga
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
 
1 - Floresta Antiga
2 - Pântano Arcano
3 - Montanhas Geladas
4 - Terras Vulcânicas
{opcao5}
 
0 - Sair do jogo
 
╚═══════════════════════════════════════════════════════════════╝
""")
    