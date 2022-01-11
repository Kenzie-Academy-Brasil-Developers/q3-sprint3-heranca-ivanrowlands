# Desenvolva sua classe Copo aqui.
from .recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True, bebida = None):
        super().__init__(tamanho, conteudo=conteudo, limpo=limpo)
        self.bebida = bebida

    def encher(self, bebida: str = 'água'):
        if self.limpo == False:
            return 'Não se pode encher um copo sujo'

        else:
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida
        
    def beber(self, quantidade: float):
        if quantidade < 0:
            return 'Quantidade deve ser positiva'
        
        if quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        
        else:
            self.conteudo = self.conteudo - quantidade
    
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self) -> str:
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo == 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
    
    def __str__(self) -> str:
        return f'Um copo vazio de {float(self.tamanho)}ml' if self.conteudo == 0 else f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'