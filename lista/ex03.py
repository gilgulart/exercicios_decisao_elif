print("""--------Em qual turno você estuda?--------
 M- matutino | V- vespertino | N- noturno """)

enter = input("> ").upper()
shift = ["M", "V", "N"]

if enter in shift:
 if enter == shift[0]:
    print("Bom dia!")
 elif enter == shift[1]:
    print("Boa tarde!")
 elif enter == shift[2]:
    print("Boa Noite!")
else:
    print("Valor inválido!")
