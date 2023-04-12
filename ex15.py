estudantes = {
    'João':{'idade':18, 'cidade':'Sao Paulo', 'notas':[7.5,8.0,9.0]},
    'Maria':{'idade':20, 'cidade':'Rio de Janeiro', 'notas': [6.5,7.0,8,5]},
    'Pedro':{'idade':19, 'cidade': 'Belo Horizonte', 'notas': [8.0,8,5,9.5]}
}

# Imprimir a idade do João
print('A idade do João é: ', str(estudantes['João']['idade']))

#Adicionar uma nova nota para Maria
estudantes['Maria']['notas'].append(9.0)

#Imprimir todas as informações dos alunos
for estudantes, info in estudantes.items():
    print(estudantes + ':')
    print('Idade: ' + str(info['idade']))
    print('Cidade: ' + info['cidade'])
    print('Notas: ' + str(info['notas']))
    print('Média: ' + str(sum(info['notas']) / len(info['notas'])))
    print()