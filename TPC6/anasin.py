from analex import lexer

prox_simb = ("Erro","",0,0)

def parserError(s):
    print(f"Erro sintático:{s} ")

def rec_term(simbolo):
    global prox_simb
    if prox_simb.type == simbolo:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        
def rec_Conta():
    global prox_simb
    if prox_simb.type == "VARIAVEL":
        rec_term("VARIAVEL")
        rec_Operacao()
        print("Reconheci p4: Conta--->VARIAVEL Operacao")
    elif prox_simb.type == "NUMERO":
        rec_term("NUMERO")
        rec_Operacao()
        print("Reconheci p5: Conta--->NUMERO Operacao")
    elif prox_simb.type == "PA":
        rec_term("PA")
        rec_Conta()
        rec_term("PF")
        print("Reconheci p6: Conta--->'(' Conta ')'")
    else:
        parserError(prox_simb)
        

def rec_Operacao():
    if prox_simb.type == "SOMA":
        rec_term("SOMA")
        rec_Conta()
        print("Reconheci p7: Operacao--->'+' Conta")
    elif prox_simb.type == "SUBTRACAO":
        rec_term("SUBTRACAO")
        rec_Conta()
        print("Reconheci p8: Operacao--->'-' Conta")
    elif prox_simb.type == "MULTIPLICACAO":
        rec_term("MULTIPLICACAO")
        rec_Conta()
        print("Reconheci p9: Operacao--->'*' Conta")
    elif prox_simb.type == "DIVISAO":
        rec_term("DIVISAO")
        rec_Conta()
        print("Reconheci p10: Operacao--->'/' Conta")
    elif prox_simb.type == "PF" or prox_simb.type == "eof":
        print("Reconheci p11: Operacao---> &")
    else:
        parserError(prox_simb)
        
def rec_Inicio():
    global prox_simb
    if prox_simb.type == "INPUT":
        rec_term("INPUT")
        rec_term("VARIAVEL")
        print("Reconheci p1: Inicio--->'?' VARIAVEL")
    elif prox_simb.type == "VARIAVEL":
        rec_term("VARIAVEL")
        rec_term("IGUAL")
        rec_Conta()
        print("Reconheci p2: Inicio--->VARIAVEL '=' Conta")
    elif prox_simb.type == "PRINT":
        rec_term("PRINT")
        rec_Conta()
        print("Reconheci p3: Inicio--->'!' Conta")

    else:
        parserError(prox_simb)
    
   
def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Inicio()
    print("Análise sintática concluída com sucesso")


rec_Parser('''
b = a * 2 /(27-3)
''')