import sqlite3

from modelo import Aluno, Disciplina, Notas

banco = sqlite3.connect('escola.db')
banco.execute('PRAGMA foreign_keys_on')


cursor = banco.cursor()


comando1 = '''INSERT INTO alunos(cpf_aluno, dt_nascimento_aluno, nome_aluno, id_aluno) VALUES (:cpf_aluno, :dt_nascimento_aluno, :nome_aluno, :id_aluno)'''

comando2 = ''' INSERT INTO disciplina(id_disciplina, nome_disciplina, professor_disciplina ) VALUES (:id_disciplina, :nome_disciplina, :professor_disciplina)'''

comando3 = '''INSERT INTO notas(id_notas, primeira_nota, segunda_nota, terceira_nota, aluno_id, disciplina_id) VALUES(:id_notas, :primeira_nota, :segunda_nota, :terceira_nota, :aluno_id, :disciplina_id)'''


aluno1 = Aluno(13795421859, '1987-04-15', 'Juninho', 1)

disciplina1 = Disciplina(1, 'historia', 'helder')

notas1 = Notas(40, 10 , 7 , 9 , 1 ,1)

'''
try:
    cursor.execute(comando1, vars(aluno1))
    banco.commit()
    print('Sucesso ao adicionar dados!')
except sqlite3.Error as erro:
    print('Ocorreu um erro ao tentar adicionar dados a tabela ', erro)
'''
'''
try:
    cursor.execute(comando2, vars(disciplina1))
    banco.commit()
    print('Sucesso ao adicionar dados!')
except sqlite3.Error as erro:
    print('Ocorreu um erro ao tentar adicionar dados a tabela ', erro)
'''


try:
    cursor.execute(comando3, vars(notas1))
    banco.commit()
    print('Sucesso ao adicionar dados!')
except sqlite3.Error as erro:
    print('Ocorreu um erro ao tentar adicionar dados a tabela ', erro)

