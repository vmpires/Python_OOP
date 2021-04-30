class LogAnalysis(object):
    def __init__(self,path):
        self.path = path
    def print_count(self):
        arquivo = open(self.path, 'r')
        conteudo = len(arquivo.readlines())
        print(f'O arquivo tem {conteudo} linhas.')