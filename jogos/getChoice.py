def getChoice():
    while True:
        try:
            choice = int(input("Digite o número da sua escolha: "))
            if choice <= 0 or choice > 3:
                print("Digite um valor válido")
            else:
                return choice
        except:
            print("Digite um valor válido")