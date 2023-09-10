def notas(*notas, situacao=False):
    '''
    função que mostra a quantidade de notas, a maior nota, a menor, a média e a situação(opcional)
    param:*notas: recebe todas as notas
    param:situacao: recebe a informação se a pessoa quer saber a situação da turma ou não
    return: retorna um dicionário contendo todas as informações
    '''
    listaNotas = list(notas) # transformando a tupla em lista para manipalá-la
    listaNotas.sort()
    dictNotas = {'total': len(listaNotas), 'maior': listaNotas[-1], 'menor': listaNotas[0], 'media': sum(listaNotas) / len(listaNotas)}
    
    if situacao:
        if dictNotas['media'] >= 8:
            situacao = 'excelente'
        elif 6 <= dictNotas['media'] < 8:
            situacao = 'bom'
        else:
            situacao = 'ruim'
        dictNotas['situação'] = situacao

    return dictNotas


# programa principal
resp = notas(10, 9, 7, 8, 10, situacao=True)
print(resp)