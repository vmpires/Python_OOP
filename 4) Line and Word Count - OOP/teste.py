from collections import Counter

arquivo = open('log.txt', 'r')
conteudo = arquivo.read()
conteudo = conteudo.replace('\n',' ')
listaconteudo = []
for line in conteudo.split():
    listaconteudo.append(line)
    listaconteudo.sort
    contagem = Counter(listaconteudo).most_common(10)
print (conteudo)
