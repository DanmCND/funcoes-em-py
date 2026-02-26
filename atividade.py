
import os 
def limpar_tela():
    os.system('cls')

limpar_tela()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2  

def multiplicar(n1, n2):   
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida."

#bonus

def porcentagem(n1, n2):
    return (n1 * n2) / 100


print(f"Soma: {somar(n1, n2)}")
print(f"Subtração: {subtrair(n1, n2)}")
print(f"Multiplicação: {multiplicar(n1, n2)}")
print(f"Divisão: {dividir(n1, n2)}")
print(f'{n2}% de {n1} é {porcentagem(n1, n2)}')