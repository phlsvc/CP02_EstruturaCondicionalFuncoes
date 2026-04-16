nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
valor = float(input("Digite seu valor desejado do emprestimo: "))
num= int(input("Digite o numero de parcelas(3 a 24)): "))

def pode_aprovar(idade, renda, valor):
    if idade >= 18:
        if valor >= (renda * 20):
            print("Emprestimo aprovado")
        else:
            print("Emprestimo negado por: Valor desejado nao correspode a no minimo 20 vezes a renda mensal")
    else:
        print("Emprestimo negado por: idade invalida")

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif num <= 12:
        return 0.08
    elif num <= 24:
        return 0.1

def calcular_parcelas(valor,taxas,parcelas):
    return  valor * ((taxas * ((1 + taxas) ** parcelas)) / (((1 + taxas) ** parcelas) - 1))

def calcuar_total(parcela,parcelas):
    return parcela*parcelas

def calcular_juros(valor,parcela):
    return valor-parcela
pode_aprovar(idade, renda, valor)
print(f"Nome do cliente: {nome}")
print(f"Valor financiado: {valor}")
taxas=definir_taxa(num)
print(f"Taxa de juros aplicada: {taxas}")
parcela=calcular_parcelas(valor,taxas)
print(f"Valor das parcelas: {parcela}")
total=calcuar_total(parcela,num)
print(f"Valor total: {total}")
print(f"Total de juros: {total-valor}")
