from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_game_person import Person

class MaldicaoPessoal:

    def PosPrimeiraLuta(self, player):
        dialogosPosPrimeiraLuta = []

        dialogosPosPrimeiraLuta.append(f"""Gilberto lança uma maldição diretamente sobre {player.o} {player.menino}, condenando-{player.o} à morte em até um ano""")

        dialogosPosPrimeiraLuta.append(f"""Sem saber o que fazer, {player.nome} se vê diante de um destino cruel: esperar, dia após dia,
        até que a maldição se cumpra… ou encontrar uma forma de quebrá-la.""")
        
        dialogosPosPrimeiraLuta.append(f"""{player.eleMaisculo} até considera aceitar seu fim, mas algo dentro {player.dele} se recusa a desistir. No entanto,
        as palavras de Gilberto ecoam em sua mente: nenhum remédio no mundo seria capaz de curá-lo(a).""")
        
        dialogosPosPrimeiraLuta.append(f"""Os dias passam, e {player.o} {player.menino} vaga sem rumo, {player.tomado} pela angústia e pela incerteza.""")
        
        dialogosPosPrimeiraLuta.append(f"""Foi então que, do nada, surge um senhor muito velho, de aparência misteriosa, que se aproxima lentamente e diz:""")
        
        dialogosPosPrimeiraLuta.append(f"""— “{player.meuMaiusculo} jovem, vejo que você está enfrentando problemas que parecem não ter solução… mas talvez eu possa ajudá-l{player.o}.
        Ouvi falar de um artefato lendário chamado Elixir da Vida, capaz de curar qualquer mal. Porém, ele só pode ser encontrado na caverna
        de Gilberto, o Pombo. Se decidir tentar a sorte, eu tenho um mapa que pode guiá-l{player.o}… mas recomendo que treine antes de enfrentar a 
        criatura alada.”""")
        
        dialogosPosPrimeiraLuta.append(f"""Assim que termina de falar, o velho desaparece como em um passe de mágica.""")
        
        dialogosPosPrimeiraLuta.append(f"""Agora, com um novo objetivo em mente, {player.o} jovem finalmente enxerga uma chance de sobreviver — e parte em uma longa jornada em 
        busca do elixir.""")

        for i in dialogosPosPrimeiraLuta:
            type_text(i)
            transition(.2)

    def PreSegundaLuta(self, player):
        dialogosPreSegundaLuta = []

        dialogosPreSegundaLuta.append(f"""Depois de uma longa jornada, enfrentando todo tipo de criatura e atravessando os mais diversos biomas de Eldoria,
        {player.o} jovem finalmente alcança as regiões mais profundas do mundo.""")

        dialogosPreSegundaLuta.append(f"""Seu objetivo é claro: enfrentar o grandioso Gilberto, o Pombo, e conquistar o lendário Elixir da Vida — sua única
        chance de escapar da morte que se aproxima a cada dia.""")
        
        dialogosPreSegundaLuta.append(f"""Mas há um problema.""")
        
        dialogosPreSegundaLuta.append(f"""Derrotar a criatura mais temida de toda Eldoria não será nada fácil.""")
        
        dialogosPreSegundaLuta.append(f"""Caminhando pela região mais profunda, o ar se torna pesado, e o silêncio, inquietante. À sua frente, surge uma 
        caverna sombria. Apenas ao olhar, {player.nome} já tem certeza — aquele é o covil de Gilberto.""")
        
        dialogosPreSegundaLuta.append(f"""Sem hesitar, {player.ele} entra.""")
        
        dialogosPreSegundaLuta.append(f"""Lá dentro, uma cena inesperada: Gilberto está tranquilamente sentado, lendo um livro de filosofia, como se nada 
        estivesse acontecendo. Logo atrás dele, uma enorme montanha de ouro e tesouros se ergue.""")
        
        dialogosPreSegundaLuta.append(f"""Mas nada disso importa.""")

        dialogosPreSegundaLuta.append(f"""O que realmente importa está ali: o Elixir da Vida… a única coisa que {player.o} separa da morte.""")
        
        dialogosPreSegundaLuta.append(f"""O coração de {player.nome} dispara.""")

        dialogosPreSegundaLuta.append(f"""Agora, não há mais volta.""")

        dialogosPreSegundaLuta.append(f"""É lutar… ou morrer.""")

        for i in dialogosPreSegundaLuta:
            type_text(i)
            transition(.2)

    def PosSegundaLuta(self, player):
        dialogosPosSegundaLuta = []

        dialogosPosSegundaLuta.append(f"""Gilberto cai.""")

        dialogosPosSegundaLuta.append(f"""O impacto ecoa pela caverna, levantando poeira e silenciando tudo ao redor. {player.oMaiusculo} jovem permanece
        de pé, quase sem forças, sentindo o peso de cada ferimento.""")

        dialogosPosSegundaLuta.append(f"""O Elixir da Vida está logo ali.""")

        dialogosPosSegundaLuta.append(f"""Mas antes que possa pegá-lo, uma voz fraca {player.o} interrompe.""")

        dialogosPosSegundaLuta.append(f"""— “Então… você venceu a morte?”""")

        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} jovem olha para Gilberto, ainda vivo, respirando com dificuldade.""")

        dialogosPosSegundaLuta.append(f"""— “Ainda não. Mas vou.”""")

        dialogosPosSegundaLuta.append(f"""Gilberto solta uma leve risada, cansada.""")

        dialogosPosSegundaLuta.append(f"""— “Curioso… você passou por tudo isso… só para adiar o inevitável.”""")

        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} {player.menino} franze a testa.""")

        dialogosPosSegundaLuta.append(f"""— “Não é sobre adiar. É sobre viver.”""")

        dialogosPosSegundaLuta.append(f"""— “Viver?” — Gilberto repete. — “Você chama isso de viver? Fugir da morte a qualquer custo?”""")

        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} jovem aperta os punhos.""")

        dialogosPosSegundaLuta.append(f"""— “Eu lutei porque não queria morrer sem propósito.”""")

        dialogosPosSegundaLuta.append(f"""Silêncio.""")

        dialogosPosSegundaLuta.append(f"""Gilberto observa, como se estivesse avaliando cada palavra.""")

        dialogosPosSegundaLuta.append(f"""— “E agora você tem um?”""")

        dialogosPosSegundaLuta.append(f"""{player.nome} hesita… mas responde:""")

        dialogosPosSegundaLuta.append(f"""— “Tenho. Eu escolhi lutar.”""")

        dialogosPosSegundaLuta.append(f"""Gilberto fecha os olhos por um instante.""")

        dialogosPosSegundaLuta.append(f"""— “Interessante… a maioria só percebe que quer viver quando está prestes a morrer.”""")

        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} jovem pega o elixir.""")

        dialogosPosSegundaLuta.append(f"""— “Então você fez isso de propósito?”""")

        dialogosPosSegundaLuta.append(f"""— “Não.” — Gilberto responde, com um leve sorriso. — “Mas o medo… costuma revelar quem realmente somos.”""")

        dialogosPosSegundaLuta.append(f"""{player.nome} encara o frasco por um momento.""")

        dialogosPosSegundaLuta.append(f"""— “E o que eu sou?”""")

        dialogosPosSegundaLuta.append(f"""Gilberto respira fundo, já no fim.""")

        dialogosPosSegundaLuta.append(f"""— “Alguém que finalmente entende que viver não é ter tempo infinito… é saber o que fazer com o tempo que tem.”""")

        dialogosPosSegundaLuta.append(f"""Silêncio.""")

        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} jovem bebe o elixir.""")

        dialogosPosSegundaLuta.append(f"""A maldição desaparece.""")

        dialogosPosSegundaLuta.append(f"""Quando {player.ele} olha novamente, Gilberto já não está mais vivo.""")

        dialogosPosSegundaLuta.append(f"""E, pela primeira vez… a vida não parece apenas algo a ser preservado — mas algo a ser vivido de verdade.""")

        for i in dialogosPosSegundaLuta:
            type_text(i)
            transition(.2)

    

        