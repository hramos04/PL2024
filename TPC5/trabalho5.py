from datetime import date
import json
import re
import ply.lex as lex

tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SAIR",
)

t_LISTAR = "Listar"

def t_MOEDA(t):
    r"Moeda\s+(1e|10c|20c)"
    moedas = re.findall(r"(1e|10c|20c)", t.value)
    if moedas:
      t.value = moedas
    else:
      print("Moeda inválida")
    return t 
  
def t_SELECIONAR(t):
    r"Selecionar\s+[0-9]+"
    t.value = int(t.value.split()[1])
    return t
  
t_SAIR = "Sair"

t_ignore = " \t\n" 

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()

def mostrarStock(data):
    dados = json.loads(data)
    stock = dados["stock"]  
    cabecalho = ["ID", "Nome", "Quantidade", "Preço"]

    print("{:<5} {:<20} {:<20} {:<10}".format(*cabecalho))
    
    for produto in stock:
        print("{:<5} {:<20} {:<20} {:<10}".format(
            produto['id'], produto['nome'], produto['quantidade'], produto['preco']
        ))
        
def mostrarSaldo(data):
  total = 0
  for moeda in data:
    valor, tipo = moeda[:-1], moeda[-1]
    if tipo == "e":
      total += int(valor) 
    elif tipo == "c":
      total += int(valor)/100
  return total
  
  
def selecionarProduto(selecionado, saldo):
  if selecionado in range(1, len(json.loads(data)["stock"]) + 1):
    produto = json.loads(data)["stock"][selecionado - 1]
    preco = produto['preco']
    if saldo >= preco and produto['quantidade'] > 0:
        print("Aqui tem o seu produto.")
        produto['quantidade'] -= 1
        saldo -= preco
        print(f"Saldo: {saldo:.2f}€")
    else:
      if saldo < preco:
        print("Saldo insuficiente.")
      else:
        print("Produto esgotado.")
  else:
      print("Produto selecionado inválido.")
      
  return saldo
   
def main():
    print("Bem-vindo à máquina de vending do Ramos.\n")
    saldo = 0

    while True:
        comando = input("Inserir comando: ")
        lexer.input(comando)
        tok = lexer.token()
        
        while tok:
            if tok.type == "LISTAR":
              mostrarStock(data)
              break
            elif tok.type == "MOEDA":
              saldo += mostrarSaldo(tok.value)
              print(f"Saldo: {saldo:.2f} €")
              break
            elif tok.type == "SELECIONAR":
              selecionado = tok.value
              saldo = selecionarProduto(selecionado, saldo)
              break
            elif tok.type == "SAIR": 
              print(f"Aqui está o seu troco de {saldo:.2f}€. Até à próxima.")
              saldo = 0
              break
              
            else:
                print(tok)
            
            tok = lexer.token()  
        if not tok:
            print("Comando não reconhecido\n")
        print()
        
if __name__ == "__main__":
    data = '''{
      "stock": [
        {
          "id": "1",
          "nome": "sumo",
          "quantidade": 3,
          "preco": 0.45
        },
        {
          "id": "2",
          "nome": "bolachas",
          "quantidade": 4,
          "preco": 0.60
        },
        {
          "id": "3",
          "nome": "bolo chocolate",
          "quantidade": 5,
          "preco": 1.20
        },
        {
          "id": "4",
          "nome": "agua",
          "quantidade": 2,
          "preco": 0.85
        }
      ]
    }'''
    main()