p1 = float(input("Qual o valor do primeiro produto: "))
p2 = float(input("Qual o valor do segundo produto: "))
p3 = float(input("Qual o valor do terceiro produto: "))

menor = min(p1, p2, p3)

if p1 == p2 == p3:
    print("Todos os produtos têm o mesmo preço. Pode escolher qualquer um!")
elif p1 == menor and p2 == menor:
    print("Você pode escolher entre o primeiro e o segundo produto!")
elif p1 == menor and p3 == menor:
    print("Você pode escolher entre o primeiro e o terceiro produto!")
elif p2 == menor and p3 == menor:
    print("Você pode escolher entre o segundo e o terceiro produto!")
elif p1 == menor:
    print("Você deveria comprar o primeiro produto!")
elif p2 == menor:
    print("Você deveria comprar o segundo produto!")
else:
    print("Você deveria comprar o terceiro produto!")