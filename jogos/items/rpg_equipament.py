class Item:
    def __init__(self, nome, tipo: int, bonus_ataque=0, bonus_defesa=0, efeito=None, funcao: int = 0):
        self.nome = nome
        self.tipo = tipo
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa
        self.efeito = efeito
        self.funcao = funcao




        # efeito 1 = cura, efeito 2 = dano extra, efeito 3 = resistência extra, feito 4 = velocidade extra, efeito 5 = veneno
        # funcao 1 = ataque, funcao 2 = defesa, funcao 3 = suporte
        # tipo: 1 curta distancia, 2 media distancia, 3 longa distancia

# Dificuldade 1 (FÁCIL)

item_slime = Item("Núcleo Gosmento", 1, bonus_defesa=1, efeito=1, funcao=3)

item_esqueleto = Item("Espada Enferrujada do Rei", 1, bonus_ataque=3, efeito=2, funcao=1)

item_fenrir = Item("Presas de Fenrir", 1, bonus_ataque=4, efeito=4, funcao=1)

item_necromante = Item("Cajado Sombrio", 2, bonus_ataque=4, efeito=1, funcao=3)

item_aranha = Item("Carapaça de Aracnys", 1, bonus_defesa=3, efeito=3, funcao=2)

item_goblin = Item("Adaga de Snix", 1, bonus_ataque=2, efeito=4, funcao=1)

item_morcego = Item("Asas de Noctis", 3, bonus_defesa=2, efeito=4, funcao=3)

item_zumbi = Item("Armadura Podre", 1, bonus_defesa=3, efeito=3, funcao=2)

item_loboSombrio = Item("Garras Sombrias", 1, bonus_ataque=4, efeito=2, funcao=1)

item_espirito = Item("Essência Etérea", 2, bonus_defesa=2, efeito=1, funcao=3)

item_bandido = Item("Adaga Rápida", 1, bonus_ataque=3, efeito=4, funcao=1)

item_cobra = Item("Veneno de Viperax", 2, bonus_ataque=4, efeito=5, funcao=1)

item_soldado = Item("Escudo Quebrado", 1, bonus_defesa=3, efeito=3, funcao=2)

item_espantalho = Item("Foice Amaldiçoada", 1, bonus_ataque=3, efeito=2, funcao=1)

item_rato = Item("Dentes Afiados", 1, bonus_ataque=2, efeito=5, funcao=1)

# Dificuldade 2 (MÉDIO)

item_ogro = Item("Porrete Brutal", 1, bonus_ataque=7, efeito=2, funcao=1)

item_feiticeira = Item("Orbe Arcano", 2, bonus_ataque=8, efeito=1, funcao=3)

item_dragaoAncestral = Item("Escama Dracônica", 1, bonus_defesa=9, efeito=3, funcao=2)

item_hidra = Item("Coração da Hidra", 1, bonus_ataque=8, efeito=1, funcao=3)

item_demonio = Item("Lâmina Infernal", 1, bonus_ataque=9, efeito=2, funcao=1)

item_cavaleiro = Item("Armadura Negra", 1, bonus_defesa=8, efeito=3, funcao=2)

# Dificuldade 3 (Difícil)

item_minotauro = Item("Machado do Labirinto", 1, bonus_ataque=12, efeito=2, funcao=1)

item_dragaoNegro = Item("Asa Sombria", 3, bonus_ataque=13, efeito=4, funcao=1)

item_golem = Item("Núcleo de Pedra", 1, bonus_defesa=14, efeito=3, funcao=2)

# Dificuldade 4 (Lendário)

item_deusGuerra = Item("Espada da Guerra Eterna", 1, bonus_ataque=18, efeito=2, funcao=1)

item_entidade = Item("Fragmento do Vazio", 2, bonus_ataque=20, efeito=5, funcao=1)