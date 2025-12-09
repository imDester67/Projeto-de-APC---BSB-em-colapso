# Guia de Gameplay - BSB em Colapso

## Conceitos Básicos

### Objetivo do Jogo

Você é o gestor de Brasília e deve completar seu mandato mantendo o equilíbrio da cidade. Para vencer, você precisa:

1. ✅ Completar todos os eventos disponíveis
2. ✅ Manter todos os indicadores entre 1 e 99
3. ❌ Se qualquer indicador chegar a 0 ou 100, é Game Over

### Os Quatro Indicadores

#### 🧑‍🤝‍🧑 População (0-100)
**Representa:** Popularidade e satisfação da população com sua gestão

**Cuidado:**
- **0**: Revolta popular - o povo pede um novo gestor
- **100**: Popularidade extrema - você é assassinado em público

**Dicas:**
- Decisões populistas aumentam população mas podem custar economia
- Ignore totalmente a população e haverá protestos
- Muito popular também é perigoso!

#### 💰 Economia (0-100)
**Representa:** Saúde financeira dos cofres públicos

**Cuidado:**
- **0**: Cidade mais pobre do Brasil - Game Over
- **100**: Dinheiro demais atrai investigação por corrupção

**Dicas:**
- Investimentos custam dinheiro mas trazem benefícios
- Economizar demais pode prejudicar outros indicadores
- Arrecadação excessiva gera descontentamento

#### 🖥️ Tecnologia (0-100)
**Representa:** Nível de desenvolvimento tecnológico

**Cuidado:**
- **0**: Cidade considerada a mais mal desenvolvida do Brasil
- **100**: BigTechs dominam completamente a cidade

**Dicas:**
- Tecnologia ajuda em várias crises
- Muito desenvolvimento tecnológico pode ter custos ambientais
- Ignorar tecnologia te deixa vulnerável a problemas modernos

#### 🌳 Meio Ambiente (0-100)
**Representa:** Qualidade ambiental e sustentabilidade

**Cuidado:**
- **0**: Cidade em chamas - desastre ambiental total
- **100**: Capivaras tomam o poder (sim, é sério!)

**Dicas:**
- Projetos ambientais geralmente custam economia
- Ignorar o meio ambiente causa crises a longo prazo
- Muito foco ambiental pode prejudicar desenvolvimento

## Mecânicas de Jogo

### Sistema de Eventos

#### Estrutura dos Eventos

Cada rodada apresenta um evento com:

1. **Contexto narrativo**: Situação que está acontecendo
2. **Duas opções**: Aceitar (s) ou Recusar (n)
3. **Consequências**: Efeitos em múltiplos indicadores

#### Lendo os Efeitos

Os efeitos são apresentados com cores:

```
Efeitos se aceitar:
- População: +15          [VERDE - Positivo] +
- Economia: -20           [VERMELHO - Negativo] -

Efeitos se recusar:
- Tecnologia: +10         [VERDE - Positivo] +
- Meio Ambiente: -5       [VERMELHO - Negativo] -
```

### Tipos de Eventos

#### 1. Eventos Simples

Decisões únicas com consequências imediatas.

**Exemplo:** Wi-Fi público em áreas carentes
- Aceitar: +Tecnologia, -Economia
- Recusar: Sem mudanças

#### 2. Eventos em Cadeia

Suas decisões desencadeiam novos eventos relacionados.

**Exemplo - Série do Supercomputador:**
1. OpenAI propõe construir supercomputador
   - Aceitar → Próximo evento
   - Recusar → Série termina
2. Problemas de superaquecimento
   - Aceitar investigar → Próximo evento
   - Ignorar → Série termina
3. Incêndio nas instalações
   - Consequências finais da série

#### 3. Eventos de Longa Duração

Crises que persistem por várias rodadas.

**Seca** (4 rodadas):
- Meio Ambiente -5 por rodada
- Aparece aviso a cada rodada
- Pode ser prevenida por decisões anteriores

**Crise Hídrica** (3 rodadas):
- População -5 por rodada
- Efeito cumulativo
- Pode ser ativada ou prevenida por eventos

#### 4. Eventos Recursivos

Alguns eventos podem retornar se você não resolver o problema.

**Exemplo:** Vazamento de dados por hackers
- Se você não melhorar a segurança, eles voltam
- Podem culminar em um cyber ataque devastador

### Modo Software

**Como desbloquear:** Apoiar startup local (Evento 10) e aceitar usar o software (Evento 10A)

**Benefício:** Mostra valores numéricos exatos ao lado das barras

**Antes:**
```
População     : [##########··········]
```

**Depois:**
```
População     : [##########··········] 50
```

## Estratégias de Jogo

### Para Iniciantes

1. **Equilibre suas escolhas**: Não foque apenas em um indicador
2. **Leia com atenção**: Os efeitos mostram exatamente o que vai acontecer
3. **Pense no longo prazo**: Algumas escolhas têm consequências posteriores
4. **Mantenha margem de segurança**: Não deixe nenhum indicador muito próximo de 0 ou 100

### Estratégias Avançadas

#### Técnica do Equilíbrio Dinâmico
- Monitore qual indicador está mais alto/baixo
- Priorize equilibrar os extremos
- Aceite perdas temporárias para ganhos maiores

#### Técnica da Prevenção
- Algumas escolhas previnem crises futuras
- Vale a pena o custo imediato para evitar eventos negativos
- Especialmente importante para seca e crise hídrica

#### Técnica da Cadeia Positiva
- Identifique séries de eventos benéficos
- Startup → Software → Prevenção de crises
- Invista no começo para colher benefícios depois

### Armadilhas Comuns

❌ **Focar demais em um indicador**
- Resultado: Outros indicadores ficam críticos

❌ **Ignorar eventos de longa duração**
- Resultado: Perda gradual que pode ser fatal

❌ **Aceitar tudo ou recusar tudo**
- Resultado: Desbalanceamento extremo

❌ **Não considerar eventos em cadeia**
- Resultado: Você se compromete com uma série ruim

## Exemplos de Jogadas

### Situação 1: Indicadores Equilibrados

```
População     : [##########··········] 50
Economia      : [##########··········] 50
Tecnologia    : [##########··········] 50
Meio-Ambiente : [##########··········] 50
```

**Evento:** Substituir frota por ônibus elétricos
- Aceitar: Meio +25, Eco -20
- Recusar: Tec +10, Pop -5

**Análise:** Todos estão em 50, então temos flexibilidade.
**Decisão recomendada:** Aceitar! Meio ambiente sobe bastante e ainda temos economia para gastar.

### Situação 2: Economia Baixa

```
População     : [##############······] 70
Economia      : [####················] 20
Tecnologia    : [###########·········] 55
Meio-Ambiente : [#########···········] 45
```

**Evento:** Investir em Wi-Fi público
- Aceitar: Tec +15, Eco -15
- Recusar: Pop -10

**Análise:** Economia já está baixa (20). Perder mais 15 seria crítico.
**Decisão recomendada:** Recusar. População está alta, pode absorver -10.

### Situação 3: Meio Ambiente Crítico

```
População     : [##########··········] 50
Economia      : [##############······] 70
Tecnologia    : [########············] 40
Meio-Ambiente : [##··················] 10
```

**Evento:** Construir usina de energia
- Aceitar: Eco +25, Meio -15
- Recusar: Pop -10, Tec -5

**Análise:** Meio ambiente está CRÍTICO em 10! Perder 15 = Game Over!
**Decisão recomendada:** RECUSAR! Mesmo perdendo população e tecnologia, é melhor que perder o jogo.

## Dicas de Veteranos

1. 🎯 **Priorize indicadores abaixo de 20 ou acima de 80** - Estes estão na zona de perigo
2. 🔄 **Considere o efeito líquido** - Às vezes perder em 2 indicadores para ganhar muito em 1 vale a pena
3. 📊 **Use o Modo Software** - Números exatos ajudam muito no planejamento
4. 🎲 **Salve mentalmente boas configurações** - Se estiver tudo equilibrado, anote ou lembre-se
5. 🎭 **Aprecie a narrativa** - O jogo tem histórias interessantes, não é só matemática!

## Cenários de Vitória

Para vencer, você precisa passar por todos os eventos. A ordem é aleatória, então cada partida é única!

**Sinais de que você está perto da vitória:**
- Poucos eventos restantes
- Indicadores equilibrados
- Sem eventos de longa duração ativos

**Mensagem de vitória:**
Quando completar todos os eventos com sucesso, você verá uma mensagem de parabéns!

## Pratique!

A melhor forma de aprender é jogando. Cada partida ensina algo novo sobre balanceamento e estratégia. Não desanime com Game Overs - eles fazem parte do aprendizado!

Boa sorte, Gestor! Brasília conta com você! 🏛️🇧🇷

---

**Veja também:**
- [README principal](../README.md)
- [Documentação técnica](../DOCUMENTATION.md)
