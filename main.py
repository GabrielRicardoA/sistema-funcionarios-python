from models.funcionario import Funcionario
from models.clt import CLT
from models.freelancer import Freelancer
import json

def salvar_dados(funcionarios):
    """
    Salva a lista de funcionários em um arquivo JSON.
    Converte cada objeto para dicionário antes de salvar.
    """

    dados = []  # Lista que vai armazenar os dados já convertidos (dicionários)

    for f in funcionarios:
        # Cada objeto (CLT ou Freelancer) se transforma em dicionário
        # usando o método to_dict() (polimorfismo)

        dados.append(f.to_dict()) 
        # Executa o método to_dict() de cada funcionário,
        # convertendo o objeto em dicionário e adicionando na lista


    with open("funcionarios.json", "w") as arquivo:
        # Salva a lista de dicionários no arquivo em formato JSON
        # indent=4 deixa o arquivo mais organizado 
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    """
    Funcao para carregar dados já exitentes
    """
    try:
        with open('funcionarios.json',"r") as arquivo: #abre o arquivo para leitura
            dados = json.load(arquivo) #a variavel dados recebe tudo que tem no arquivo

        funcionarios = []

        for item in dados: #percorre cada item de dados

            if item["tipo"]== "CLT":#se ["tipo"] == CLT ele vai guardar o nome e salario na lista abaixo
                funcionarios.append(CLT(item["nome"], item["salario"]))

            elif item["tipo"] == "Freelancer":#mesmo mecanismo do CLT so que com Freelancer

                funcionarios.append(Freelancer(item["nome"],item["horas_trabalhadas"],item["valor_da_hora"]))

        return funcionarios #retorna o funcionarios

    except FileNotFoundError: #caso o arquivo nao exista
        return []


funcionarios = carregar_dados()

while True:
    print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
    print("1 - Adicionar CLT")
    print("2 - Adicionar Freelancer")
    print("3 - Listar funcionários")
    print("4 - Folha salarial total")
    print("5 - Remover funcionário")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")

        try:
            salario = float(input("Salario: "))


        except ValueError:
            print("Salário inválido! Digite um número.")

            continue
        
    
        funcionarios.append(CLT(nome,salario))

    elif opcao == "2":

        nome = input("Nome: ")
        try:
            qntd_horas = int(input("Quantas horas você trabalhou: "))
            valor_hora = float(input("O valor da hora trabalhada: "))

        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue


        funcionarios.append(Freelancer(nome,qntd_horas,valor_hora))

    elif opcao == "3":
        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")

        else:

            for f in funcionarios:
                print(f)


    elif opcao == "4":
        total = 0

        for f in funcionarios:
            total += f.calcular_salario()

        print(f"\nFolha salarial total: {total}")

    elif opcao == "5":

        if len(funcionarios) == 0:
            print("Nenhum funcionário para remover.")
            continue

        for i, f in enumerate(funcionarios):
            print(f"{i} - {f}")

        try:
            indice = int(input("Escolha o índice: "))
            removido = funcionarios.pop(indice)
            print(f"{removido.nome} removido!")

        except (ValueError, IndexError):
            print("Índice inválido!")

    elif opcao == "0":
        salvar_dados(funcionarios)
        print("Salvando os dados")
        print("Saindo...")
        break