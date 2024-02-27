# TPC2: Conversor de MarkDown para HTML

## Aluno

**Nome:** Hugo António Gomes Ramos

**Número:** A100644

## Resumo
O objetivo deste tpc é fazer um somador On/Off capaz de fazer o seguinte:

- Somar todas as sequências de digitos que encontre num texto;
- Quando aparecer a string "Off", as sequências de dígitos deixam de ser somadas;
- Quando aparecer a string "On", as sequências de dígitos voltam a ser somadas;
- Quando aparecer o carater “=”, é retornado o valor total da soma dos dígitos até ao momento.

## Resolução
Para a resolucao deste TPC, num script em python, foi criada a função contador que percorre, através do método findall, todo o texto passado como input e guarda numa lista todas as ocorrências que aparecem no texto e que estão definidas na expressão regular. Após isso, cada elemento da lista vai ser iterado e se for = "on", vão ser somados todos os dígitos que aparecerem até aparecer um elemento que seja ="off" que colocará a flag "onOff" a falso e os dígitos que aparecerem não vão ser somados. Cada vez cada aparecer o carater "=", é feito um print no terminal do valor atual do contador.