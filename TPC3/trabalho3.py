import re
import sys


def contador(texto):
   
   with open(texto, "r") as texto: 
    ficheiro = texto.read()
    res = re.findall(r"(off|on|=|\d+)", ficheiro,re.I)
        
    contador = 0
    onOff= False 
    for i in res:
        if i.lower() == "off":
            onOff = False
        elif i.lower() == "on":
            onOff = True
        elif i == "=":
            print(contador)
        elif onOff:
            contador += int(i)
    

def main(argumentos):
    for linha in argumentos:
        contador(linha.strip())
        
if __name__ == "__main__":
    main(sys.argv[1:])