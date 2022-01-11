# Desenvolva sua classe Recipiente aqui.
class Recipiente:
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = true):
        tamanho = 0 if tamanho < 0 else tamanho
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        return true if self.conteudo == 0 else False

    def lavar(self):
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        return self.limpo
    
    def estado(self):
        return 'limpo' if self.limpo == True else 'sujo'

    def sujar(self):
        return self.limpo = False

    def __repr__(self):
        return f'não foi especificado o recipiente {self.estado()}'