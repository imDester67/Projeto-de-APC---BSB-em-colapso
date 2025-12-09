# Guia de Contribuição

Obrigado por considerar contribuir para o projeto **BSB em Colapso**! 🎉

## Como Contribuir

### Reportando Bugs

Se você encontrou um bug, por favor:

1. Verifique se o bug já não foi reportado nas [Issues](https://github.com/bielperes/APC-BSB-em-colapso/issues)
2. Abra uma nova issue incluindo:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. comportamento atual
   - Versão do Python utilizada
   - Sistema operacional

### Sugerindo Melhorias

Sugestões de novas funcionalidades são bem-vindas! Abra uma issue com:

- Descrição clara da funcionalidade
- Justificativa de por que seria útil
- Exemplos de uso, se possível

### Pull Requests

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Padrões de Código

- Use nomes de variáveis descritivos em português (conforme padrão do projeto)
- Adicione comentários para lógicas complexas
- Mantenha a consistência com o estilo de código existente
- Teste suas alterações antes de submeter

### Adicionando Novos Eventos

Para adicionar um novo evento ao jogo:

1. Siga a estrutura padrão de eventos (veja exemplos no código)
2. Balanceie os efeitos nos indicadores (tipicamente ±10 a ±35 pontos)
3. Escreva narrativas interessantes e coerentes com o tema
4. Use `print_event()` para exibir efeitos com cores
5. Adicione o evento à lista de eventos disponíveis
6. Teste o evento em diferentes cenários

### Estrutura de um Evento

```python
def eventoX(stats):
    pop, eco, meio, tec = stats
    
    print("Título do Evento")
    print("=" * 50)
    print("Descrição da situação...")
    print_event('''
        Efeitos se aceitar:
        - Indicador1: +valor +
        - Indicador2: -valor -
        
        Efeitos se recusar:
        - Indicador3: +valor +
        - Indicador4: -valor -
    ''')
    
    while True:
        decisao = input('\nDigite "s" ou "n": ').lower()
        if decisao in ['s', 'n']:
            break
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
    
    eventos.remove(eventoX)
    
    if decisao == 's':
        # Aplicar efeitos da aceitação
        pop += valor1
        eco -= valor2
    else:
        # Aplicar efeitos da recusa
        tec += valor3
        meio -= valor4
    
    return pop, eco, meio, tec
```

## Código de Conduta

Este é um projeto educacional. Mantenha um ambiente respeitoso e construtivo para todos os contribuidores.

## Dúvidas?

Sinta-se à vontade para abrir uma issue com suas dúvidas ou entrar em contato com os desenvolvedores.

---

Agradecemos sua contribuição! 🚀
