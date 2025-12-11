# Guia de Instalação - BSB em Colapso

## Requisitos do Sistema

### Sistema Operacional
- Windows 7 ou superior
- macOS 10.12 ou superior
- Linux (qualquer distribuição moderna)

### Software Necessário
- Python 3.6 ou superior

## Instalação Passo a Passo

### 1. Verificar Instalação do Python

Antes de começar, verifique se você tem o Python instalado:

```bash
python --version
# ou
python3 --version
```

Se não tiver o Python instalado, baixe em: https://www.python.org/downloads/

### 2. Clonar o Repositório

#### Opção A: Usando Git
```bash
git clone https://github.com/bielperes/APC-BSB-em-colapso.git
cd APC-BSB-em-colapso
```

#### Opção B: Download ZIP
1. Acesse https://github.com/bielperes/APC-BSB-em-colapso
2. Clique em "Code" > "Download ZIP"
3. Extraia o arquivo ZIP
4. Navegue até a pasta extraída no terminal

### 3. Criar Ambiente Virtual (Opcional, mas Recomendado)

#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### No macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o Jogo

```bash
python logica_brasilia.py
```

Ou no macOS/Linux:
```bash
python3 logica_brasilia.py
```

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'colorama'"

**Solução:** Instale a biblioteca colorama:
```bash
pip install colorama
```

### Erro: "python não é reconhecido como comando"

**Solução:** 
- No Windows: Adicione Python ao PATH durante a instalação
- No macOS/Linux: Use `python3` em vez de `python`

### Cores não aparecem no terminal

**Solução:**
- **Windows**: Use o Windows Terminal ou PowerShell (não o CMD antigo)
- **macOS/Linux**: A maioria dos terminais modernos suporta cores
- Alternativamente, o jogo ainda funciona sem cores, apenas a visualização fica menos atraente

### Caracteres especiais não aparecem corretamente

**Solução:**
- Certifique-se de que seu terminal está usando encoding UTF-8
- No Windows, execute: `chcp 65001` antes de rodar o jogo

## Verificação da Instalação

Para verificar se tudo está funcionando corretamente:

1. Execute o jogo
2. Você deve ver o menu inicial com a arte ASCII de Brasília
3. As cores devem aparecer (amarelo para título, verde/vermelho para efeitos)
4. Escolha a opção 1 para iniciar o jogo
5. Você deve ver os 4 indicadores com barras visuais

Se tudo aparecer corretamente, a instalação foi bem-sucedida! 🎉

## Desinstalação

Para remover o jogo:

1. Desative o ambiente virtual (se estiver usando):
```bash
deactivate
```

2. Delete a pasta do projeto:
```bash
cd ..
rm -rf APC-BSB-em-colapso  # macOS/Linux
# ou
rmdir /s APC-BSB-em-colapso  # Windows
```

## Atualizações

Para atualizar o jogo para a versão mais recente:

```bash
cd APC-BSB-em-colapso
git pull origin main
pip install -r requirements.txt --upgrade
```

## Suporte

Se você encontrar problemas durante a instalação:

1. Verifique se está usando Python 3.6+
2. Tente reinstalar as dependências
3. Abra uma issue no GitHub com detalhes do problema
4. Inclua a saída de `python --version` e seu sistema operacional

---

**Próximos Passos:** Veja o [Guia de Gameplay](gameplay.md) para aprender a jogar!
