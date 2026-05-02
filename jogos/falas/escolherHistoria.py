import random
from jogos.falas.maldicao_familia import MaldicaoFamilia
from jogos.falas.maldicao_pessoal import MaldicaoPessoal
from jogos.falas.perda_total import PerdaTotal


historias = [MaldicaoFamilia(), MaldicaoPessoal(), PerdaTotal()]

historia = random.choice(historias)

