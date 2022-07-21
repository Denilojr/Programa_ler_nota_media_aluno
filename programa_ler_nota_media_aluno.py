def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor adicional indicando se deve ou nao indicar a situação
    :return: dicionarios com várias informações sobre a situação dos alunos
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return s


resp = notas(9, 8.5, 2, sit=True)
print(resp)
help(notas)