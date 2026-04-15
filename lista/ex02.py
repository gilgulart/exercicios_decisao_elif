num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

if num1 < maior and num1 > menor:
    print(f"{maior}, {num1}, {menor}")

if num2 < maior and num2 > menor:
    print(f"{maior}, {num2}, {menor}")

if num3 < maior and num3 > menor:
    print(f"{maior}, {num3}, {menor}")


print(f"Os números em ordem decrescentes é {ord}")