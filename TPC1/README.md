# TPC1: Análise de um dataset

## Aluno

**Nome:** Hugo António Gomes Ramos

**Número:** A100644

## Resumo
O objetivo deste tpc é fazer parsing dos dados de um ficheiro **.csv** e com os dados fazer os seguintes exercícios:

- Lista ordenada alfabeticamente das modalidades desportivas;
- Percentagens de atletas aptos e inaptos para a prática desportiva;
- Distribuição de atletas por escalão etário.

## Resolução
Para a resolução deste TPC, num script em python, comecei por guardar todos os dados lidos do csv num dicionário e foram criadas funções auxiliares. A função listaModalidades tem como objetivo organizar a lista com todas as modalidades por ordem alfabética, sem haver repetidos. A função atletasAptos vê no dicionário quais os atletas aptos e retorna o número total de atletas com o campo "resultado" do csv a true. Por último, a função distribuirPorIdades cria vários intervalos de idades de 5 anos e distribui os atletas pelo respetivo intervalo conforme a sua idade.