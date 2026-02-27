
alunos = []

def menu_opcoes():     
    print("---Menu---")
    print("1- Cadastrar aluno")
    print("2- Listar alunos")
    print("3- Mostar total de alunos cadastrados")
    print("4- Sair")

def cadastro_aluno():
    nome = input("Digite o nome do aluno:")
    nota1 = int(input("Digite a nota do aluno:"))
    nota2 = int(input("Digite a segunda nota:"))

    media = (nota1 + nota2) / 2
    
    if media >= 7:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    #Adicina na lista: nome aluno e situação
    alunos.append(f"{nome} - {situacao}")

    print("Aluno cadastrado com sucesso")

def listar_alunos():
    for aluno in alunos:
            print(aluno)

def total_cadastrado():
    if len(alunos) > 0:
        print(len(alunos))
    else:
        print("A lista esta Vazia!")


while True:
  
    menu_opcoes()
    
    opcao = input("Escolha a opcao:")

    match opcao:
        
        case "1":
            cadastro_aluno()
            
           
        case "2":
           listar_alunos()
           

        case "3":
            total_cadastrado()
           
           
        case "4":
            print("Sistema encerrado.")
            break

        case _:
            print("opção invalida!")
