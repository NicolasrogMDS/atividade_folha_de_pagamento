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
            sleep(1)
            break
        else:
            print("\nMatrícula e senha incorretas. Por favor, tente novamente.")
            sleep(1)
    return matricula_inserida, senha_inserida

def calcular_desconto_inss(a):
    if a <= 1100.00:  # Desconta 7,5%
        desconto_inss = a * 0.075
        return desconto_inss
    elif a <= 2203.48:  # Desconta 9%
        desconto_inss = a * 0.09
        return desconto_inss
    elif a <= 3305.22:  # Desconta 12%
        desconto_inss = a * 0.12
        return desconto_inss
    elif a <=  6433.57:  # Desconta 14% ou no máximo R$854.36
        desconto_inss = a * 0.14
        if desconto_inss > 854.36:
            desconto_inss = 854.36
        return desconto_inss
    else:  # Desconta no máximo R$854.36
        desconto_inss = a * 0.14
        if desconto_inss > 854.36:
            desconto_inss = 854.36
        return desconto_inss
    
def calcular_desconto_vale_transporte(a):
    desconto_vale_transporte = a * 0.06
    return desconto_vale_transporte

def calcular_desconto_vale_refeicao(a):
    desconto_vale_refeicao = a * 0.20
    return desconto_vale_refeicao 
    

matricula_registrada, senha_registrada = registrar_matricula_senha()
matricula_inserida, senha_inserida = verificar_matricula_senha()
salario_base = float(input("Insira o seu salário base: "))

while True:
    pergunta_vale_transporte = input("""
Você recebe vale transporte? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_vale_transporte == 's':
        break
    elif pergunta_vale_transporte == 'n':
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

while True:
    pergunta_vale_refeicao = input("""
Você recebe vale refeição? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_vale_refeicao == 's':
        vale_refeicao = float(input("Insira o valor do vale refeição: "))
        break
    elif pergunta_vale_refeicao == 'n':
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

while True:
    pergunta_dependentes = input("""
Você possui algum dependente? 
Digite 's' se sim ou 'n' se não: """).lower().strip()
    if pergunta_dependentes == 's':
        quantidade_de_dependentes = float(input("Insira quantos dependentes você possui: "))
        break
    elif pergunta_vale_refeicao == 'n':
        break
    else:
        print("Ops... Você não inseriu 's' ou 'n'. Por favor, tente novamente.")

desconto_inss = calcular_desconto_inss(salario_base)