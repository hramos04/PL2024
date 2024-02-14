import sys

def listaModalidades(dados):
    listaModalidades = set()
       
    for linha in dados.values():
        listaModalidades.add(linha[1])
        
        
    return sorted(listaModalidades,key=lambda x: x.lower())


def atletasAptos(dados): 
    atletasAptos = 0
    
    for linha in dados.values():
        if linha[2] == "true\n":
            atletasAptos += 1
                         
    return atletasAptos

    

def main():
    
    dados = {}
    input()
    for linha in sys.stdin:
        split = linha.split(",")
        dados[split[0]] = [split[5],split[8],split[12]]
    
    print(f"Lista modalidades: {listaModalidades(dados)}")
    aptos = atletasAptos(dados)
    total = len(dados)
    percentagemAptos = aptos/total*100
    print(f"Percentagem atletas aptos: {percentagemAptos:.2f}%")
    print(f"Percentagem atletas nao aptos: {100-percentagemAptos:.2f}%")
    
    
if __name__ == "__main__":  
    main()
    