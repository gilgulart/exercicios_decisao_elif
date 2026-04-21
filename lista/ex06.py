nota1 = float(input("Digite a sua nota: "))
nota2 = float(input("Digite a sua nota: "))

average = (nota1 + nota2) / 2

def showResult(n1: float, n2: float, m: float, c: str, msg: str):
    print(f"""
----------------- BOLETIM -----------------
    Nota 1: {n1}            Nota 2: {n2}
    Média: {m}              conceito: {c}
                {msg}""")

if average >= 9.00 and average <= 10.00:
    showResult(nota1, nota2, average, 'A', "APROVADO")

elif average >= 7.5:
    showResult(nota1, nota2, average, 'B', "APROVADO")
elif average >= 6.00:
    showResult(nota1, nota2, average, 'C', "APROVADO")
elif average >= 4.00:
    showResult(nota1, nota2, average, 'D', "REPROVADO")
elif average < 4:
    showResult(nota1, nota2, average, 'E', "REPROVADO")
    
