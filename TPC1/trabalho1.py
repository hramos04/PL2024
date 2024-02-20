import sys

def listaModalidades(dados):
    listaModalidades = set()
       
    for linha in dados.values():
        listaModalidades.add(linha[1])
        
    return sorted(listaModalidades, key=lambda x: x.lower())


def atletasAptos(dados): 
    atletasAptos = 0
    
    for linha in dados.values():
        if linha[2] == "true\n":
            atletasAptos += 1
                         
    return atletasAptos


def distribuirPorIdades(dados):
    escaloes = {"0-5": 0, "6-10": 0, "11-15": 0, "16-20": 0, "21-25": 0, "26-30": 0, "31-35": 0, "36-40": 0, "41-45": 0}
    
    for linha in dados.values():
        idade = int(linha[0])
        for intervalo in escaloes:
            inicio, fim = map(int, intervalo.split("-"))
            if inicio <= idade <= fim:
                escaloes[intervalo] += 1
                break
    
    return escaloes


def main():
    
    dados = {}
    input()
    for linha in sys.stdin:
        split = linha.split(",")
        dados[split[0]] = [split[5], split[8], split[12]]
    
    print(f"Lista modalidades: {listaModalidades(dados)}")
    
    aptos = atletasAptos(dados)
    total = len(dados)
    percentagemAptos = aptos / total * 100
    print(f"Percentagem atletas aptos: {percentagemAptos:.2f}%")
    print(f"Percentagem atletas nao aptos: {100 - percentagemAptos:.2f}%")
    
    distribuicao = distribuirPorIdades(dados)
    print("Distribuição por escalão etário:")
    for intervalo, totalAtletas in distribuicao.items():
        print(f"{intervalo}: {totalAtletas} atletas")
    

if __name__ == "__main__":  
    main()