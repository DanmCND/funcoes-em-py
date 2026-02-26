''' 
---Como criar funções em python----

---Estrutura de uma função---

def nome_da_funcao(parametros):
    bloco de código
    return valor_de_retorno

nome_da_funcao()

'''
#função para limpar terminal
import os
def limpar_terminal():
     os.system('cls')

#exemplo de fução com parametro
def saudacao(nome):
    print(f'Olá, {nome}! Como esta seu dia ?')

def soma(n1, n2):
    return n1 + n2





limpar_terminal()
saudacao('Danm')

print(soma(5, 10))
