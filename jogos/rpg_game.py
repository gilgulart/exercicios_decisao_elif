def introHistory():
  print("""
          Você é um aventureiro que recebeu uma missão: 
          encontrar um cristal mágico perdido na Floresta de Eldoria.
          Dizem que criaturas estranhas vivem lá dentro.
        ---------------------------------------------------------------""")
def getChoice():
  choice = int(input("Digite o número da sua escolha: "))
  if choice <= 0 or choice > 3:
    print("Digite um valor válido")
  else:
    return choice
  
def mainHistory():   
  print("""
          Você tem três opções para começar sua jornada:
          1. Seguir pela trilha escura.
          2. Seguir pela trilha iluminada pelo sol.
          3. Explorar ao redor da floresta.
        ---------------------------------------------------------------
          """)
  choice = getChoice()
  
  if choice == 1:
      print("""
            Você encontra um Lobo gigante!
            suas pernas tremem na presença desta criatura mítica
            e agora restam poucas opções:
        ---------------------------------------------------------------
            1. Lutar com sua espada
            2. Tentar fugir
            3. Oferecer comida ao lobo
            """)
      getChoice()
      choice = getChoice()

introHistory()
mainHistory()