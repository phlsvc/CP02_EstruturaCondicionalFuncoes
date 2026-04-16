#criacao das funcoes
def calcular_horas_extras(salario, horasExtra):
    return salario*(horasExtra*0.015)

def calcular_descontos_faltas(salario, faltas):
    return salario*(faltas*0.02)

def calcular_bonus(bonus,cargo):
    if bonus=="s":
        match cargo:
            case "1":
                return 1000
            case "2":
                return 500
            case "3":
                return 300
            case "4":
                return 100
            case _:
                print("Codigo de cargo invalido")
                return 0
    elif bonus=="n":
        print("Voce nao recebeu o bonus")
        return 0

#Recebimento de dados
nome=input("Digite seu nome: ")
cargo=input("Digite seu cargo (1 a 4): ")
salario=float(input("Digite seu salario base: "))
horasExtra=int(input("Digite o total das suas horas extra trabalhadas: "))
faltas=int(input("Digite o total de faltas no mes: "))
bonus=input("Voce recebeu bonus (s ou n): ")

print(f"Salario bruto:{salario}")
acrescimos=calcular_horas_extras(salario,horasExtra)+calcular_bonus(bonus,cargo)
print(f"Total de acrescimo:{acrescimos}")
print(f"Total de descontos:{calcular_descontos_faltas(salario,faltas)}")
print(f"Salario bruto:{salario+acrescimos-calcular_descontos_faltas(salario,faltas)}")
