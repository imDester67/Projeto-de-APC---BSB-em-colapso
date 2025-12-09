# Documentação Técnica para Desenvolvedores

## Arquitetura do Projeto

### Visão Geral

O projeto BSB em Colapso é um jogo textual implementado em Python usando programação procedural. A estrutura é monolítica, com toda a lógica contida no arquivo principal `logica_brasilia.py`.

### Estrutura de Arquivos

```
APC-BSB-em-colapso/
├── logica_brasilia.py              # Arquivo principal do jogo
├── apply_color_to_events.py     # Script utilitário para colorização
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação principal
├── DOCUMENTATION.md              # Documentação técnica detalhada
├── LICENSE                       # Licença MIT
├── CONTRIBUTING.md               # Guia de contribuição
├── CHANGELOG.md                  # Histórico de mudanças
├── .gitignore                    # Arquivos ignorados pelo Git
└── docs/
    ├── instalacao.md             # Guia de instalação
    ├── gameplay.md               # Guia de gameplay
    └── tecnica.md                # Esta documentação
```

## Fluxo de Execução

### Diagrama de Fluxo Principal

```
┌─────────────────┐
│   Inicializar   │
│     Jogo        │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Menu Inicial   │
│  1. Jogar       │
│  2. Créditos    │
│  0. Sair        │
└────────┬────────┘
         │
         v (opção 1)
┌─────────────────┐
│ Função rodada() │
│ Inicia com      │
│ stats = 50,50,  │
│      50,50      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Loop Principal │
│  - Escolhe      │
│    evento       │
│  - Executa      │
│  - Atualiza     │
│    stats        │
│  - Verifica     │
│    Game Over    │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    v         v
┌───────┐ ┌──────────┐
│Vitória│ │Game Over │
└───────┘ └──────────┘
```

### Fluxo de um Evento

```python
def eventoX(stats):
    # 1. Desempacotar estatísticas
    pop, eco, meio, tec = stats
    
    # 2. Apresentar narrativa
    print("Descrição do evento...")
    print_event("Efeitos...")
    
    # 3. Capturar decisão do jogador
    decisao = input('\nDigite "s" ou "n": ').lower()
    
    # 4. Remover evento da lista (impede repetição)
    eventos.remove(eventoX)
    
    # 5. Validar entrada
    while decisao not in ['s', 'n']:
        # Loop de validação
    
    # 6. Aplicar efeitos baseado na decisão
    if decisao == 's':
        # Modificar stats
    else:
        # Modificar stats alternativo
    
    # 7. Retornar estatísticas atualizadas
    return pop, eco, meio, tec
```

## Estruturas de Dados

### Variáveis Globais

```python
# Controle de modo
software = False  # Tipo: bool
                  # Propósito: Ativa exibição de valores numéricos

# Contadores de eventos de longa duração
seca = 0         # Tipo: int
                 # Range: 0-4
                 # Propósito: Contador de rodadas restantes de seca

crise_hidro = 0  # Tipo: int
                 # Range: 0-3
                 # Propósito: Contador de rodadas de crise hídrica

# Lista de eventos disponíveis
eventos = []     # Tipo: list[function]
                 # Propósito: Pool de eventos não executados
```

### Tupla de Estatísticas (stats)

```python
stats = (pop, eco, meio, tec)
# Tipo: tuple[int, int, int, int]
# Range de cada: 0-100 (valores típicos: 1-99 para gameplay)
# 
# Componentes:
# - pop  (int): População/Popularidade
# - eco  (int): Economia
# - meio (int): Meio Ambiente
# - tec  (int): Tecnologia
```

## Funções Principais

### Funções de Interface

#### `limpar_tela()`
```python
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
```
**Complexidade:** O(1)  
**Dependências:** `os`  
**Compatibilidade:** Windows (cls) / Unix (clear)

#### `barra(nome: str, valor: int) -> str`
```python
def barra(nome, valor):
    cheios = int(valor / 5)
    vazios = 20 - cheios
    if software:
        return f"{nome:<14}: [{Fore.YELLOW}#" * cheios + Fore.WHITE + "·" * vazios + f"] {valor}"
    else:
        return f"{nome:<14}: [{Fore.YELLOW}#" * cheios + Fore.WHITE + "·" * vazios + f"] "
```
**Complexidade:** O(1)  
**Parâmetros:**
- `nome`: Nome do indicador (str, 14 chars left-aligned)
- `valor`: Valor numérico 0-100 (int)

**Retorno:** String formatada com barra visual

**Lógica:**
- Cada `#` representa 5 pontos (20 símbolos máximo)
- Cor amarela para preenchido, branco para vazio
- Mostra valor numérico se `software == True`

#### `mostrar_interface(pop: int, eco: int, meio: int, tec: int)`
```python
def mostrar_interface(pop, eco, meio, tec):
    limpar_tela()
    print("=" * 50)
    print(" " * 15 + Fore.YELLOW + "I N D I C A D O R E S" + Fore.WHITE)
    print("=" * 50)
    print(barra("População", pop))
    print(barra("Economia", eco))
    print(barra("Tecnologia", tec))
    print(barra("Meio-Ambiente", meio))
    print("=" * 50 + "\n")
```
**Complexidade:** O(1)  
**Side Effects:** Limpa tela e imprime interface

#### `print_event(block: str)`
```python
def print_event(block):
    try:
        init()  # Inicializa colorama
    except Exception:
        pass
    for raw in block.splitlines():
        line = raw.rstrip()
        if line.strip().endswith('+'):
            print(Fore.GREEN + line + Fore.WHITE)
        elif line.strip().endswith('-'):
            print(Fore.RED + line + Fore.WHITE)
        else:
            print(line)
```
**Complexidade:** O(n) onde n = número de linhas  
**Lógica de Colorização:**
- Linhas terminando em '+' → Verde (positivo)
- Linhas terminando em '-' → Vermelho (negativo)
- Outras linhas → Branco (neutro)

### Funções de Controle

#### `checar_game_over(pop: int, eco: int, meio: int, tec: int)`
```python
def checar_game_over(pop, eco, meio, tec):
    if pop <= 0: minPop()
    if pop >= 100: maxPop()
    if eco <= 0: minEco()
    if eco >= 100: maxEco()
    if meio <= 0: minMeio()
    if meio >= 100: maxMeio()
    if tec <= 0: minTec()
    if tec >= 100: maxTec()
```
**Complexidade:** O(1)  
**Side Effects:** Pode chamar Menu() e encerrar jogo

**Condições de Game Over:**
| Condição | Função | Descrição |
|----------|--------|-----------|
| pop ≤ 0 | minPop() | Revolta popular |
| pop ≥ 100 | maxPop() | Assassinato |
| eco ≤ 0 | minEco() | Falência |
| eco ≥ 100 | maxEco() | Corrupção |
| meio ≤ 0 | minMeio() | Desastre ambiental |
| meio ≥ 100 | maxMeio() | Invasão de capivaras |
| tec ≤ 0 | minTec() | Subdesenvolvimento |
| tec ≥ 100 | maxTec() | Domínio das BigTechs |

#### `rodada()`
```python
def rodada():
    # Inicialização
    pop = eco = meio = tec = 50
    global seca, crise_hidro, software, eventos
    seca = crise_hidro = 0
    software = False
    eventos = [evento1, evento2, ..., evento19]
    
    # Loop principal
    while eventos:
        # Verificar fim de eventos longos
        if seca == 1 or crise_hidro == 1:
            # Reset contadores
            
        # Mostrar interface
        mostrar_interface(pop, eco, meio, tec)
        
        # Verificar game over
        checar_game_over(pop, eco, meio, tec)
        
        # Escolher e executar evento
        evento_atual = random.choice(eventos)
        pop, eco, meio, tec = evento_atual((pop, eco, meio, tec))
        
        # Aplicar efeitos de longa duração
        if seca > 0:
            meio -= 5
            seca -= 1
        if crise_hidro > 0:
            pop -= 5
            crise_hidro -= 1
    
    # Vitória
    limpar_tela()
    print("PARABÉNS! Você completou seu mandato!")
```
**Complexidade:** O(n) onde n = número de eventos  
**Algoritmo:** Loop while consome eventos da lista até vazio

## Sistema de Eventos

### Taxonomia de Eventos

```
Eventos (19 totais)
│
├─ Simples (13 eventos)
│  ├─ evento1: Wi-Fi público
│  ├─ evento2: Incentivo à reciclagem
│  ├─ evento3: Ônibus elétricos
│  ├─ evento4: Parque tecnológico
│  ├─ evento6: Fechamento de empresas
│  ├─ evento8: Casas sustentáveis
│  ├─ evento9: Aumento de tributos
│  ├─ evento12: Tarifa social
│  ├─ evento14: Coleta seletiva obrigatória
│  ├─ evento16: Projeto de hortas
│  ├─ evento17: Teleconsulta
│  ├─ evento18: Ciclofaixas
│  └─ evento19: Projeto educacional
│
├─ Em Cadeia (6 eventos em 3 séries)
│  ├─ Série Supercomputador
│  │  ├─ evento5 → evento5A → evento5B
│  │  └─ evento6 (recursivo, pode reativar evento5)
│  │
│  ├─ Série Hackers
│  │  ├─ evento7 → evento7A → evento7B → evento7C
│  │  ├─ evento7 (recursivo via evento7A)
│  │  └─ evento7final (Game Over especial)
│  │
│  └─ Série Startup
│     ├─ evento10 → evento10A (modo software)
│     └─ evento10B (ativa/desativa crise_hidro)
│
└─ Longa Duração (2 eventos)
   ├─ evento11: Seca (4 rodadas, -5 meio/rodada)
   ├─ evento13 → evento13A (manifestação)
   └─ evento15: Crise Hídrica (3 rodadas, -5 pop/rodada)
```

### Padrão de Implementação de Evento

```python
def eventoX(stats):
    """
    Template para novos eventos
    
    Args:
        stats (tuple): (pop, eco, meio, tec)
    
    Returns:
        tuple: (pop, eco, meio, tec) atualizados
    
    Side Effects:
        - Remove-se da lista eventos
        - Pode adicionar outros eventos
        - Pode modificar variáveis globais
    """
    # 1. Desempacotar
    pop, eco, meio, tec = stats
    
    # 2. Narrativa
    print("\n[TÍTULO DO EVENTO]")
    print("=" * 50)
    print("Descrição narrativa do que está acontecendo...")
    
    # 3. Apresentar opções com cores
    print_event('''
        Efeitos se aceitar:
        - População: +10 +
        - Economia: -5 -
        
        Efeitos se recusar:
        - Tecnologia: +5 +
        - Meio Ambiente: -10 -
    ''')
    
    # 4. Capturar decisão
    while True:
        decisao = input('\nDigite "s" para aceitar ou "n" para recusar: ').lower()
        if decisao in ['s', 'n']:
            break
        print("Opção inválida.")
    
    # 5. Remover evento
    eventos.remove(eventoX)
    
    # 6. Aplicar efeitos
    if decisao == 's':
        pop += 10
        eco -= 5
        print("\n[Texto da consequência positiva]")
    else:
        tec += 5
        meio -= 10
        print("\n[Texto da consequência negativa]")
    
    # 7. Efeitos especiais (opcional)
    # Adicionar eventos em cadeia
    # Modificar variáveis globais
    # Ativar eventos de longa duração
    
    # 8. Pausa dramática
    input("\nPressione Enter para continuar...")
    
    # 9. Retornar stats atualizadas
    return pop, eco, meio, tec
```

### Eventos Especiais - Implementação

#### Evento de Longa Duração (Seca)
```python
def evento11(stats):
    global seca
    # ... lógica do evento ...
    seca = 4  # Ativa por 4 rodadas
    return pop, eco, meio, tec

# Na função rodada():
if seca > 0:
    print(f"\n⚠️  SECA EM ANDAMENTO! ({seca} rodadas restantes)")
    meio -= 5
    seca -= 1
```

#### Evento Recursivo (Hackers)
```python
def evento7A(stats):
    # ... apresentação ...
    if decisao == 's':
        # Jogador melhora segurança, série continua
        eventos.append(evento7B)
    else:
        # Jogador ignora, hackers retornam
        eventos.append(evento7)
    return pop, eco, meio, tec
```

#### Evento que Ativa Modo (Modo Software)
```python
def evento10A(stats):
    global software
    # ... lógica ...
    if decisao == 's':
        software = True  # Ativa valores numéricos
        print("\n✓ Modo Software Ativado!")
    return pop, eco, meio, tec
```

## Balanceamento

### Princípios de Design

1. **Range de Valores:**
   - Modificações pequenas: ±5 a ±10
   - Modificações médias: ±15 a ±25
   - Modificações grandes: ±30 a ±35
   - Eventos de longa duração: -5 por rodada

2. **Trade-offs:**
   - Toda escolha benéfica deve ter um custo
   - Indicadores geralmente se movem em pares
   - Exemplo: +Tecnologia/-Economia ou +População/-Meio Ambiente

3. **Progressão:**
   - Eventos iniciais têm efeitos menores
   - Eventos em cadeia aumentam progressivamente
   - Eventos finais podem ter consequências maiores

### Tabela de Balanceamento Típico

| Tipo de Evento | Range de Modificação | Número de Indicadores Afetados |
|----------------|---------------------|--------------------------------|
| Simples Pequeno | ±5 a ±15 | 2 |
| Simples Médio | ±15 a ±25 | 2-3 |
| Simples Grande | ±25 a ±35 | 3-4 |
| Cadeia Inicial | ±10 a ±20 | 2 |
| Cadeia Intermediário | ±15 a ±30 | 2-3 |
| Cadeia Final | ±20 a ±35 | 3-4 |
| Longa Duração | -5 por rodada | 1 |

## Dependências

### Bibliotecas Padrão
```python
import sys      # Controle do sistema (exit)
import random   # Escolha aleatória de eventos
import os       # Limpeza de tela
import time     # Pausas e delays
```

### Bibliotecas Externas
```python
from colorama import Fore, init
# Versão: >=0.4.6
# Propósito: Colorização de texto no terminal
# Cores usadas:
#   - Fore.YELLOW: Títulos e barras preenchidas
#   - Fore.GREEN: Efeitos positivos
#   - Fore.RED: Efeitos negativos
#   - Fore.WHITE: Reset/texto normal
```

## Compatibilidade

### Versões Python
- Mínimo: Python 3.6 (f-strings)
- Recomendado: Python 3.8+
- Testado: Python 3.6, 3.8, 3.9, 3.10, 3.11

### Sistemas Operacionais
- ✅ Windows 7+ (cmd, PowerShell, Windows Terminal)
- ✅ macOS 10.12+
- ✅ Linux (qualquer distribuição moderna)

### Terminais
- ✅ Windows Terminal (recomendado para Windows)
- ✅ PowerShell
- ⚠️ CMD (funciona mas cores podem não aparecer)
- ✅ Terminal do macOS
- ✅ GNOME Terminal, Konsole, xterm, etc (Linux)

## Performance

### Análise de Complexidade

| Operação | Complexidade | Notas |
|----------|--------------|-------|
| Inicialização | O(1) | Constante |
| Loop principal | O(n) | n = número de eventos (19) |
| Escolha de evento | O(n) | random.choice() em lista |
| Execução de evento | O(1) | Tempo constante |
| Verificação Game Over | O(1) | 8 comparações |
| Renderização interface | O(1) | 4 barras fixas |

### Uso de Memória

- Memória base: ~1-2 MB (interpretador Python)
- Memória do jogo: < 100 KB
  - Lista de eventos: ~19 referências de função
  - Variáveis globais: ~32 bytes
  - Stack de execução: < 1 KB

### Otimizações Possíveis

1. **Lista de eventos:**
   ```python
   # Atual: O(n) para remover
   eventos.remove(eventoX)
   
   # Otimizado: O(1) com set
   eventos_disponiveis = set([evento1, evento2, ...])
   eventos_disponiveis.discard(eventoX)
   ```

2. **Cache de strings formatadas:**
   ```python
   # Pré-computar strings de formatação
   SEPARATOR = "=" * 50
   HEADER = " " * 15 + Fore.YELLOW + "INDICADORES" + Fore.WHITE
   ```

3. **Validação de input:**
   ```python
   # Usar set para O(1) lookup
   VALID_INPUTS = {'s', 'n'}
   while decisao not in VALID_INPUTS:
       ...
   ```

## Testes

### Casos de Teste Sugeridos

#### Teste de Inicialização
```python
def test_inicializacao():
    # Verificar valores iniciais
    assert pop == 50
    assert eco == 50
    assert meio == 50
    assert tec == 50
    assert software == False
    assert seca == 0
    assert crise_hidro == 0
```

#### Teste de Barra
```python
def test_barra():
    # Valor 0
    assert barra("Teste", 0).count('#') == 0
    assert barra("Teste", 0).count('·') == 20
    
    # Valor 50
    assert barra("Teste", 50).count('#') == 10
    assert barra("Teste", 50).count('·') == 10
    
    # Valor 100
    assert barra("Teste", 100).count('#') == 20
    assert barra("Teste", 100).count('·') == 0
```

#### Teste de Game Over
```python
def test_game_over():
    # Testar cada condição
    checar_game_over(0, 50, 50, 50)  # deve chamar minPop()
    checar_game_over(100, 50, 50, 50)  # deve chamar maxPop()
    # ... etc
```

#### Teste de Evento
```python
def test_evento_basico():
    stats = (50, 50, 50, 50)
    # Simular input 's'
    new_stats = evento1(stats)
    # Verificar que stats mudaram apropriadamente
    assert new_stats != stats
    # Verificar que evento foi removido
    assert evento1 not in eventos
```

### Teste Manual

1. **Smoke Test:**
   - Execute o jogo
   - Verifique menu inicial
   - Inicie novo jogo
   - Complete 1 evento
   - Confirme que interface atualiza

2. **Teste de Balanceamento:**
   - Jogue até Game Over
   - Anote qual indicador causou Game Over
   - Repita várias vezes
   - Todos os indicadores devem ser igualmente possíveis

3. **Teste de Eventos Especiais:**
   - Encontre evento da Startup (10)
   - Aceite e complete série até ativar modo software
   - Verifique que valores numéricos aparecem

## Troubleshooting

### Problemas Comuns

#### Cores não aparecem
```python
# Solução: Verificar colorama
try:
    from colorama import Fore, init
    init()
except ImportError:
    print("Instale colorama: pip install colorama")
```

#### Caracteres especiais quebrados
```python
# Solução: Configurar encoding
import sys
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
```

#### Tela não limpa corretamente
```python
# Solução alternativa
def limpar_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\n' * 50)  # Fallback: imprimir linhas vazias
```

## Extensibilidade

### Adicionando Novo Indicador

1. Modificar tupla stats:
```python
stats = (pop, eco, meio, tec, novo)
```

2. Atualizar todas as funções que usam stats:
```python
def evento(stats):
    pop, eco, meio, tec, novo = stats
    # ...
    return pop, eco, meio, tec, novo
```

3. Adicionar barra na interface:
```python
print(barra("Novo Indicador", novo))
```

4. Adicionar condições de Game Over:
```python
if novo <= 0: minNovo()
if novo >= 100: maxNovo()
```

### Adicionando Sistema de Save/Load

```python
import json

def salvar_jogo(stats, eventos_restantes):
    save_data = {
        'stats': stats,
        'eventos': [e.__name__ for e in eventos_restantes],
        'seca': seca,
        'crise_hidro': crise_hidro,
        'software': software
    }
    with open('save.json', 'w') as f:
        json.dump(save_data, f)

def carregar_jogo():
    with open('save.json', 'r') as f:
        save_data = json.load(f)
    # Reconstituir estado
    return save_data
```

### Adicionando Sistema de Pontuação

```python
def calcular_pontuacao(eventos_completados, tempo_decorrido, equilibrio_final):
    pontos_base = eventos_completados * 100
    bonus_tempo = max(0, 1000 - tempo_decorrido)
    bonus_equilibrio = sum(abs(50 - stat) for stat in equilibrio_final)
    return pontos_base + bonus_tempo - bonus_equilibrio
```

## Referências

### Documentação Relacionada
- [README.md](../README.md) - Documentação do usuário
- [instalacao.md](instalacao.md) - Guia de instalação
- [gameplay.md](gameplay.md) - Guia de gameplay
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Guia de contribuição

### Recursos Externos
- [Python Official Docs](https://docs.python.org/3/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

**Nota:** Esta documentação técnica é destinada a desenvolvedores que desejam entender, modificar ou estender o código do jogo.
