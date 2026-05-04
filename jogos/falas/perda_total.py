from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_game_person import Person

class PerdaTotal:

    def PosPrimeiraLuta(self, player):
        dialogosPosPrimeiraLuta = []

        dialogosPosPrimeiraLuta.append(f"""
        Gilberto elimina sua família, deixando {player.o} {player.nome} {player.sozinho} no mundo, sem lar e sem ninguém para amar.""")

        dialogosPosPrimeiraLuta.append(f"""
        {player.tomadoMaisculo} por ódio e fúria por ser incapaz de proteger aqueles que ama — e ainda mais ódio pela criatura que os 
        matou sem qualquer motivo, mesmo sabendo que sua região e sua família eram pacíficas e jamais fariam mal a ninguém.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        Alguns dias se passam, e {player.o} {player.nome}, {player.consumido} pela raiva, vaga pela antiga região onde vivia… agora completamente 
        dizimada por Gilberto, o Pombo.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        Durante sua caminhada sem rumo, {player.ele}, sem querer, pisa em um pedaço de papel velho e parcialmente queimado. Ao pegá-lo, algo 
        chama sua atenção: trata-se de um mapa de Eldoria, detalhado como nenhum outro, mostrando até mesmo as regiões mais profundas e 
        esquecidas do mundo — incluindo o possível local onde a criatura alada habita.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        Mesmo {player.consumido} pela vingança, {player.o} jovem reconhece uma verdade dura: em seu estado atual, jamais será capaz de derrotar Gilberto.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        A dor se transforma em determinação.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        Se quiser vingar sua família, {player.ele} precisará se tornar mais forte.""")
        
        dialogosPosPrimeiraLuta.append(f"""
        E assim, com o mapa em mãos e um único objetivo em mente, {player.o} jovem inicia sua jornada — não por salvação… mas por vingança.""")

        for i in dialogosPosPrimeiraLuta:
            type_text(i)
            transition(.2)

    def PreSegundaLuta(self, player):
        dialogosPreSegundaLuta = []

        dialogosPreSegundaLuta.append(f"""
        Depois de uma longa jornada, enfrentando criaturas perigosas e superando desafios em todos os cantos de Eldoria, {player.nome} finalmente
        chega às regiões mais profundas do mundo.""")

        dialogosPreSegundaLuta.append(f"""
        Cada passo até aqui foi movido por um único objetivo: VINGANÇA.""")
        
        dialogosPreSegundaLuta.append(f"""
        Caminhando pela região mais profunda, o ar se torna pesado, e o silêncio domina tudo ao redor. À sua frente, surge uma caverna sombria.
        Apenas ao olhar, {player.o} {player.menino} já tem certeza — aquele é o covil de Gilberto.""")
        
        dialogosPreSegundaLuta.append(f"""
        Respirando fundo, {player.ele} entra.""")
        
        dialogosPreSegundaLuta.append(f"""
        Lá dentro, encontra uma cena inesperada: Gilberto está calmamente sentado, lendo um livro de filosofia, como se nada tivesse acontecido.
        Atrás dele, uma gigantesca montanha de ouro e tesouros brilha na escuridão.""")
        
        dialogosPreSegundaLuta.append(f"""
        Mas nada disso importa.""")
        
        dialogosPreSegundaLuta.append(f"""
        Tomad{player.o} pela raiva e pelo desejo de vingança, {player.o} jovem sente o corpo tremer. Em sua mente, existe apenas um objetivo: ver Gilberto
        derrotado, sem vida, pagando por tudo o que fez.""")
        
        dialogosPreSegundaLuta.append(f"""
        Esse é o momento que {player.ele} reviveu em sua mente todas as noites.""")

        dialogosPreSegundaLuta.append(f"""
        A luta de sua vida.""")
        
        dialogosPreSegundaLuta.append(f"""
        Sem mais dúvidas. Sem mais medo.""")

        dialogosPreSegundaLuta.append(f"""
        Apenas ódio… e determinação.""")


        for i in dialogosPreSegundaLuta:
            type_text(i)
            transition(.2)

    def PosSegundaLuta(self, player):
        dialogosPosSegundaLuta = []

        dialogosPosSegundaLuta.append(f"""
        Gilberto está caído.""")

        dialogosPosSegundaLuta.append(f"""
        {player.o} jovem caminha lentamente até ele, com a arma firme
        em mãos. Cada passo ecoa pela caverna como o fim de tudo que foi perdido.""")
        
        dialogosPosSegundaLuta.append(f"""
        Agora… só falta um golpe.""")
        
        dialogosPosSegundaLuta.append(f"""
        — “E então…” — diz Gilberto, com voz fraca — “isso vai te trazer paz?”""")
        
        dialogosPosSegundaLuta.append(f"""
        {player.o} jovem não hesita:""")
        
        dialogosPosSegundaLuta.append(f"""
        — “Vai.”""")
        
        dialogosPosSegundaLuta.append(f"""
        Gilberto observa em silêncio por um instante.""")
        
        dialogosPosSegundaLuta.append(f"""
        — “Tem certeza… ou você só precisa acreditar nisso?”""")

        dialogosPosSegundaLuta.append(f"""
        — “Você matou minha família.” — a voz de {player.nome} falha por um segundo, mas 
        se firma.""")
        
        dialogosPosSegundaLuta.append(f"""
        — “Isso não tem perdão.”""")

        dialogosPosSegundaLuta.append(f"""
        — “Eu sei.” — responde Gilberto, sem resistência.""")

        dialogosPosSegundaLuta.append(f"""
        — “Mas me diga… sua dor começou comigo?”""")

        dialogosPosSegundaLuta.append(f"""
        {player.o} jovem trava.""")

        dialogosPosSegundaLuta.append(f"""
        — “A dor sempre encontra um motivo.” — diz Gilberto.""")

        dialogosPosSegundaLuta.append(f"""
        — “Mas ela não termina quando o motivo desaparece.”""")

        dialogosPosSegundaLuta.append(f"""
        {player.nome} aperta a arma com mais força.""")                

        dialogosPosSegundaLuta.append(f"""
        — “Você é o motivo.”""")   

        dialogosPosSegundaLuta.append(f"""
        Gilberto balança levemente a cabeça.""")   

        dialogosPosSegundaLuta.append(f"""
        — “Não. Eu fui a causa… naquele momento. Mas o que você sente agora… já é seu.”""")   

        dialogosPosSegundaLuta.append(f"""
        Silêncio.""")   

        dialogosPosSegundaLuta.append(f"""
        A lâmina treme levemente.""")   

        dialogosPosSegundaLuta.append(f"""
        — “Se eu te matar… isso acaba.”""")   

        dialogosPosSegundaLuta.append(f"""
        — “Ou começa outra coisa.” — responde Gilberto.""")   

        dialogosPosSegundaLuta.append(f"""
        — “A vingança não encerra histórias… ela as continua.”""")

        dialogosPosSegundaLuta.append(f"""
        {player.o} jovem fica em silêncio.""")   

        dialogosPosSegundaLuta.append(f"""
        O ódio ainda está ali… mas algo mudou.""")   

        dialogosPosSegundaLuta.append(f"""
        — “Então o que você quer que eu faça?” — pergunta, quase em um sussurro.""")   

        dialogosPosSegundaLuta.append(f"""
        Gilberto solta um último suspiro.""")   

        dialogosPosSegundaLuta.append(f"""
        — “Nada. Pela primeira vez… escolha por você. Não por mim… e nem pela dor.”""")   

        dialogosPosSegundaLuta.append(f"""
        Silêncio absoluto.""")  

        dialogosPosSegundaLuta.append(f"""
        A arma ainda está levantada.""")  

        dialogosPosSegundaLuta.append(f"""
        Mas agora… não é mais sobre Gilberto.""")  

        dialogosPosSegundaLuta.append(f"""
        É sobre quem {player.nome} decide se tornar depois de tudo.""")  

        for i in dialogosPosSegundaLuta:
            type_text(i)
            transition(.2)

    

        