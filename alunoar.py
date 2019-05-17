aluno = []
#PARA SALVAR O CADASTRO, A ATUALIZAÇÃO E A REMOÇÃO DO ALUNO
def salvar_cadastro():
    global aluno
    arq = open("alunos.txt", "w", encoding = "utf-8")
    for i in aluno:
        nome_aluno = str(i[0])
        cpf_aluno = str(i[1])
        arq.write('%s %s\n' % (nome_aluno, cpf_aluno))
    arq.close()


#CADASTRO
def cadastro_aluno():
    while True:
        try:
            op = int(input("Para realizar o cadastro de aluno, digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                nome_aluno = input("Digite o nome do aluno: ") #ADICIONAR DADOS DO ALUNO
                cpf_aluno = input("Digite o cpf do aluno: ")
                for i in range(len(aluno)):
                    if cpf_aluno in aluno[i][1]:  #CASO ELE SEU CPF JÁ ESTEJA NA LISTA, SIGNIFICA QUE JÁ ESTÁ MATRICULADO
                        print("Aluno já matriculado.\n")
                        print("Nome do aluno: {} CPF do aluno: {}".format(aluno[i][0], aluno[i][1]))
                        break #SE ELE ESTIVER MATRICULADO, PARAMOS O PROGRAMA
                else:
                    aluno.append([nome_aluno, cpf_aluno]) #CASO CONTRÁRIO, ELE SERÁ ADICIONADO À LISTA DE ALUNOS
                    print("NOME: {} CPF: {}, Aluno matriculado com sucesso!".format(nome_aluno,cpf_aluno))
                    salvar_cadastro() #FUNÇÃO PARA SALVAR CADASTRO
                    break
            elif op == 2:
                break #CASO ELE ESCOLHA A OPÇÃO 2, O PROGRAMA SERÁ FINALIZADO
            else:
                print("Opção inválida") #CASO ELE ESCOLHA QUALQUER OUTRA OPÇÃO, SERÁ CONSIDERADA INVÁLIDA
        except EOFError:
            break

#REMOVER O CADASTRO
def remover_aluno():
    while True:
        try:
            op = int(input("Para remover aluno, digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                r_aluno = input("Para remoção do aluno, digite seu cpf: ") #PARA EXERCUTAR A REMOÇÃO É PRECISO INFORMAR O CPF
                for i in range(len(laluno)):
                    if aluno[i][1] == r_aluno:
                        print("Aluno removido com sucesso.") #CASO O ALUNO ESTEJA CADASTRADO, A REMOÇÃO É EFETUADA
                        aluno.remove(aluno[i])
                        salvar_cadastro()
                        break
                else:
                    print("Cadastro não encontrado.") #CASO CONTRÁRIO, SERÁ INFORMADO DE QUE ESTE CPF NÃO ESTÁ CADASTRADO
            elif op == 2: #CASO ELE ESCOLHA A OPÇÃO 2, O PROGRAMA DEIXARÁ DE RODAR
                break
            elif op != 1 or op != 2: #CASO ELE ESCOLHA OUTRA OPÇÃO, ELA SERÁ CONSIDERADA INVÁLIDA
                print("Operação inválida.")
        except EOFError:
            break


#CONSULTA DO CADASTRO
def consultar_aluno():
    while True:
        try:
            op = int(input("Para realizar a consulta de aluno, digite 1, para retornar ao menu principal digite 2: "))
            if op == 1:
                consulta_aluno = input("Digite seu cpf para a consulta de matrícula: ") #PARA A CONSULTA É NECESSÁRIO A VERIFICAÇÃO DO CPF
                for i in range(len(aluno)):
                    if aluno[i][1] == consulta_aluno: #SE O CPF ESTIVER NA LISTA, O CADASTRO SERÁ CONSULTADO NORMALMENTE
                        print("NOME: {}\n"
                              "CPF: {}".format(aluno[i][0], aluno[i][1]))
                    else:
                        print("Aluno não matriculado.") #CASO CONTRÁRIO, SRÁ INFORMADO DE QUE NÃO HÁ CADASTRO COM ESTE CPF
            elif op == 2:
                break #FINALIZAR PROGRAMA
            else:
                print("Operação inválida.") #CASO A OPÇÃO DELE SEJA DIFERENTE DAS APRESENTADAS, ELA SERÁ CONSIDERADA INVÁLIDA
        except EOFError:
            break



#ATUALIZAR O CADASTRO
def atualizar_aluno():
    while True:
        try:
            alt_aluno = int(input("Para ter acesso à atualização de cadastro, digite 1, para retornar ao menu principal digite 2: "))
            if alt_aluno == 1:
                alterar = input("Digite seu CPF(sem pontos) para ter acesso à atualização de cadastro: ") #VERIFICAÇÃO DE CPF
                for i in range(len(aluno)):
                    if aluno[i][1] == alterar: #CASO ESTEJA NA LISTA, A ATUALIZAÇÃO SERÁ PERMITIDA
                        op = int(input("Para atualizar o nome digite 1, para atualizar o cpf digite 2: "))
                        if op == 1:
                            nome = input("Digite seu nome aqui: ")
                            aluno[i][0] = nome
                            print("NOME: {}\n"
                                  "CPF: {}".format(aluno[i][0], aluno[i][1]))
                            print("Cadastro alterado com sucesso.")
                            salvar_cadastro()
                        elif op == 2:
                            cpf = input("Digite seu cpf(sem pontos): ")
                            aluno[i][1] = cpf
                            print("NOME: {}\n"
                                    "CPF: {}".format(aluno[i][0], aluno[i][1]))
                            print("Cadastro alterado com sucesso.")
                            salvar_cadastro()
                        else:
                            print("Opção inválida.") #ESCLHA DIFERENTE DAS APRESENTADAS
                    else:
                        print("Este aluno não está cadastrado.") #CPF NÃO ENCONTRADO NA LISTA
            elif alt_aluno == 2:
                break
        except EOFError:
            break

