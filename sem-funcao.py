# Montar um sistema de cadastro de aluno e notas 

'''
Menu de opçoes

1- cadastrar alunos
2- listar alunos
3- sair

'''

alunos = []


while True:
  
    #menu
    print("---Menu---")
    print("1- Cadastrar aluno")
    print("2- Listar alunos")
    print("3- Sair")
    
    opcao = input("Escolha a opcao:")

    match opcao:
        
        case "1":
           
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

        case "2":
            for alunos in alunos:
                print(alunos)     

        case "3":
            print("Sistema encerrado.")
            break
