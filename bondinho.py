professores = int(input())
alunos = int(input())
soma = alunos / professores
if soma <= 50:
    print(f'foi possivel fazer em {professores} viagem')
elif soma > 50:
    print('nao foi possivel fazer a viagem')
