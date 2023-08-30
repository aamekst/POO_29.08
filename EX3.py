alunos = {}

for i in range(5):
    ra = input('RA:')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    alunos[ra] = [n1, n2, n3]
print(alunos)


for ra, notas in alunos.items():
    media = sum(notas)/len(notas)
    print(ra, media)


    '''
login =input('digite o nome do usuario para remover o amigo:')

for n in registro[login]['amigos']:
    print(n)

amigo =input('nome do amigo para remover: ')
registro[login]['amigos'].remove(amigo)

print(registro)



login =input('digite o nome do usuario para adicionar o amigo:')

for n in registro[login]['amigos']:
    print(n)

amigo =input('nome do amigo para adicionar: ')

registro[login]['amigos'].append(amigo)

print(registro)



#for usuario in registro.key():
#remove = input(f'nome do usuario: ')
#    print()
'''