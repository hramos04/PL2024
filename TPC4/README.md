# TPC4: Analisador léxico

## Aluno

**Nome:** Hugo António Gomes Ramos

**Número:** A100644

## Resumo
O objetivo deste tpc é fazer um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

  **Select id, nome, salario\
    From empregados\
    Where salario >= 820**

## Resolução
Para a resolucao deste TPC, num script em python, foi criada uma lista com todos os tokens necessários que de seguida são definidos através de expressões regulares para reconhecer os tokens durante o processo de tokenização e de seguida são retornados na consola todos os tokens.