sal = float(input("Qual é o seu salário atual: "))

if sal > 0:
    if sal <= 280.00:
        percentual = 20
    elif sal <= 700.00:
        percentual = 15
    elif sal <= 1500.00:
        percentual = 10
    else:
        percentual = 5
    
    aumento = (sal * (percentual / 100))
    nsal = sal + aumento

    print(f"Seu salário antes do reajuste era: R${sal:.2f}")
    print(f"O percentual de aumento foi {percentual}%")
    print(f"O valor do aumento foi: R${aumento:.2f}")
    print(f"Seu novo salário após o aumento é: R${nsal:.2f}")
            
else:
    print("Digite um valor válido")
