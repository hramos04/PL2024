from datetime import date
import json
import re
import ply.lex as lex

tokens = (
    "INPUT",
    "VARIAVEL",
    "NUMERO",
    "PRINT",
    "SOMA",
    "SUBTRACAO",
    "MULTIPLICACAO",
    "DIVISAO",
    "PA",
    "PF",
    "IGUAL",
)

t_INPUT = r"\?"
t_NUMERO = r"\d+"
t_VARIAVEL = r"\w+"
t_PRINT = "!"
t_SOMA = "\+"
t_SUBTRACAO = "\-"
t_MULTIPLICACAO = "\*"
t_DIVISAO = "/"
t_PA = "\("
t_PF = "\)"
t_IGUAL = "="

t_ignore = " \t\n" 

def t_eof(t):
    r'$'
    t.value = None
    
def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

data = '''
? a
b = a * 2 /(27-3)
! a + b
c = a * b / (a/b)
'''

lexer.input(data)




