#importa o sql
import sqlite3

#criacao bando de dados 
banco = sqlite3.connect('escola.db')

#metodo cursor para manipular o banco 
cursor = banco.cursor()

'''
tabela alunos: cpf, nome, dt_nascimento
tabela disciplinas: id_disciplina, nome_disciplina, professr_disciplina,
tabela notas: id_nota, nota1, nota2, nota3, aluno_id, disciplina_id
'''

#comando para criar tabela alunos
tablealunos = '''CREATE TABLE alunos(
    cpf_aluno INTEGER NOT NULL,    
    dt_nascimento_aluno DATE NOT NULL,
    nome_aluno TEXT NOT NULL, 
    id_aluno INTEGER NOT NULL PRIMARY KEY
)'''
#comando para criar a atabela disciplina
tabledisciplina = '''CREATE TABLE disciplina(
    id_disciplina INTEGER NOT NULL PRIMARY KEY,
    nome_disciplina TEXT NOT NULL,
    professor_disciplina TEXT NOT NULL
)'''
#comando para criar a tabela notas
tablenotas = '''CREATE TABLE notas(
    id_notas INTEGER NOT NULL PRIMARY KEY,
    primeira_nota INTEGER NOT NULL, 
    segunda_nota INTEGER NOT NULL,
    terceira_nota INTEGER NOT NULL,
    aluno_id INTEGER NOT NULL,
    disciplina_id INTEGER NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id_aluno),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id_disciplina)
)'''


'''
cursor com o metodo execute para criar a tabela alunos 
cursor.execute(tablealunos)
'''

'''
cursor com o metodo execute para criar a tabela disciplina
cursor.execute(tabledisciplina)
'''

'''
cursor com o metodo execute para criar a tabela notas
cursor.execute(tablenotas)
'''




