class Item:
    def __init__(self, nomeItem, tipoItem: int, bonus_ataque=0, bonus_defesa=0, efeitoItem=None, funcaoItem: int = 0):
        self.nomeItem = nomeItem
        self.tipoItem = tipoItem
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa
        self.efeitoItem = efeitoItem
        self.funcaoItem = funcaoItem

        # efeitoItem 1 = cura, efeitoItem 2 = dano extra, efeitoItem 3 = resistência extra
        # funcaoItem 1 = ataque, funcaoItem 2 = defesa, funcaoItem 3 = suporte

    def aplicarEfeito(self, jogador):
        if self.efeitoItem == 1:
            self.efeitoItem = "Cura"
            self.funcaoItem = "Suporte"
            jogador.hp += self.bonus_defesa
        elif self.efeitoItem == 2:
            self.efeitoItem = "Dano extra"
            self.funcaoItem = "Ataque"
            jogador.dano += self.bonus_ataque
        elif self.efeitoItem == 3:
            self.efeitoItem = "Resistencia extra"
            self.funcaoItem = "Defesa"
            jogador.resistencia += self.bonus_defesa
        else:
            print("Sem efeitoItem")

    def mostrarAtributosItem(self):
        print(f"Item: {self.nomeItem}")
        print(f"Tipo: {self.tipoItem}")
        print(f"Bônus de Ataque: {self.bonus_ataque}")
        print(f"Bônus de Defesa: {self.bonus_defesa}")
        print(f"Função: {self.funcaoItem}")

# Dificuldade 1 (FÁCIL)

item_slime = Item("Núcleo Gosmento", 1, bonus_defesa=1, efeitoItem=1, funcaoItem=3)

item_esqueleto = Item("Espada Enferrujada do Rei", 1, bonus_ataque=3, efeitoItem=2, funcaoItem=1)

item_fenrir = Item("Presas de Fenrir", 1, bonus_ataque=4, efeitoItem=2, funcaoItem=1)

item_necromante = Item("Cajado Sombrio", 2, bonus_ataque=4, efeitoItem=1, funcaoItem=3)

item_aranha = Item("Carapaça de Aracnys", 1, bonus_defesa=3, efeitoItem=3, funcaoItem=2)

item_goblin = Item("Adaga de Snix", 1, bonus_ataque=2, efeitoItem=2, funcaoItem=1)

item_morcego = Item("Asas de Noctis", 3, bonus_defesa=2, efeitoItem=3, funcaoItem=3)

item_zumbi = Item("Armadura Podre", 1, bonus_defesa=3, efeitoItem=3, funcaoItem=2)

item_loboSombrio = Item("Garras Sombrias", 1, bonus_ataque=4, efeitoItem=2, funcaoItem=1)

item_espirito = Item("Essência Etérea", 2, bonus_defesa=2, efeitoItem=1, funcaoItem=3)

item_bandido = Item("Adaga Rápida", 1, bonus_ataque=3, efeitoItem=2, funcaoItem=1)

item_cobra = Item("Veneno de Viperax", 2, bonus_ataque=4, efeitoItem=2, funcaoItem=1)

item_soldado = Item("Escudo Quebrado", 1, bonus_defesa=3, efeitoItem=3, funcaoItem=2)

item_espantalho = Item("Foice Amaldiçoada", 1, bonus_ataque=3, efeitoItem=2, funcaoItem=1)

item_rato = Item("Dentes Afiados", 1, bonus_ataque=2, efeitoItem=2, funcaoItem=1)


# Dificuldade 2 (MÉDIO)

item_ogro = Item("Porrete Brutal", 1, bonus_ataque=7, efeitoItem=2, funcaoItem=1)

item_feiticeira = Item("Orbe Arcano", 2, bonus_ataque=8, efeitoItem=1, funcaoItem=3)

item_dragaoAncestral = Item("Escama Dracônica", 1, bonus_defesa=9, efeitoItem=3, funcaoItem=2)

item_hidra = Item("Coração da Hidra", 1, bonus_ataque=8, efeitoItem=1, funcaoItem=3)

item_demonio = Item("Lâmina Infernal", 1, bonus_ataque=9, efeitoItem=2, funcaoItem=1)

item_cavaleiro = Item("Armadura Negra", 1, bonus_defesa=8, efeitoItem=3, funcaoItem=2)


# Dificuldade 3 (Difícil)

item_minotauro = Item("Machado do Labirinto", 1, bonus_ataque=12, efeitoItem=2, funcaoItem=1)

item_dragaoNegro = Item("Asa Sombria", 3, bonus_ataque=13, efeitoItem=2, funcaoItem=1)

item_golem = Item("Núcleo de Pedra", 1, bonus_defesa=14, efeitoItem=3, funcaoItem=2)


# Dificuldade 4 (Lendário)

item_deusGuerra = Item("Espada da Guerra Eterna", 1, bonus_ataque=18, efeitoItem=2, funcaoItem=1)

item_entidade = Item("Fragmento do Vazio", 2, bonus_ataque=20, efeitoItem=2, funcaoItem=1)