from jogos.items.rpg_equipament import *

class Boss:

    def __init__(self, introducao: str, nome: str, dano: float, vida: float, resistencia: int, dificuldade = int,  derrotado: bool = False, loot = Item): 
        self.introducao = introducao
        self.nome = nome
        self.dano = dano
        self.vida = vida
        self.resistencia = resistencia
        self.derrotado = derrotado
        self.dificuldade = dificuldade
        self.loot = loot
        

    def hpBoss(self):
        print(f"{self.nome} - Hp: ", end="")
        for i in range(int(self.vida)):
            print("|", end="")
        print("\n")

# DIFICULDADE 1 (FÁCIL)

# DIFICULDADE 1

slimeGigante = Boss("uma massa gosmenta gigante que se arrasta lentamente",
                    "Gloop", 3, 60, 1, 1, loot=item_slime)

esqueletoRei = Boss("um esqueleto coroado empunhando uma espada enferrujada",
                    "Bone King", 4, 50, 2, 1, loot=item_esqueleto)

necromante = Boss("um mago sombrio envolto em sombras que controla os mortos",
                  "Zar'kul", 10, 60, 3, 1, loot=item_necromante)

goblin = Boss("um goblin pequeno e irritante com uma adaga enferrujada",
              "Snix", 3, 50, 1, 1, loot=item_goblin)

morcegoGigante = Boss("um morcego gigante que voa em círculos emitindo gritos agudos",
                      "Noctis", 2, 45, 1, 1, loot=item_morcego)

zumbi = Boss("um morto-vivo lento com carne em decomposição",
             "Rotwalker", 4, 65, 2, 1, loot=item_zumbi)

loboSombrio = Boss("um lobo envolto em sombras que se move silenciosamente",
                   "Shadowfang", 5, 70, 2, 1, loot=item_loboSombrio)

espirito = Boss("um espírito errante que atravessa paredes e sussurra",
                "Whisper", 4, 55, 1, 1, loot=item_espirito)

bandido = Boss("um ladrão ágil que tenta te atacar de surpresa",
               "Ravik", 5, 60, 2, 1, loot=item_bandido)

cobraGigante = Boss("uma serpente venenosa com olhos hipnotizantes",
                    "Viperax", 4, 65, 1, 1, loot=item_cobra)

soldadoCorrompido = Boss("um antigo soldado tomado por uma maldição sombria",
                         "Fallen Guard", 6, 75, 2, 1, loot=item_soldado)

espantalhoVivo = Boss("um espantalho que ganhou vida e se move de forma assustadora",
                      "Hayterror", 3, 50, 1, 1, loot=item_espantalho)

ratoGigante = Boss("um rato enorme com dentes afiados e comportamento agressivo",
                   "Gnaw", 2, 40, 1, 1, loot=item_rato)


# DIFICULDADE 2
aranhaGigante = Boss("uma aranha monstruosa com patas afiadas como lâminas",
                     "Aracnys", 7, 90, 1, 3, loot=item_aranha)

loboGigante = Boss("um lobo gigantesco com aproximadamente 8 metros de altura e olhos flamejantes",
                   "Fenrir", 5, 100, 2, 1, loot=item_fenrir)

ogro = Boss("um ogro brutal com um porrete enorme coberto de sangue seco",
            "Grum", 9, 140, 4, 2, loot=item_ogro)

feiticeira = Boss("uma feiticeira que manipula energia arcana roxa",
                  "Morganna", 11, 100, 3, 2, loot=item_feiticeira)

dragaoAncestral = Boss("um dragão colossal que cobre o céu com suas asas e cospe fogo azul",
                       "Ignis Draconis", 12, 150, 5, 2, loot=item_dragaoAncestral)

hidra = Boss("uma criatura com várias cabeças que se regeneram ao serem cortadas",
             "Hydrath", 9, 130, 4, 2, loot=item_hidra)

demônio = Boss("um demônio das profundezas com chifres gigantes e olhos vermelhos",
               "Azgorath", 11, 120, 6, 2, loot=item_demonio)

cavaleiroNegro = Boss("um guerreiro amaldiçoado com armadura negra e espada sombria",
                      "Dread Knight", 10, 110, 5, 2, loot=item_cavaleiro)


# DIFICULDADE 3

minotauro = Boss("uma criatura metade homem metade touro com força absurda",
                 "Asterion", 14, 180, 6, 3, loot=item_minotauro)

dragaoNegro = Boss("um dragão negro envolto em sombras e destruição",
                   "Noctyra", 16, 200, 8, 3, loot=item_dragaoNegro)

golemPedra = Boss("um golem feito de rochas maciças que treme o chão a cada passo",
                  "Titanus", 8, 200, 10, 3, loot=item_golem)


# DIFICULDADE 4

deusGuerra = Boss("uma entidade divina que carrega o peso de incontáveis batalhas",
                  "Krathos", 20, 300, 12, 4, loot=item_deusGuerra)

entidadeCosmica = Boss("uma entidade além da compreensão humana que distorce a realidade",
                       "Voidrex", 25, 350, 15, 4, loot=item_entidade)

bossesFaceis = [
    slimeGigante, 
    esqueletoRei, 
    loboGigante, 
    necromante, 
    aranhaGigante,
    goblin, 
    morcegoGigante, 
    zumbi, 
    loboSombrio, 
    espirito, 
    bandido,
    cobraGigante, 
    soldadoCorrompido, 
    espantalhoVivo, 
    ratoGigante,
]

bossesMedios = [
    ogro,
    feiticeira,
    dragaoAncestral,
    hidra,
    demônio,
    cavaleiroNegro,
    ]

bossesDificeis = [
    minotauro,
    dragaoNegro,
    golemPedra,
    ]

bossesLendarios = [
    deusGuerra,
    entidadeCosmica
    ]

