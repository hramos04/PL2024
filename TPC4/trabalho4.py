import ply.lex as lex

tokens = (
    "SELECT",
    "VARIABLE",
    "COMMA",
    "FROM",
    "WHERE",
    "LESS",
    "LESS_EQUALS",
    "GREATER",
    "GREATER_EQUALS",
    "EQUALS",
    "NUMBER",  
)


t_SELECT = r"Select"
t_VARIABLE = r"\w+"
t_COMMA= r","
t_FROM = r"From"
t_WHERE = r"Where"
t_LESS = r"<"
t_LESS_EQUALS = r"<="
t_GREATER = r">"
t_GREATER_EQUALS = r">="
t_EQUALS = r"="


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ignore = " \t\n" 

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()

data = '''
Select id, nome, salario 
From empregados 
Where salario >= 820
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)


