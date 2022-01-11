# Desenvolva sua classe Recipiente aqui.
class Recipiente:
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True):
        tamanho = 0 if tamanho < 0 else tamanho
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        return True if self.conteudo == 0 else False
    
    def lavar(self):
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        return self.limpo
    
    def estado(self):
        return 'limpo' if self.limpo == True else 'sujo'
    
    def sujar(self):
        self.limpo = False
    
    def __repr__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado'