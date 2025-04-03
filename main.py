from os import system
from time import sleep

def limpar_tela():
    system("cls || clear")

def registrar_matricula_senha():
    matricula = input("Digite os 4 dígitos para registrar a sua matrícula: ")
    senha = input("Agora, registre a sua senha: ")
    print("Matrícula e senha registradas com sucesso!")
    return matricula, senha

def fazer_login():
    matricula_inserida = input("\nInsira a sua matrícula: ")
    senha_inserida = input("Insira a sua senha: ")
    return matricula_inserida, senha_inserida

def verificar_matricula_senha():
    while True:
        matricula_inserida, senha_inserida = fazer_login()
        if matricula_inserida == matricula_registrada and senha_inserida == senha_registrada:
            print("\nSeja bem-vindo!")
            sleep(2)
            limpar_tela()
            break
        else:
            print("\nMatrícula ou senha incorretas. Por favor, tente novamente.")
            sleep(2)
            limpar_tela()
    return matricula_inserida, senha_inserida

def calcular_desconto_inss(salario_bruto):
    if salario_bruto <= 1518.00:  # Desconta 7,5%
        desconto_inss = salario_bruto * 0.075
    elif salario_bruto <= 2793.88:  # Desconta 9%
        desconto_inss = salario_bruto * 0.09
    elif salario_bruto <= 4190.83:  # Desconta 12%
        desconto_inss = salario_bruto * 0.12
    elif salario_bruto <=  8157.41:  # Desconta 14%
        desconto_inss = salario_bruto * 0.14
    else:  # Desconta no máximo R$854.36
        desconto_inss = 854.36
    return desconto_inss

def calcular_desconto_irrf(salario_bruto, dependentes):
    if salario_bruto <= 2259.20:  # Isento
        desconto_irrf = 0
    elif salario_bruto <= 2826.65:  # Desconta 7,5%
        desconto_irrf = salario_bruto * 0.075
    elif salario_bruto <= 3751.05:  # Desconta 15%
        desconto_irrf = salario_bruto * 0.15
    elif salario_bruto <= 4664.68:  # Desconta 22,5%
        desconto_irrf = salario_bruto * 0.225
    else:  # Desconta 27,5%
        desconto_irrf = salario_bruto * 0.275
    
    if dependentes != 0:
        deducao_por_dependente = 189.59 * dependentes
    else:
        deducao_por_dependente = 0
    
    desconto_irrf_final = desconto_irrf - deducao_por_dependente
    return desconto_irrf_final

def calcular_desconto_vale_transporte(a):
    desconto_vale_transporte = a * 0.06
    return desconto_vale_transporte

def calcular_desconto_vale_refeicao(a):
    desconto_vale_refeicao = a * 0.20
    return desconto_vale_refeicao

def calcular_desconto_plano_de_saude(dependentes):
    valor_por_dependente = 150
    if dependentes != 0:
        desconto_plano_de_saude = valor_por_dependente * dependentes
    else:
        desconto_plano_de_saude = 0
    return desconto_plano_de_saude 

limpar_tela()
matricula_registrada, senha_registrada = registrar_matricula_senha()
matricula_inserida, senha_inserida = verificar_matricula_senha()
salario_base = float(input("Insira o seu salário base: "))

desconto_inss = calcular_desconto_inss(salario_base)
while True:
    pergunta_vale_transporte = input("""
Você recebe vale transporte? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_vale_transporte == 's':
        desconto_vale_transporte = calcular_desconto_vale_transporte(salario_base)
        break
    elif pergunta_vale_transporte == 'n':
        desconto_vale_transporte = 0
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

while True:
    pergunta_vale_refeicao = input("""
Você recebe vale refeição? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_vale_refeicao == 's':
        vale_refeicao = float(input("Insira o valor do vale refeição: "))
        desconto_vale_refeicao = calcular_desconto_vale_refeicao(vale_refeicao)
        break
    elif pergunta_vale_refeicao == 'n':
        desconto_vale_refeicao = 0
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

while True:
    pergunta_dependentes = input("""
Você possui algum dependente? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_dependentes == 's':
        quantidade_de_dependentes = int(input("Insira quantos dependentes você possui: "))
        calcular_desconto_plano_de_saude(quantidade_de_dependentes)
        break
    elif pergunta_dependentes == 'n':
        quantidade_de_dependentes = 0
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

desconto_irrf = calcular_desconto_irrf(salario_base, quantidade_de_dependentes)
desconto_plano_de_saude = calcular_desconto_plano_de_saude(quantidade_de_dependentes)

salario_liquido = salario_base - (desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_de_saude)

print(f"\nO seu salário líquido será: R${salario_liquido:.2f}")
print(f"\nDesconto inss = R${desconto_inss:.2f}")
print(f"Desconto imposto de renda = R${desconto_irrf}")
print(f"Desconto vale de transporte = R${desconto_vale_transporte}")
print(f"Desconto vale refeição = R${desconto_vale_refeicao}")
print(f"Desconto plano de saúde = R${desconto_plano_de_saude}")