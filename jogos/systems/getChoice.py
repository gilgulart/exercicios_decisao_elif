import shutil

WIDTH = shutil.get_terminal_size().columns

def getChoice():
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: ".center(WIDTH)))
            if choice <= 0 or choice > 3:
                print("Digite um valor válido".center(WIDTH))
            else:
                return choice
        except ValueError:
            print("Digite um número válido".center(WIDTH))
def choiceMap():
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: ".center(WIDTH)))
            if choice < 0 or choice > 4:
                print("Digite um valor válido".center(WIDTH))
            elif choice == 0:
                exit()
            else:
                return choice
        except ValueError:
            print("Digite um número válido".center(WIDTH))
