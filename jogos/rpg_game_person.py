RESET = "\033[0m"
AMARELO = "\033[33m"
CASTANHO = "\033[38;5;94m"
RUIVO = "\033[38;5;166m"

# cores do corpo por classe
COR_ORC = "\033[32m"        # verde
COR_MAGO = "\033[30m"       # preto
COR_ARQUEIRO = "\033[37m"   # branco


def getChoice():
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: "))
            if choice <= 0 or choice > 3:
                print("Digite um valor válido")
            else:
                return choice
        except ValueError:
            print("Digite um número válido")


def classePersonagem():
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

print(f"""
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