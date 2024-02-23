import re
import sys


def markDownToHTML(res):
    
    #h1
    res = re.sub(r"^# (.+)$", r"<h1>\1</h1>", res, flags = re.MULTILINE) 
    #h2
    res = re.sub(r"^## (.+)$", r"<h2>\1</h2>", res, flags = re.MULTILINE)
    #h3
    res = re.sub(r"^### (.+)$", r"<h3>\1</h3>", res, flags = re.MULTILINE)
    
    #bold
    res = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", res)
    
    #italico
    res = re.sub(r"\*(.+?)\*", r"<i>\1</i>", res)
    
    #lista numerada
    res = re.sub(r"^[0-9]+\.(.+)$", r"<li>\1</li>", res, flags = re.MULTILINE)
    res = re.sub(r"((<li>.+</li>\n)+)", r"<ol>\n\1</ol>\n", res, flags = re.MULTILINE)
    
    #imagem
    res = re.sub(r"^!\[(.+)\]\((.+)\)$",r"<img src='\2' alt='\1'/>", res, flags = re.MULTILINE)
    
    #link
    res = re.sub(r"^\[(.+)\]\((.+)\)$",r"<a href = '\2'> \1</a>", res, flags = re.MULTILINE)
    
    
    
    return res
    
def main(argumentos):
    html = ""
    with open(argumentos[1]) as ficheiro:
        html += markDownToHTML(ficheiro.read())
        
    with open("paginaHtml.html", "w") as ficheiro:
        ficheiro.write(html)
    
    
if __name__ == "__main__":
    main(sys.argv)