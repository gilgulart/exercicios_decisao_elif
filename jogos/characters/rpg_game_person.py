from jogos.systems.getChoice import getChoice
from colorama import Fore, Style, init
from jogos.items.rpg_equipament import *
from jogos.characters.rpg_boss import *
import shutil
from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
import math

WIDTH = shutil.get_terminal_size().columns


init()


RESET = Style.RESET_ALL
AMARELO = Fore.YELLOW
CASTANHO = Fore.LIGHTBLACK_EX
RUIVO = Fore.RED

# cores do corpo por classe
COR_ORC = Fore.GREEN      # verde
COR_MAGO = Fore.BLACK       # preto
COR_ARQUEIRO = Fore.WHITE   # branco


class Person:
    def __init__(self):
        self.criar_personagem()

    def criar_personagem(self):
        self.experienciaAtual = 0
        self.nivel = 1
        self.experienciaNecessaria = 20
        self.itemEquipado = False
        self.itemAtual = None
        
        self.nome = input("\nDigite o nome do seu personagem: ")
        # GÊNERO
        print(Fore.WHITE + """
        Gênero do(a) personagem:
        1 - Masculino
        2 - Feminino
        """)
        choice = getChoice()
        if choice == 1:
            self.genero = "Masculino"
            self.um = "um"
            self.menino = "menino"
            self.eleMaisculo = "Ele"
            self.ele = "ele"
            self.o = "o"
            self.conhecido = "conhecido"
            self.do = "do"
            self.consumido = "consumido"
            self.tomado = "tomado"
            self.meuMaiusculo = "Meu"
            self.oMaiusculo = "O"
            self.dele = "dele"
            self.sozinho = "sozinho"
            self.tomadoMaisculo = "Tomado"
        else:
            self.genero = "Feminino"            
            self.um = "uma"
            self.menino = "menina"
            self.eleMaisculo = "Ela"
            self.o = "a"
            self.conhecido = "conhecida"
            self.do = "da"
            self.consumido = "consumida"
            self.tomado = "tomada"
            self.meuMaiusculo = "Minha"
            self.ele = "ela"
            self.oMaiusculo = "A"
            self.dele = "dela"
            self.sozinho = "sozinha"
            self.tomadoMaisculo = "Tomada"

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
            self.hp = 180
            self.dano = 12
            self.resistencia = 10
            self.cor = COR_ORC

        elif choice == 2:
            self.classe = "Mago"
            self.hp = 100
            self.dano = 18
            self.resistencia = 5
            self.cor = COR_MAGO

        else:
            self.classe = "Arqueiro"
            self.hp = 120
            self.dano = 15
            self.resistencia = 7
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
        
        if self.genero == "Masculino":
            cabelo_base = "/////////"
            
        if self.genero == "Feminino":
            cabelo_base = """@@=====@@"""
        

        if choice == 1:
            self.cabelo = AMARELO + cabelo_base + RESET
        elif choice == 2:
            self.cabelo = CASTANHO + cabelo_base + RESET
        else:
            self.cabelo = RUIVO + cabelo_base + RESET

    def mochilaItens(self):
        self.mochila = [] 
        for i in todosBosses:
            if i.derrotado == True:
                self.mochila.append(i.loot)

    def escolherItem(self):
        if len(self.mochila) == 0:
            print("Sua mochila está vazia.")
            return None

        if self.itemEquipado and self.itemAtual:
            type_text("Item equipado: ")
            self.itemAtual.mostrarAtributosItem()

        print("Itens disponíveis na mochila:")

        for index, item in enumerate(self.mochila):
            print(f"{index + 1}. {item.nomeItem}")

        while True:
            try:
                choice = int(input("Digite o número do item que deseja usar: "))

                if 1 <= choice <= len(self.mochila):
                    
                    item = self.mochila[choice - 1]
                    item.mostrarAtributosItem()

                    type_text("Equipar item?\n 1) Sim\n 2) Não\n 3) Sair")
                    equipar_choice = getChoice()


                    if equipar_choice == 1:
                        if self.itemAtual:
                            self.itemAtual.removerEfeito(self)
                            self.itemAtual.sendoUsado = False

                        self.itemAtual = item
                        self.itemEquipado = True
                        item.sendoUsado = True
                        item.aplicarEfeito(self)

                    elif equipar_choice == 2:
                        return None
                        
                    elif equipar_choice == 3:
                        return None
                    
                    return item
                else:
                    print("Digite um número válido.")

            except ValueError:
                print("Digite apenas números.")
    def atualizar(self):   
        if self.classe == "Orc":
                self.hp = 150
        elif self.classe == "Mago":
                self.hp = 80
        elif self.classe == "Arqueiro":
                self.hp = 100  
        while self.experienciaNecessaria <= self.experienciaAtual:             
            self.nivel = self.nivel + 1
            self.experienciaNecessaria = (self.experienciaNecessaria*50)/100 + self.experienciaNecessaria
            self.dano += math.ceil(math.sqrt(self.nivel))
            self.hp += math.ceil(math.sqrt(self.nivel))
            self.resistencia += math.ceil(math.sqrt(self.nivel))
    
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
