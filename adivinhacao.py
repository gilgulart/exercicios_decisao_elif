import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sort = random.choice(numbers)

while True:
    first_player = int(input("Jogador 1: "))
    second_player = int(input("Jogador 2: "))
    third_player = int(input("Jogador 3: "))

    if first_player == sort or second_player == sort or third_player == sort:
        print(f"A escolha do computador foi {sort}, você acertou!")
        if first_player == sort:
            first_player = "Jogador 1"
            print(f"O {first_player} foi o vencedor!")
            break
        elif second_player == sort:
            second_player = "Jogador 2"
            print(f"O {second_player} foi o vencedor!")
            break
        else:
            third_player = "Jogador 3"
            print(f"O {third_player} foi o vencedor!")
            break
    else:
        print("Tente novamente um numero entre 1 e 10")