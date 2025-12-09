# BSB em Colapso 🏛️

Um jogo de simulação em Python onde você assume o papel de gestor de Brasília, tomando decisões que afetam quatro indicadores principais da cidade: População, Economia, Tecnologia e Meio Ambiente.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Jogar](#como-jogar)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuindo](#contribuindo)
- [Créditos](#créditos)

## 🎮 Sobre o Projeto

**BSB em Colapso** é um jogo de simulação textual desenvolvido como trabalho final da disciplina de Algoritmos e Programação de Computadores (APC). O jogador precisa equilibrar quatro indicadores cruciais da cidade de Brasília durante seu mandato como gestor:

- 🧑‍🤝‍🧑 **População**: Nível de popularidade e satisfação do povo
- 💰 **Economia**: Quantidade de recursos nos cofres públicos
- 🖥️ **Tecnologia**: Nível de desenvolvimento tecnológico
- 🌳 **Meio Ambiente**: Qualidade ambiental da cidade

**Objetivo**: Completar o mandato mantendo todos os indicadores equilibrados entre 1 e 99. Se qualquer indicador atingir 0 ou 100, é Game Over!

## 🔧 Requisitos

- Python 3.x
- Biblioteca colorama (para cores no terminal)

## 📥 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/bielperes/APC-BSB-em-colapso.git
cd APC-BSB-em-colapso
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o jogo:
```bash
python logica_brasilia.py
```

## 🎯 Como Jogar

### Inicialização

1. Execute o arquivo principal `logica_brasilia.py`
2. No menu inicial, escolha:
   - `1` - Iniciar novo jogo
   - `2` - Ver créditos
   - `0` - Sair

### Interface do Jogo

Durante o jogo, você verá uma interface com os quatro indicadores representados por barras visuais:

```
==================================================
      I N D I C A D O R E S
==================================================
População     : [##########··········] 50
Economia      : [##########··········] 50
Tecnologia    : [##########··········] 50
Meio-Ambiente : [##########··········] 50
==================================================
```

### Mecânica

- Cada rodada apresenta um evento com uma decisão binária (Sim/Não)
- Suas escolhas afetam os indicadores de forma diferente
- Linhas em **verde** terminando com `+` indicam efeitos positivos
- Linhas em **vermelho** terminando com `-` indicam efeitos negativos
- Mantenha todos os indicadores entre 1 e 99 para vencer

### Condições de Game Over

Cada indicador tem consequências específicas se atingir 0 ou 100:

| Indicador | Valor 0 | Valor 100 |
|-----------|---------|-----------|
| **População** | Revolta popular | Assassinato em discurso |
| **Economia** | Cidade mais pobre do Brasil | Investigação por corrupção |
| **Tecnologia** | Cidade mal desenvolvida | Domínio das BigTechs |
| **Meio Ambiente** | Cidade em chamas | Invasão de capivaras |

## ✨ Funcionalidades

### Sistema de Eventos

- **19 eventos principais** com narrativas únicas
- **Eventos em cadeia**: Algumas decisões desencadeiam sequências de eventos
- **Eventos de longa duração**: Crises que persistem por múltiplas rodadas
- **Eventos recursivos**: Alguns eventos podem retornar dependendo de escolhas anteriores

### Tipos de Eventos

#### Eventos Simples
Decisões pontuais com consequências imediatas (Ex: Wi-Fi público, ônibus elétricos, tarifa social)

#### Eventos em Cadeia
Sequências narrativas que se desenvolvem ao longo do jogo:
- **Série do Supercomputador**: OpenAI propõe construção → problemas de superaquecimento → incêndio
- **Série dos Hackers**: Vazamento de dados → investigação → cyber ataque em massa
- **Série da Startup**: Apoio a empresa local → desenvolvimento de software → prevenção de crises

#### Eventos de Longa Duração
- **Seca**: Reduz Meio Ambiente em 5 pontos por rodada durante 4 rodadas
- **Crise Hídrica**: Reduz População em 5 pontos por rodada durante 3 rodadas

### Modo Software

Um recurso especial que pode ser desbloqueado durante o jogo (Evento 10A), exibindo valores numéricos exatos ao lado das barras de indicadores.

## 📂 Estrutura do Código

### Arquivos Principais

- `logica_brasilia.py`: Arquivo principal do jogo contendo toda a lógica
- `apply_color_to_events.py`: Script utilitário para aplicar cores aos eventos
- `README.md`: Documentação principal (este arquivo)
- `DOCUMENTATION.md`: Documentação técnica detalhada

### Funções Principais

#### Interface e Visualização
- `limpar_tela()`: Limpa o terminal
- `barra(nome, valor)`: Cria representação visual dos indicadores
- `mostrar_interface(pop, eco, meio, tec)`: Exibe interface principal do jogo
- `print_event(block)`: Aplica cores aos textos de eventos

#### Controle de Jogo
- `Menu()`: Gerencia menu inicial e navegação
- `rodada()`: Loop principal do jogo
- `checar_game_over(pop, eco, meio, tec)`: Verifica condições de derrota

#### Eventos
- `evento1()` a `evento19()`: Eventos principais do jogo
- `eventoXA()`, `eventoXB()`: Variações e desdobramentos de eventos
- Cada evento segue o padrão: recebe stats, apresenta situação, processa decisão, retorna stats atualizados

### Variáveis Globais

```python
software = False  # Controla exibição de valores numéricos
seca = 0         # Contador de rodadas do evento de seca
crise_hidro = 0  # Contador de rodadas da crise hídrica
eventos = []     # Lista de eventos disponíveis
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Aqui estão algumas sugestões de melhorias:

### Ideias para Novos Recursos

1. Sistema de save/load
2. Múltiplos finais de vitória com diferentes condições
3. Sistema de conquistas
4. Dificuldade ajustável
5. Mais eventos encadeados
6. Interface gráfica (GUI)
7. Sistema de pontuação
8. Estatísticas detalhadas ao final do jogo

### Como Adicionar Novos Eventos

1. Crie uma função seguindo o padrão:
```python
def eventoX(stats):
    pop, eco, meio, tec = stats
    
    # Descrição do evento
    print("Descrição da situação...")
    print_event('''
        Efeitos se aceitar:
        - População: +10
        - Economia: -5
        
        Efeitos se recusar:
        - Tecnologia: +5
        - Meio Ambiente: -10
    ''')
    
    # Processar decisão
    decisao = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(eventoX)
    
    # Aplicar efeitos
    if decisao == 's':
        pop += 10
        eco -= 5
    else:
        tec += 5
        meio -= 10
    
    return pop, eco, meio, tec
```

2. Adicione à lista de eventos no início do jogo
3. Teste e ajuste o balanceamento

## 👥 Créditos

Desenvolvido por:
- **Pedro Vítor de Mendonça Furtado**
- **Gusthavo de Oliveira Silva**
- **Marco Antônio Lopes de Medeiros**
- **Gabriel Peres de Oliveira**

Trabalho Final de APC - Universidade de Brasília

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

## 🔗 Links Úteis

- [Documentação Técnica Detalhada](DOCUMENTATION.md)
- [Python Official Documentation](https://docs.python.org/3/)
- [Colorama Library](https://pypi.org/project/colorama/)

---

⭐ Se você gostou deste projeto, considere dar uma estrela no repositório!
