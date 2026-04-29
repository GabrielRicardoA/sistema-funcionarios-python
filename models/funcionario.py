
from abc import ABC,abstractmethod


class Funcionario(ABC):

    """
    Classe base abstrata para funcionários.
    Define estrutura obrigatória.
    """

    def __init__(self,nome):
        
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}"

    @abstractmethod

    def calcular_salario(self):
        pass

    @abstractmethod
    def to_dict(self): 
        """
        Converte o objeto para um dicionário (usado para salvar em JSON).
        """
        pass




