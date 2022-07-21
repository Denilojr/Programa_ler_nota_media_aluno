import time
from random import randint
from operator import itemgetter
print('-=' * 15)
print('JOGO DE DADOS')
print('-=' * 15)
jogo = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = list()
for k, v in jogo.items(): # k é o titulo e v é o valor
    time.sleep(1)
    print(f'{k} tirou o número {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    time.sleep(0.5)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
