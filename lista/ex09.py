nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = ((nota1 + nota2 + nota3) / 3)

if nota1 > 10:
    print("Nota 1 é Inválida!!")
    exit()
elif nota2 > 10:
    print("Nota 2 é Inválida!!")
    exit()
elif nota3 > 10:
    print("Nota 3 é Inválida!!")
    exit()
elif media > 10:
    print("Média é Inválida!!")
    exit()

if 0 <= media <= 10:
    if media < 7:
        print(f"A média é: {media}")
        print("O aluno está: Reprovado")
    if 7 <= media <= 9:
        print(f"A média é: {media}")
        print(f"O aluno está: Aprovado")
    if media == 10:
        print(f"A média é: {media}")
        print(f"O aluno está: Aprovado com Distinção")
else:
    print("Valor Inválido!")
    