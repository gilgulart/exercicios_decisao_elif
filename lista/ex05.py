print("Os dias da semana correspodente (1-Domingo, 2- Segunda, etc.) ")
day_name = input("Digite o dia da semana: ").strip()

if day_name in ("1", "2", "3", "4", "5", "6", "7"):
    if day_name in ("1"):
        print("Hoje é Domingo!")
    if day_name in ("2"):
        print("Hoje é Segunda-feira!")
    if day_name in ("3"):
        print("Hoje é Terça-feira!")
    if day_name in ("4"):
        print("Hoje é Quarta-feira!")
    if day_name in ("5"):
        print("Hoje é Quinta-feira!")
    if day_name in ("6"):
        print("Hoje é Sexta-feira!")
    if day_name in ("7"):
        print("Hoje é Sábado!")
else:
    print("Valor Inválido!")