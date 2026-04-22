import shutil
from jogos.arts.ascii_arts import gameOver

WIDTH = shutil.get_terminal_size().columns

def getChoice():
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: ".center(WIDTH)))
            if choice <= 0 or choice > 3:
                print("Digite um valor entre 1 e 3".center(WIDTH))
            else:
                return choice
        except ValueError:
            print("Digite um número válido".center(WIDTH))

def choiceMap_Boss(boss_liberado: bool) -> int:
    limite = 5 if boss_liberado else 4
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: ".center(WIDTH)))
            if choice == 0:
                exit()
                gameOver()
            elif choice < 1 or choice > limite:
                print(f"Digite um valor entre 1 e {limite} (ou 0 para sair).".center(WIDTH))
            else:
                return choice
        except ValueError:
            print("Digite um número válido.".center(WIDTH))

