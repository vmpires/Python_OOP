class LogAnalysis(object):
    def __init__(self,path):
        self.path = open(path, 'r')
    def print_count(self):
        conteudo = len(self.path.readlines())
        print(f'O arquivo tem {conteudo} linhas.')