a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Os lados formam um triângulo")
else:
    print("Os lados não formam um triângulo!")
    exit()

if a == b == c:
    print("O triângulo é um triângulo Equilátero")
elif a == b or b == c or c == a:
    print("O triângulo é um triângulo Isósceles")
else:
    print("o triângulo é um triângulo Escaleno")