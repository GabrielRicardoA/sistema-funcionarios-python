from models.funcionario import Funcionario

class CLT(Funcionario):
    def __init__(self, nome,salario):
        super().__init__(nome)

        self.salario = salario

    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return f"{self.nome} (CLT) - Salario: {self.calcular_salario()}"
    
    def to_dict(self):
        """
        Converte o objeto para um dicionário para salvar em JSON.
        """
        return {

        "tipo" : "CLT",
        "nome" :  self.nome,
        "salario" : self.salario

    }


    

