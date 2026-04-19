from jogos.systems.getChoice import getChoice
from colorama import Fore, Style, init
from jogos.items.rpg_equipament import *
from jogos.characters.rpg_boss import *


init()


RESET = Style.RESET_ALL
AMARELO = Fore.YELLOW
CASTANHO = Fore.LIGHTBLACK_EX
RUIVO = Fore.RED

# cores do corpo por classe
COR_ORC = Fore.GREEN      # verde
COR_MAGO = Fore.BLACK       # preto
COR_ARQUEIRO = Fore.WHITE   # branco


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


class Person:
    def __init__(self):
        self.criar_personagem()

    def criar_personagem(self):
        self.experienciaAtual = 0
        self.nivel = 1
        self.experienciaNecessaria = 20

        # CLASSE
        print(Fore.WHITE + """
        Classe do personagem:
        1 - Orc
        2 - Mago sombrio
        3 - Arqueiro da luz
        """)
        choice = getChoice()

        if choice == 1:
            self.classe = "Orc"
            self.hp = 150
            self.dano = 10
            self.resistencia = 15
            self.cor = COR_ORC

        elif choice == 2:
            self.classe = "Mago"
            self.hp = 80
            self.dano = 15
            self.resistencia = 5
            self.cor = COR_MAGO

        else:
            self.classe = "Arqueiro"
            self.hp = 100
            self.dano = 12
            self.resistencia = 10
            self.cor = COR_ARQUEIRO


        # OLHOS
        print("""
        Cor dos olhos:
        1 - Castanhos
        2 - Verdes
        3 - Azuis
        """)
        choice = getChoice()

        if choice == 1:
            self.olho = "👁️ "
        elif choice == 2:
            self.olho = "🟢"
        else:
            self.olho = "🧿"


        # CABELO
        print("""
        Cor do cabelo:
        1 - Loiro
        2 - Castanho
        3 - Ruivo
        """)
        choice = getChoice()

        if choice == 1:
            self.cabelo = AMARELO + "/////////" + RESET
        elif choice == 2:
            self.cabelo = CASTANHO + "/////////" + RESET
        else:
            self.cabelo = RUIVO + "/////////" + RESET

    def mochilaItens(self):
        self.mochila = [] 
        for i in todosBosses:
            if i.derrotado == True:
                self.mochila.append(i.loot)

    def escolherItem(self):
         if len(self.mochila) == 0:
            return None
         else:
            print("Itens disponíveis na mochila:")
            for index, item in enumerate(self.mochila):
                print(f"{index + 1}. {item.nomeItem}")
            while True:
                    choice = int(input("Digite o número do item que deseja usar: "))
                    if 1 <= choice <= len(self.mochila):
                        self.mochila[choice - 1].mostrarAtributosItem()
                        self.mochila[choice - 1].aplicarEfeito(self)
                        break
                    else:
                        print("Digite um número válido.")

    def atualizar(self):
        while self.experienciaNecessaria <= self.experienciaAtual:
            self.nivel = self.nivel + 1
            self.experienciaNecessaria = (self.experienciaNecessaria*50)/100 + self.experienciaNecessaria
            self.dano = self.dano + (self.nivel*2)*0.1
    
    def mostrar(self):
        print(f"""
    Classe: {self.classe}
    HP: {self.hp}
    ATK: {self.dano}
    DEF: {self.resistencia}
    LVL: {self.nivel}

      {self.cabelo}
    {self.cor}  |{self.olho}  {self.olho} |
    {self.cor}  |   ^   |
    {self.cor}  |  ---  |
    {self.cor}   \\_____/
    {self.cor}    / | \\
    {self.cor}   /  |  \\
    {self.cor}     / \\
    {self.cor}    /   \\{RESET}
    """)

# jogador = Person()