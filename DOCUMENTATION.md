# Documentação - BSB em Colapso

## Visão Geral
**BSB em Colapso** é um jogo de simulação em Python onde o jogador assume o papel de gestor de Brasília, tomando decisões que afetam quatro indicadores principais da cidade: População, Economia, Tecnologia e Meio Ambiente. O objetivo é completar o mandato mantendo todos os indicadores equilibrados entre 0 e 100.

## Requisitos
- Python 3.x
- Bibliotecas padrão: `sys`, `random`, `os`

## Estrutura do Código

### Variáveis Globais
- `software`: Booleana que controla se os indicadores mostram valores numéricos
- `seca`: Contador de rodadas do evento de seca
- `crise_hidro`: Contador de rodadas da crise hídrica
- `eventos`: Lista contendo todos os eventos disponíveis no jogo

### Funções Principais

#### `limpar_tela()`
Limpa o terminal para melhor visualização.
- **Compatibilidade**: Windows (`cls`) e Unix/Linux (`clear`)

#### `barra(nome, valor)`
Cria representação visual dos indicadores.
- **Parâmetros**:
  - `nome` (str): Nome do indicador
  - `valor` (int): Valor atual (0-100)
- **Retorno**: String formatada com barra visual
- **Comportamento**: Mostra valores numéricos apenas se `software == True`

#### `mostrar_interface(pop, eco, meio, tec)`
Exibe a interface principal do jogo com todos os indicadores.
- **Parâmetros**: Valores atuais dos 4 indicadores (0-100)

#### `checar_game_over(pop, eco, meio, tec)`
Verifica condições de derrota.
- **Condições**: Qualquer indicador atingir 0 ou 100
- **Ação**: Exibe mensagem específica e encerra o jogo

### Funções de Game Over
Mensagens específicas para cada tipo de derrota:
- `maxTec()`: Tecnologia = 100 (BigTechs dominam)
- `minTec()`: Tecnologia = 0 (Cidade mal desenvolvida)
- `maxPop()`: População = 100
- `minPop()`: População = 0 (Revolta popular)
- `maxMeio()`: Meio Ambiente = 100 (Capivaras no poder)
- `minMeio()`: Meio Ambiente = 0 (Cidade em chamas)
- `maxEco()`: Economia = 100 (Corrupção)
- `minEco()`: Economia = 0 (Cidade mais pobre)

## Sistema de Eventos

### Estrutura Padrão de Eventos
Cada evento segue o padrão:
```python
def eventoX(stats):
    pop, eco, meio, tec = stats
    # Descrição do evento
    # Efeitos de cada escolha
    decisao = input('\nDigite "s" ou "n": ').lower()
    eventos.remove(eventoX)  # Remove evento da lista
    # Validação de entrada
    # Aplicação dos efeitos
    return pop, eco, meio, tec
```

### Eventos Implementados

#### Eventos Simples (1-4, 6, 8-9, 12-14, 16-19)
Eventos de decisão única com consequências diretas.

**Exemplos**:
- **Evento 1**: Wi-Fi público em áreas carentes
- **Evento 3**: Substituição da frota por ônibus elétricos
- **Evento 12**: Tarifa social de energia

#### Eventos em Cadeia

**Série 5 (Supercomputador)**:
- `evento5`: OpenAI propõe construir supercomputador
- `evento5A`: Problemas de superaquecimento
- `evento5B`: Incêndio nas instalações

**Série 7 (Hackers)**:
- `evento7`: Vazamento de dados
- `evento7A`: Investigação e melhoria de segurança
- `evento7B`: Grupo hacker reivindica autoria
- `evento7C`: Proposta de acordo de paz
- `evento7final`: Cyber ataque em massa (Game Over)

**Série 10 (Startup)**:
- `evento10`: Apoio a startup local
- `evento10A`: Ativa modo software (indicadores numéricos)
- `evento10B`: Prevenção de crise hídrica

**Série 13 (Tarifas)**:
- `evento13`: Aumento da tarifa de ônibus
- `evento13A`: Manifestação contra o aumento

#### Eventos de Longa Duração
- **Evento 11 (Seca)**: Reduz Meio Ambiente em 5 pontos por rodada durante 4 rodadas
- **Evento 15 (Crise Hídrica)**: Reduz População em 5 pontos por rodada durante 3 rodadas

### Lista de Eventos Iniciais
```python
eventos = [
    evento1, evento2, evento3, evento4,
    evento6, evento7, evento8, evento9, evento10,
    evento11, evento12, evento13, evento14,
    evento16, evento17, evento18, evento19
]
```

## Mecânicas de Jogo

### Indicadores
Todos iniciam em **50 pontos**:
- **População**: Satisfação popular
- **Economia**: Saúde financeira
- **Tecnologia**: Desenvolvimento tecnológico
- **Meio Ambiente**: Sustentabilidade ambiental

### Função Principal: `rodada()`

**Fluxo de execução**:
1. Inicializa indicadores e variáveis de eventos longos
2. Loop principal:
   - Verifica término de eventos de longa duração
   - Exibe interface
   - Verifica game over
   - Escolhe evento aleatório
   - Aplica efeitos de eventos de longa duração
   - Repete até vitória ou derrota

**Condição de Vitória**: Completar todos os eventos da lista

## Interface do Jogo

### Tela Principal
```
==================================================
      B S B   E M   C O L A P S O
==================================================
População     : [##########··········] 50
Economia      : [##########··········] 50
Tecnologia    : [##########··········] 50
Meio-Ambiente : [##########··········] 50
==================================================
```

### Sistema de Barras
- 20 caracteres de largura
- `#` representa porções preenchidas
- `·` representa porções vazias
- Cada `#` equivale a 5 pontos

## Inicialização do Jogo

1. Mensagem de boas-vindas
2. Explicação dos 4 indicadores
3. Aguarda Enter para iniciar
4. Executa função `rodada()`

## Recursos Especiais

### Modo Software (Evento 10A)
- Ativa exibição de valores numéricos nas barras
- Melhora visibilidade da situação atual

### Eventos Recursivos
Alguns eventos podem ser reativados:
- `evento7`: Retorna após `evento7A` se jogador não melhorar segurança
- `evento5`: Pode retornar via `evento6`
- `evento15`: Pode ser acionado via `evento10B`

## Dicas de Desenvolvimento

### Para Adicionar Novos Eventos
1. Criar função seguindo o padrão `eventoX(stats)`
2. Implementar texto descritivo e opções
3. Validar entrada do usuário
4. Aplicar modificações nos indicadores
5. Gerenciar remoção/adição de eventos
6. Adicionar à lista `eventos`

### Balanceamento
- Modificações típicas: ±10 a ±35 pontos
- Eventos positivos geralmente têm custos
- Eventos em cadeia têm impactos progressivos
- Eventos de longa duração causam -5 por rodada

## Observações Técnicas

- **Encoding**: Código usa caracteres especiais (necessário UTF-8)
- **Validação**: Todas as entradas são validadas em loops
- **Estado**: Eventos removidos após execução (exceto recursivos)
- **Aleatoriedade**: `random.choice()` seleciona eventos

## Possíveis Melhorias

1. Sistema de save/load
2. Múltiplos finais de vitória
3. Sistema de conquistas
4. Dificuldade ajustável
5. Mais eventos encadeados
6. Interface gráfica
7. Sistema de pontuação
8. Estatísticas de fim de jogo
