class Aluno :
    def __init__(self, cpf_aluno, dt_nascimento_aluno, nome_aluno, id_aluno):
        self.cpf_aluno = cpf_aluno
        self.dt_nascimento_aluno = dt_nascimento_aluno 
        self.nome_aluno = nome_aluno
        self.id_aluno = id_aluno

class Disciplina:
    def __init__(self, id_disciplina, nome_disciplina, professor_disciplina):
        self.id_disciplina = id_disciplina
        self.nome_disciplina = nome_disciplina
        self.professor_disciplina = professor_disciplina

class Notas:
    def __init__(self, id_notas, primeira_nota, segunda_nota, terceira_nota, aluno_id, disciplina_id):
        self.id_notas = id_notas
        self.primeira_nota = primeira_nota
        self.segunda_nota = segunda_nota
        self.terceira_nota = terceira_nota
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id
