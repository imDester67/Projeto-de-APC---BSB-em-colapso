# Documentação - BSB EM COLAPSO

## Visão Geral

**BSB em Colapso** é um jogo de simulação política desenvolvido em Python onde o jogador assume o papel de gestor de Brasília. O objetivo é equilibrar quatro indicadores fundamentais da cidade através de decisões estratégicas sobre eventos diversos.

## Requisitos do Sistema

### Bibliotecas Necessárias
- `sys` - Controle de sistema
- `random` - Geração de eventos aleatórios
- `os` - Operações do sistema operacional
- `time` - Controle de tempo e delays
- `colorama` - Colorização do terminal

### Instalação
```bash
pip install colorama
```

## Estrutura do Jogo

### Indicadores Principais

O jogo possui 4 indicadores que devem ser mantidos entre 1% e 99%:

1. **População** (pop) - Popularidade e satisfação do povo
2. **Economia** (eco) - Recursos financeiros públicos
3. **Tecnologia** (tec) - Nível de desenvolvimento tecnológico
4. **Meio-Ambiente** (meio) - Qualidade ambiental

**Valor inicial:** Todos começam em 50%

### Condições de Vitória/Derrota

- **Vitória:** Completar todos os eventos disponíveis sem game over
- **Derrota:** Qualquer indicador atingir 0% ou 100%

## Funções Principais

### Interface e Navegação

#### `Menu()`
Menu principal do jogo com opções:
- Iniciar novo jogo
- Ver créditos
- Sair

#### `tela_inicial()`
Exibe a tela inicial com logo ASCII e opções do menu.

#### `limpar_tela()`
Limpa o terminal (compatível com Windows e Unix).

#### `mostrar_interface(pop, eco, meio, tec)`
Exibe os indicadores em formato de barras visuais.
- Barras com 20 caracteres de comprimento
- Coloração amarela para progresso
- Valores numéricos opcionais (quando software ativado)

#### `barra(nome, valor)`
Gera representação visual de um indicador.
- Cada 5 pontos = 1 caractere preenchido
- Máximo: 20 caracteres

### Sistema de Game Over

Cada indicador possui duas funções de game over (mínimo e máximo):

- `minPop()` / `maxPop()` - População
- `minEco()` / `maxEco()` - Economia
- `minMeio()` / `maxMeio()` - Meio-Ambiente
- `minTec()` / `maxTec()` - Tecnologia

#### `checar_game_over(pop, eco, meio, tec)`
Verifica se algum indicador atingiu valores extremos e encerra o jogo.

### Sistema de Eventos

#### Eventos Base (17 eventos principais)
- `evento1` - Wi-Fi público em áreas carentes
- `evento2` - Sistema de segurança com IA
- `evento3` - Substituição da frota de ônibus
- `evento4` - Aceitar criptomoedas
- `evento5` - Construir supercomputador (OpenAI)
- `evento6` - Redução de impostos
- `evento7` - Vazamento de dados
- `evento8` - Cortes no orçamento
- `evento9` - Polo industrial no Gama
- `evento10` - Lazule's Tech
- `evento11` - Seca
- `evento12` - Tarifa social de energia
- `evento13` - Aumento da tarifa de ônibus
- `evento14` - Instalação de energia solar
- `evento15` - Crise hídrica
- `evento16` - Projeto Brasília Verde
- `evento17` - Incêndio no Parque Nacional
- `evento18` - Drones de entrega
- `evento19` - Modernização do ensino

#### Eventos Encadeados

Alguns eventos geram eventos subsequentes baseados nas escolhas:

**Cadeia do Supercomputador:**
- `evento5` → `evento5A` (Superaquecimento) → `evento5B` (Incêndio)

**Cadeia do Vazamento:**
- `evento7` → `evento7A` (Investigação) ou `evento7B` (Hackers)
- `evento7B` → `evento7C` (Acordo de paz)
- Qualquer recusa → `evento7final` (Cyber ataque)

**Cadeia Lazule's Tech:**
- `evento10` → `evento10A` (Ativação software) + `evento10B` (Prevenção crise)

**Cadeia de Manifestações:**
- `evento8` (Cortes) → `evento8A` (Manifestação saúde)
- `evento13` (Aumento tarifa) → `evento13A` (Manifestação transporte)

### Estrutura dos Eventos

Cada evento segue este padrão:

```python
def eventoX(stats):
    pop, eco, meio, tec = stats
    
    print_event('''
        TÍTULO DO EVENTO
        Descrição da situação...
        
        Efeitos: (sim)
        Indicador +/-
        
        Efeitos: (não)
        Indicador +/-
    ''')
    
    decisao = input('Digite "s" (sim) ou "n" (não): ').lower()
    eventos.remove(eventoX)
    
    while decisao not in 'sn' or decisao == "":
        # Validação de entrada
    
    if decisao == 's':
        # Modificações nos indicadores
    elif decisao == 'n':
        # Modificações alternativas
    
    return pop, eco, meio, tec
```

### Sistema de Coloração

#### `print_event(block)`
Função especial que adiciona cores aos efeitos:
- **Verde** (`Fore.GREEN`) - Efeitos positivos (linhas terminadas em "+")
- **Vermelho** (`Fore.RED`) - Efeitos negativos (linhas terminadas em "-")
- **Branco** (`Fore.WHITE`) - Texto normal

## Sistemas Especiais

### Eventos de Longa Duração

#### Seca
- **Ativação:** `evento11`
- **Duração:** 4 rodadas
- **Efeito:** -5 Meio-Ambiente por rodada
- **Variável:** `seca` e `tempo_seca`

#### Crise Hídrica
- **Ativação:** `evento15` (ou recusa em `evento10B`)
- **Duração:** 3 rodadas
- **Efeito:** -5 População por rodada
- **Variável:** `crise_hidro` e `tempo_hidro`

### Software Lazule's Tech
- **Ativação:** `evento10A`
- **Efeito:** Exibe valores numéricos nas barras de indicadores
- **Variável global:** `software`

## Função Principal

### `rodada()`
Loop principal do jogo que:

1. Inicializa todos os indicadores em 50%
2. Cria lista de eventos disponíveis
3. Reseta variáveis globais
4. **Loop de jogo:**
   - Verifica fim de eventos de longa duração
   - Exibe interface
   - Verifica game over
   - Escolhe evento aleatório
   - Executa evento
   - Aplica efeitos de eventos de longa duração
   - Remove eventos concluídos

## Fluxo de Execução

```
Menu()
  ↓
Escolha "Iniciar Jogo"
  ↓
rodada()
  ↓
Loop de Eventos
  ↓
Game Over ou Vitória
  ↓
Retorna ao Menu()
```

## Variáveis Globais

- `eventos` - Lista de eventos disponíveis
- `seca` - Contador de rodadas da seca
- `tempo_seca` - Tempo decorrido da seca
- `crise_hidro` - Contador de rodadas da crise
- `tempo_hidro` - Tempo decorrido da crise
- `software` - Status do software Lazule's Tech

## Script Auxiliar

### `apply_color_to_events.py`

Script de automação que:
1. Lê o arquivo `logica_brasilia2.py`
2. Insere a função `print_event()` após os imports
3. Substitui chamadas `print()` por `print_event()` em blocos que:
   - Contêm "Efeitos:"
   - Não contêm "Fore." (evita duplicação)
4. Usa regex para identificar blocos print completos
5. Salva arquivo modificado

**Uso:**
```python
python apply_color_to_events.py
```

## Mensagens de Arte ASCII

O jogo inclui arte ASCII para:
- Logo principal (cidade de Brasília)
- Game over (caveira hacker)
- Fim da seca (nuvem de chuva)
- Fim da crise hídrica (reservatório)
- Vitória (cidade novamente)

## Dicas de Jogabilidade

1. **Equilíbrio:** Mantenha todos os indicadores entre 20-80% para segurança
2. **Eventos encadeados:** Algumas escolhas desbloqueiam eventos futuros
3. **Eventos de longa duração:** Prepare-se para perdas graduais
4. **Software Lazule's Tech:** Útil para decisões mais precisas
5. **Leia os efeitos:** Sempre analise consequências antes de decidir

## Créditos

Desenvolvido por:
- Pedro Vítor de Mendonça Furtado
- Gusthavo de Oliveira Silva
- Marco Antônio Lopes de Medeiros
- Gabriel Peres de Oliveira

**Projeto:** Trabalho Final de APC (Algoritmos e Programação de Computadores)
