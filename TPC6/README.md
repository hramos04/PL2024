# TPC6: Analisador sintático

## Aluno

**Nome:** Hugo António Gomes Ramos

**Número:** A100644

## Resumo
O objetivo deste tpc é fazer um analisador léxico e um analisador sintático capaz de reconhecer a seguinte expressão criando uma gramática.

```
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a / b)
```

## Resolução
Para a resolucao deste TPC, num script em python, foi criado um analisador léxico e noutro script em python foi criado um analisador léxico. Também criei a seguinte gramática para aplicar nos analisadores criados.

```
Inicio -> '?' VARIAVEL
        | VARIAVEL '=' Conta
        | '!' Conta

Conta -> VARIAVEL Operacao
        | NUMERO Operacao
        | '(' Conta ')'

Operacao -> '+' Conta
        | '-' Conta
        | '*' Conta
        | '/' Conta
        | &
```