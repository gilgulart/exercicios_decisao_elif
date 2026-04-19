def getChoice():
        try:
            choice = int(input("Faça a sua escolha: "))
            if choice < 0 or choice > 4:
                print("Digite um valor válido")
            else:
                return choice
        except:
            print("Digite um valor válido")