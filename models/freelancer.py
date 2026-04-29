from models.funcionario import Funcionario

class Freelancer(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)

        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas

    def __str__(self):
        return f"{self.nome} (Freelancer) - Salário: {self.calcular_salario()}"
    
    def to_dict(self):
        """
        Converte o objeto para um dicionário para salvar em JSON.
        """
        return {

            "tipo" : "Freelancer",
            "nome" : self.nome,
            "horas_trabalhadas": self.horas_trabalhadas,
            "valor_da_hora" : self.valor_hora
            

        }

        