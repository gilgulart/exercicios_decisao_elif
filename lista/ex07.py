print("Digite um número inteiro menor que 1000")
num = input("Digite o número inteiro: ")

if len(num) > 4:
    print("Número Inválido!")
    exit()


if len(num) == 3:
    print(f"Seu número {num} \nPossui {num[0]} centenas, {num[-2]} dezenas e {num[-1]} unidades.")
elif len(num) == 2:
    print(f"Seu número {num} \nPossui {num[0]} dezenas e {num[1]} unidades.")
elif len(num) == 1:
    print(f"Seu número {num} \nPossui {num[0]} unidades.")
    