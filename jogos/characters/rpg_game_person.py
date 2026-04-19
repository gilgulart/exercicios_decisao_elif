from jogos.systems.getChoice import getChoice
from colorama import Fore, Style, init

init()

RESET = Style.RESET_ALL
AMARELO = Fore.YELLOW
CASTANHO = Fore.LIGHTBLACK_EX
RUIVO = Fore.RED

# cores do corpo por classe
COR_ORC = Fore.GREEN      # verde
COR_MAGO = Fore.BLACK       # preto
COR_ARQUEIRO = Fore.WHITE   # branco

def createPerson():
    def classePersonagem():
        print("""
        Escolha o seu Herói, você guiará este guerreiro nesta jornada épica
        ---------------------------------------------------------------
        """)
        
        print("""
            Classe do personagem: 
            1 - Orc 
            2 - Mago sombrio
            3 - Arqueiro da luz 
        ---------------------------------------------------------------
        """)
        choiceClass = getChoice()

        if choiceClass == 1:
            return "Orc", 150, 20, 15, COR_ORC
        elif choiceClass == 2:
            return "Mago", 80, 30, 5, COR_MAGO
        else:
            return "Arqueiro", 100, 25, 10, COR_ARQUEIRO


    def corOlhos():
        print("""
            Cor dos olhos: 
            1 - Castanhos
            2 - Verdes
            3 - Azuis
        ---------------------------------------------------------------
        """)
        choiceEyes = getChoice()

        if choiceEyes == 1:
            return "👁️"
        elif choiceEyes == 2:
            return "🟢"
        else:
            return "🧿"


    def corCabelo():
        print("""
            Cor do cabelo: 
            1 - Loiro
            2 - Castanho
            3 - Ruivo
        ---------------------------------------------------------------
        """)
        choiceHair = getChoice()

        if choiceHair == 1:
            return AMARELO + "/////////" + RESET
        elif choiceHair == 2:
            return CASTANHO + "/////////" + RESET
        else:
            return RUIVO + "/////////" + RESET


    # ===== EXECUÇÃO =====

    classe, hp, atk, defesa, cor_corpo = classePersonagem()
    cabelo = corCabelo()
    olho = corOlhos()

    
    playerMale = (f"""
    Classe: {classe}
    HP: {hp}
    ATK: {atk}
    DEF: {defesa}

    {cabelo}
    {cor_corpo}  |{olho}   {olho}  |
    {cor_corpo}  |   ^   |
    {cor_corpo}  |  ---  |
    {cor_corpo}   \\_____/
    {cor_corpo}    / | \\
    {cor_corpo}   /  |  \\
    {cor_corpo}     / \\
    {cor_corpo}    /   \\{RESET}
    """)
    
    print(playerMale)