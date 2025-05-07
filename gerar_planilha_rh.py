import pandas as pd
from faker import Faker
import random
from datetime import timedelta

fake = Faker('pt_BR')
num_rows = 5000

# Helper functions
def random_date(start, end):
    return fake.date_between(start_date=start, end_date=end)

def random_bool():
    return random.choice(['Sim', 'Não'])

def random_choice(choices):
    return random.choice(choices)

# ABA 1: FUNCIONÁRIOS
funcionarios = []
for i in range(1, num_rows + 1):
    data_nasc = fake.date_of_birth(minimum_age=18, maximum_age=65)
    data_adm = fake.date_between(start_date='-10y', end_date='today')
    data_desl = data_adm + timedelta(days=random.randint(0, 365*5)) if random.random() < 0.2 else ''
    funcionarios.append([
        i,
        fake.name(),
        fake.cpf(),
        fake.rg(),
        data_nasc.strftime('%d/%m/%Y'),
        random_choice(['Masculino', 'Feminino', 'Outro']),
        random_choice(['Solteiro', 'Casado', 'Divorciado', 'Viúvo']),
        'Brasileiro',
        random_choice(['Analista', 'Gerente', 'Assistente', 'Diretor', 'Coordenador']),
        random_choice(['RH', 'Financeiro', 'TI', 'Comercial', 'Operacional']),
        data_adm.strftime('%d/%m/%Y'),
        data_desl.strftime('%d/%m/%Y') if data_desl else '',
        random_choice(['CLT', 'PJ', 'Estágio', 'Temporário']),
        round(random.uniform(1500, 20000), 2),
        random_choice(['VT, VR', 'Plano Saúde', 'Seguro de Vida', '']),
        fake.email(),
        fake.phone_number(),
        fake.address().replace('\n', ', '),
        fake.sentence(nb_words=6)
    ])
df_funcionarios = pd.DataFrame(funcionarios, columns=[
    'ID', 'Nome Completo', 'CPF', 'RG', 'Data Nasc.', 'Gênero', 'Estado Civil', 'Nacionalidade',
    'Cargo', 'Departamento', 'Data Admissão', 'Data Desligamento', 'Tipo Contrato (CLT/PJ/etc.)',
    'Salário Base', 'Benefícios', 'E-mail', 'Telefone', 'Endereço', 'Observações'
])

# ABA 2: FOLHA DE PAGAMENTO
folha_pagamento = []
for i in range(1, num_rows + 1):
    salario_base = round(random.uniform(1500, 20000), 2)
    horas_extras = round(random.uniform(0, 40), 2)
    adicionais = round(random.uniform(0, 1000), 2)
    inss = round(salario_base * 0.11, 2)
    irrf = round(salario_base * 0.075, 2)
    vt = round(random.uniform(0, 300), 2)
    va = round(random.uniform(0, 500), 2)
    faltas = random.randint(0, 5)
    descontos = round(random.uniform(0, 1000), 2)
    salario_liquido = salario_base + adicionais + horas_extras - inss - irrf - descontos
    folha_pagamento.append([
        i,
        fake.name(),
        salario_base,
        horas_extras,
        adicionais,
        inss,
        irrf,
        vt,
        va,
        faltas,
        descontos,
        round(salario_liquido, 2),
        fake.date_this_year().strftime('%d/%m/%Y'),
        random_choice(['Transferência', 'Cheque', 'Dinheiro'])
    ])
df_folha = pd.DataFrame(folha_pagamento, columns=[
    'ID', 'Nome', 'Salário Base', 'Horas Extras', 'Adicionais', 'INSS', 'IRRF',
    'Vale Transporte', 'Vale Alimentação', 'Faltas', 'Descontos', 'Salário Líquido',
    'Data Pagamento', 'Método Pagamento'
])

# ABA 3: BANCO DE HORAS
banco_horas = []
for i in range(1, num_rows + 1):
    data = fake.date_this_year()
    hora_entrada = fake.time(pattern='%H:%M')
    hora_saida = fake.time(pattern='%H:%M')
    total_horas = round(random.uniform(6, 10), 2)
    horas_extras = round(random.uniform(0, 2), 2)
    saldo_banco = round(random.uniform(-10, 20), 2)
    banco_horas.append([
        i,
        fake.name(),
        data.strftime('%d/%m/%Y'),
        hora_entrada,
        hora_saida,
        total_horas,
        horas_extras,
        saldo_banco,
        fake.sentence(nb_words=4)
    ])
df_banco = pd.DataFrame(banco_horas, columns=[
    'ID', 'Nome', 'Data', 'Hora Entrada', 'Hora Saída', 'Total Horas/Dia',
    'Horas Extras', 'Saldo Banco', 'Observações'
])

# ABA 4: FÉRIAS
ferias = []
for i in range(1, num_rows + 1):
    data_inicio = fake.date_between(start_date='-2y', end_date='today')
    dias_gozados = random.randint(5, 30)
    data_fim = data_inicio + timedelta(days=dias_gozados)
    saldo_dias = 30 - dias_gozados
    ferias.append([
        i,
        fake.name(),
        data_inicio.strftime('%d/%m/%Y'),
        data_fim.strftime('%d/%m/%Y'),
        dias_gozados,
        saldo_dias,
        random_bool(),
        fake.sentence(nb_words=3)
    ])
df_ferias = pd.DataFrame(ferias, columns=[
    'ID', 'Nome', 'Data Início', 'Data Fim', 'Dias Gozados', 'Saldo Dias',
    'Abono Pecuniário? (Sim/Não)', 'Observações'
])

# ABA 5: BENEFÍCIOS
beneficios = []
for i in range(1, num_rows + 1):
    data_inicio = fake.date_between(start_date='-3y', end_date='today')
    data_termino = data_inicio + timedelta(days=random.randint(30, 365))
    beneficios.append([
        i,
        fake.name(),
        random_bool(),
        random_bool(),
        random_bool(),
        random_bool(),
        random_choice(['Seguro de Vida', 'Auxílio Home Office', '']),
        data_inicio.strftime('%d/%m/%Y'),
        data_termino.strftime('%d/%m/%Y')
    ])
df_beneficios = pd.DataFrame(beneficios, columns=[
    'ID', 'Nome', 'Plano Saúde', 'Vale Alimentação', 'Vale Transporte',
    'Auxílio Creche', 'Outros Benefícios', 'Data Início', 'Data Término'
])

# ABA 6: TREINAMENTOS
treinamentos = []
for i in range(1, num_rows + 1):
    treinamentos.append([
        i,
        fake.name(),
        random_choice(['Liderança', 'Excel', 'Comunicação', 'Gestão de Projetos', 'Vendas']),
        fake.date_this_decade().strftime('%d/%m/%Y'),
        random.randint(4, 40),
        random_choice(['SENAI', 'SENAC', 'Udemy', 'Alura', 'Interno']),
        round(random.uniform(0, 2000), 2),
        random.randint(1, 5),
        random_bool()
    ])
df_treinamentos = pd.DataFrame(treinamentos, columns=[
    'ID', 'Nome', 'Treinamento', 'Data', 'Carga Horária', 'Fornecedor',
    'Custo', 'Avaliação (1-5)', 'Certificado? (Sim/Não)'
])

# ABA 7: AVALIAÇÕES
avaliacoes = []
for i in range(1, num_rows + 1):
    comp_tec = random.randint(1, 5)
    comp_comp = random.randint(1, 5)
    nota_final = round((comp_tec + comp_comp) / 2, 2)
    avaliacoes.append([
        i,
        fake.name(),
        random_choice(['Analista', 'Gerente', 'Assistente', 'Diretor', 'Coordenador']),
        fake.date_this_year().strftime('%d/%m/%Y'),
        comp_tec,
        comp_comp,
        nota_final,
        fake.sentence(nb_words=6),
        fake.sentence(nb_words=4)
    ])
df_avaliacoes = pd.DataFrame(avaliacoes, columns=[
    'ID', 'Nome', 'Cargo', 'Data Avaliação', 'Competência Técnica (1-5)',
    'Competência Comportamental (1-5)', 'Nota Final', 'Feedback', 'Ações de Melhoria'
])

# ABA 8: DOCUMENTOS
documentos = []
for i in range(1, num_rows + 1):
    validade = fake.date_between(start_date='today', end_date='+5y').strftime('%d/%m/%Y')
    documentos.append([
        i,
        fake.name(),
        fake.numerify(text='#########'),  # CTPS
        fake.numerify(text='##########'),  # PIS
        fake.numerify(text='######'),  # Cert. Reservista
        fake.numerify(text='###########'),  # Título Eleitor
        fake.numerify(text='###########'),  # Comprovante Escolar
        fake.numerify(text='###########'),  # Comprovante Endereço (ADDED)
        random_bool(),  # Visto em Dia?
        validade  # Validade Documentos
    ])
df_documentos = pd.DataFrame(documentos, columns=[
    'ID', 'Nome', 'CTPS', 'PIS', 'Cert. Reservista', 'Título Eleitor',
    'Comprovante Escolar', 'Comprovante Endereço', 'Visto em Dia? (Sim/Não)', 'Validade Documentos'
])

# ABA 9: RECRUTAMENTO
recrutamento = []
for i in range(1, num_rows + 1):
    data_inscricao = fake.date_between(start_date='-2y', end_date='today')
    data_contratacao = data_inscricao + timedelta(days=random.randint(1, 60)) if random.random() < 0.5 else ''
    recrutamento.append([
        i,
        fake.name(),
        random_choice(['Analista', 'Gerente', 'Assistente', 'Diretor', 'Coordenador']),
        data_inscricao.strftime('%d/%m/%Y'),
        random_choice(['Triagem', 'Entrevista', 'Contratação']),
        fake.name(),
        random_choice(['Aprovado', 'Reprovado']),
        data_contratacao.strftime('%d/%m/%Y') if data_contratacao else '',
        fake.sentence(nb_words=5)
    ])
df_recrutamento = pd.DataFrame(recrutamento, columns=[
    'ID', 'Nome Candidato', 'Vaga', 'Data Inscrição', 'Fase (Triagem/Entrevista/Contratação)',
    'Entrevistador', 'Resultado (Aprovado/Reprovado)', 'Data Contratação', 'Observações'
])

# ABA 10: DEMISSÕES
demissoes = []
for i in range(1, num_rows + 1):
    data_demissao = fake.date_between(start_date='-2y', end_date='today')
    ultimo_dia = data_demissao + timedelta(days=random.randint(0, 30))
    demissoes.append([
        i,
        fake.name(),
        data_demissao.strftime('%d/%m/%Y'),
        random_choice(['Pedido', 'Justa Causa', 'Sem Justa Causa', 'Acordo']),
        random_choice(['Voluntária', 'Involuntária']),
        random_bool(),
        round(random.uniform(0, 50000), 2),
        ultimo_dia.strftime('%d/%m/%Y'),
        fake.sentence(nb_words=6)
    ])
df_demissoes = pd.DataFrame(demissoes, columns=[
    'ID', 'Nome', 'Data Demissão', 'Motivo (Pedido/Justa Causa/etc.)', 'Tipo Saída',
    'Aviso Prévio? (Sim/Não)', 'Liquidação (Valor)', 'Último Dia', 'Feedback Saída'
])

# Save to Excel
with pd.ExcelWriter(r'c:\Users\elmessonjesus\Desktop\RH\gestao_rh_dp.xlsx', engine='xlsxwriter') as writer:
    df_funcionarios.to_excel(writer, sheet_name='FUNCIONÁRIOS', index=False)
    df_folha.to_excel(writer, sheet_name='FOLHA DE PAGAMENTO', index=False)
    df_banco.to_excel(writer, sheet_name='BANCO DE HORAS', index=False)
    df_ferias.to_excel(writer, sheet_name='FÉRIAS', index=False)
    df_beneficios.to_excel(writer, sheet_name='BENEFÍCIOS', index=False)
    df_treinamentos.to_excel(writer, sheet_name='TREINAMENTOS', index=False)
    df_avaliacoes.to_excel(writer, sheet_name='AVALIAÇÕES', index=False)
    df_documentos.to_excel(writer, sheet_name='DOCUMENTOS', index=False)
    df_recrutamento.to_excel(writer, sheet_name='RECRUTAMENTO', index=False)
    df_demissoes.to_excel(writer, sheet_name='DEMISSÕES', index=False)

print("Planilha de RH criada com sucesso!")