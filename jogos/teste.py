import os
import time

RESET = "\033[0m"
AMARELO = "\033[33m"

frames = [
f"""
   {AMARELO}/////////{RESET}
  |👁️   👁️|
  |   ^   |
  |  ---  |
   \\_____/
    / | \\
   /  |  \\
     / \\
    /   \\
""",
f"""
   {AMARELO}/////////{RESET}
  |👁️   👁️|
  |   -   |
  |  ---  |
   \\_____/
    / | \\
   /  |  \\
     / \\
    /   \\
"""
]

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    for frame in frames:
        limpar()
        print(frame)
        time.sleep(0.4)


print("pedro esteve aqui novamente")