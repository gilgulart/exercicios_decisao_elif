# Eldoria - Jogo de Aventura em Texto

## Sobre o jogo
Eldoria é um jogo de aventura em texto ambientado em um mundo fantástico. O jogador assume o papel de um herói ou heroína corajoso(a) de Eldoria e parte em uma missão para encontrar o elixir da vida e enfrentar criaturas lendárias.

O jogo apresenta uma narrativa inicial com escolhas de caminho e combate, incluindo:
- seleção do personagem
- apresentação da história e cenário
- encontro com inimigos
- opções de ação como lutar, fugir ou tentar ser amigável
- mapa do mundo com áreas diferentes para explorar

> Observação: o projeto está em desenvolvimento e apresenta a estrutura inicial da aventura, mas nem todas as lógicas de combate e caminhos estão completamente implementadas.

## Estrutura do projeto
- `main_game.py`: arquivo principal que inicia o jogo e exibe a introdução.
- `arts/ascii_arts.py`: arte em ASCII usada na tela de título.
- `characters/rpg_game_person.py`: classe do personagem jogador.
- `story/introHistory.py`: introdução da missão e primeiras opções de escolha.
- `story/history.py`: textos para encontros e combate.
- `systems/getChoice.py`: valida as escolhas numéricas do jogador.
- `systems/map.py`: apresenta o mapa e as opções de destino.
- `utils/prompt.py`: funções para exibir texto com efeito de digitação.
- `utils/transition.py`: transições entre cenas.

## Dependências Python
Este projeto utiliza as seguintes bibliotecas:

- `colorama`
- `pyfiglet`

### Instalação
Você pode instalar as dependências diretamente com:

```powershell
pip install colorama pyfiglet
```

Ou usar o arquivo `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Como executar o jogo
Para rodar o jogo corretamente, execute a partir da pasta pai de `jogos`:

```powershell
cd C:\Users\tudod\exercicios_decisao_elif
python -m jogos.main_game
```

## Observações
Se quiser executar o jogo diretamente de dentro da pasta `jogos`, será necessário ajustar os imports para caminhos relativos ou diretos. No estado atual, o comando recomendado é:

```powershell
python -m jogos.main_game
```
