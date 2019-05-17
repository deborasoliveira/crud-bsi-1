#ADD alunos.txt, ADD disciplinas.txt, ADD professor.txt, ADD turmas.txt

from menus import menu_professor
from menus import menu_aluno
from menus import menu_disciplina
from menus import menu_turma
from menus import menu_principal

from alunoar import cadastro_aluno
from alunoar import remover_aluno
from alunoar import consultar_aluno
from alunoar import atualizar_aluno

from disciplinaar import cadastro_disciplina
from disciplinaar import remover_disciplina
from disciplinaar import alterar_disciplina
from disciplinaar import consultar_disciplina

from professorar import cadastro_prof
from professorar import remover_cadastro
from professorar import consultar_cadastro
from professorar import atualizar_prof

from turmaar import cadastro_turma
from turmaar import remover_turma
from turmaar import alterar_turma
from turmaar import consultar_turma

#RODANDO O PROGRAMA:
while True:
    try:
        menu_principal()
        cod = int(input("Digite a operação que deseja executar: "))
        if cod == 0:
            exit(0)


        elif cod == 1:
            menu_aluno()
            cod = int(input("Digite a operação que deseja executar: "))
            if cod == 0:
                menu_principal()
            elif cod == 1:
                cadastro_aluno()
            elif cod == 2:
                remover_aluno()
            elif cod == 3:
                consultar_aluno()
            elif cod == 4:
                atualizar_aluno()
            else:
                print("OPERAÇÃO INVÁLIDA.")


        elif cod == 2:
            menu_professor()
            cod = int(input("Digite a operação que deseja executar: "))
            if cod == 0:
                menu_principal()
            elif cod == 1:
                cadastro_prof()
            elif cod == 2:
                remover_cadastro()
            elif cod == 3:
                consultar_cadastro()
            elif cod == 4:
                atualizar_prof()
            else:
                print("OPERAÇÃO INVÁLIDA.")



        elif cod == 3:
            menu_disciplina()
            cod = int(input("Digite a operação que deseja executar: "))
            if cod == 0:
                menu_principal()
            elif cod == 1:
                cadastro_disciplina()
            elif cod == 2:
                remover_disciplina()
            elif cod == 3:
                consultar_disciplina()
            elif cod == 4:
                alterar_disciplina()
            else:
                print("OPERAÇÃO INVÁLIDA.")


        elif cod == 4:
            menu_turma()
            cod = int(input("Digite a operação que deseja executar: "))
            if cod == 0:
                menu_principal()
            elif cod == 1:
                cadastro_turma()
            elif cod == 2:
                remover_turma()
            elif cod == 3:
                consultar_turma()
            elif cod == 4:
                alterar_turma()
            else:
                print("OPERAÇÃO INVÁLIDA.")
        else:
            print("OPERAÇÃO INVÁLIDA.")
    except EOFError:
        break
menu_principal()


