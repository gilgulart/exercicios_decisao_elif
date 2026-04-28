from jogos.utils.prompt import type_text
from jogos.utils.transition import transition
from jogos.characters.rpg_game_person import Person

class maldicaoFamilia:

    def PosPrimeiraLuta(player: Person):
        dialogosPosPrimeiraLuta = []

        dialogosPosPrimeiraLuta.append(f"""Gilberto amaldiçoa toda a família {player.do} jovem, decretando que todos morrerão dentro de um ano""")

        dialogosPosPrimeiraLuta.append(f"""Sem saber o que fazer, {player.nome} se vê {player.consumido} pelo desespero. Sua família está condenada,
                                        e o tempo está correndo.""")
        
        dialogosPosPrimeiraLuta.append(f"""{player.eleMaisculo} pensa em aceitar o destino… mas a ideia de perder todos que ama é insuportável.
                                        Ainda assim, as palavras de Gilberto não saem de sua cabeça: nenhum remédio no mundo poderia salvá-los.""")
        
        dialogosPosPrimeiraLuta.append(f"""Os dias passam, e {player.o} {player.menino} vaga sem rumo, {player.tomado} pela angústia e pela incerteza.""")
        
        dialogosPosPrimeiraLuta.append(f"""Até que, inesperadamente, surge um senhor muito velho, de aparência misteriosa, que diz:""")
        
        dialogosPosPrimeiraLuta.append(f"""— “{player.meuMaiusculo} jovem, vejo que você carrega um grande peso… Talvez eu tenha a resposta que procura.
                                        Existe um artefato lendário conhecido como Elixir da Vida, capaz de curar qualquer maldição. No entanto,
                                        ele está escondido na caverna de Gilberto, o Pombo. Se quiser tentar salvá-los, eu posso lhe dar um mapa…
                                        mas prepare-se, pois você precisará ficar mais forte antes de enfrentar tal criatura.”""")
        
        dialogosPosPrimeiraLuta.append(f"""Assim que termina, o velho desaparece como em um passe de mágica.""")
        
        dialogosPosPrimeiraLuta.append(f"""Agora, com esperança renovada, {player.nome} entende que tem apenas uma escolha: lutar contra o destino e 
                                       embarcar em uma longa jornada para salvar sua família.""")

        for i in dialogosPosPrimeiraLuta:
            type_text(i)
            transition(.2)

    def PreSegundaLuta(player: Person):
        dialogosPreSegundaLuta = []

        dialogosPreSegundaLuta.append(f"""Depois de uma longa jornada, enfrentando criaturas perigosas e superando desafios em todos os cantos de Eldoria,
                                        o(a) jovem finalmente chega às regiões mais profundas do mundo.""")

        dialogosPreSegundaLuta.append(f"""Cada passo até aqui foi movido por um único objetivo: salvar sua família.""")
        
        dialogosPreSegundaLuta.append(f"""Para isso, {player.ele} precisa enfrentar o temido Gilberto, o Pombo, e conquistar o lendário Elixir da Vida — a única
                                        esperança de impedir a morte daqueles que ama.""")
        
        dialogosPreSegundaLuta.append(f"""Mas há um problema.""")
        
        dialogosPreSegundaLuta.append(f"""Derrotar a criatura mais temida de toda Eldoria não será nada fácil.""")
        
        dialogosPreSegundaLuta.append(f"""Caminhando pela região mais profunda, o ambiente se torna cada vez mais sombrio. O silêncio pesa, e o perigo é constante.
                                        À frente, surge uma caverna escura — e {player.o} jovem sabe, sem dúvidas, que encontrou o lar de Gilberto.""")
        
        dialogosPreSegundaLuta.append(f"""Respirando fundo, {player.ele} entra.""")
        
        dialogosPreSegundaLuta.append(f"""Lá dentro, encontra uma cena inesperada: Gilberto está calmamente sentado, lendo um livro de filosofia. Atrás dele,
                                        uma gigantesca montanha de ouro e tesouros brilha na escuridão.""")

        dialogosPreSegundaLuta.append(f"""Mas nada disso importa.""")
        
        dialogosPreSegundaLuta.append(f"""O que realmente importa está ali: o Elixir da Vida… a única chance de salvar sua família.""")

        dialogosPreSegundaLuta.append(f"""{player.nome} fecha os punhos, sentindo o peso de tudo o que está em jogo.""")

        dialogosPreSegundaLuta.append(f"""Não é apenas uma batalha.""")

        dialogosPreSegundaLuta.append(f"""É a última esperança.""")

        for i in dialogosPreSegundaLuta:
            type_text(i)
            transition(.2)

    def PosSegundaLuta(player: Person):
        dialogosPosSegundaLuta = []

        dialogosPosSegundaLuta.append(f"""Gilberto cai, derrotado, suas asas se espalhando pelo chão da caverna.""")

        dialogosPosSegundaLuta.append(f"""{player.nome} corre até o Elixir da Vida, mas antes de sair, uma voz fraca o interrompe.""")
        
        dialogosPosSegundaLuta.append(f"""— “Você realmente acredita… que pode salvar todos?”""")
        
        dialogosPosSegundaLuta.append(f"""{player.eleMaisculo} se vira.""")
        
        dialogosPosSegundaLuta.append(f"""— “Eu não acredito. Eu sei.”""")
        
        dialogosPosSegundaLuta.append(f"""— “Salvar… é uma palavra bonita. Mas me diga… você pode protegê-los para sempre?”""")
        
        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} jovem hesita.""")
        
        dialogosPosSegundaLuta.append(f"""— “Não… mas posso tentar.”""")

        dialogosPosSegundaLuta.append(f"""— “Então sua luta não é contra mim…” — diz Gilberto — “é contra o inevitável.”""")
        
        dialogosPosSegundaLuta.append(f"""{player.oMaiusculo} {player.menino} segura o elixir com força.""")

        dialogosPosSegundaLuta.append(f"""— “Não. Minha luta é por cada momento que ainda posso ter com eles.”""")

        dialogosPosSegundaLuta.append(f"""Silêncio toma conta da caverna.""")

        dialogosPosSegundaLuta.append(f"""Gilberto observa por um instante, como se analisasse aquela resposta.""")

        dialogosPosSegundaLuta.append(f"""— “Então vá… e valorize cada segundo. Porque nem mesmo o elixir pode parar o tempo.”""")

        dialogosPosSegundaLuta.append(f"""{player.nome} não responde.""")

        dialogosPosSegundaLuta.append(f"""Apenas parte.""")                

        dialogosPosSegundaLuta.append(f"""Ao chegar em casa, usa o elixir e salva sua família.""")   

        dialogosPosSegundaLuta.append(f"""Mas agora {player.nome} sabe…""")   

        dialogosPosSegundaLuta.append(f"""Que o verdadeiro valor não está em evitar a perda — mas em amar enquanto ainda há tempo.""")   


        for i in dialogosPosSegundaLuta:
            type_text(i)
            transition(.2)

    

        