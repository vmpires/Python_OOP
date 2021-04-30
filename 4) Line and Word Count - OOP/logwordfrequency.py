from loganalysis import LogAnalysis
from collections import Counter

class LogWordFrequency(LogAnalysis):

    def print_word_frequency(self):
        arquivo = open(self.path, 'r')
        conteudo = arquivo.read()
        conteudo = conteudo.replace('\n',' ')
        listaconteudo = []
        for line in conteudo.split():
            listaconteudo.append(line)
            conteudo = Counter(listaconteudo).most_common(10)
        print(conteudo)