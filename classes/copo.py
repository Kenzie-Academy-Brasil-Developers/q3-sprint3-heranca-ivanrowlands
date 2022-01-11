# Desenvolva sua classe Copo aqui.
from .recipiente import recipiente

class Copo(Recipiente):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.bebida = None
    
    def encher(self, bebida: str="água"):
        if not self.limpo:
            return "não se enche um copo sujo"
        self.sujar()
        self.conteudo = self.tamanho
        self.bebida = bebida

    def beber(self, quantidade: float):
        if quantidade < 0:
            return "A quantidade não pode ser menor que 0"
        if quantidade > self.conteudo:
            return "Da para encher mais o copo!"
        self.conteudo = self.conteudo - quantidade
    
    def lavar(self):
        self.limpo = true
        self.conteudo = 0
        self.bebida = None
    
    def __repr__(self):
        return f"Um copo de {float(self.tamanho)}ml vazio." if self.conteudo <= 0 else f"um copo de {float(self.conteudo)}ml de {self.bebida} no copo de {float(self.tamanho)}ml"