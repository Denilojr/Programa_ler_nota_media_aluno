import random
import time
print('Vamos jogar Jokenpô??')
time.sleep(2)
jogador = str(input('Escolha sua jogada, \nPara Pedra digite 1 \nPara Papel digite 2 \nPara Tesoura digite 3: '))
print('Pedra...')
time.sleep(1)
print('papel...')
time.sleep(1)
print('Tesoura!!')
time.sleep(1)
computador = random.choice(['1', '2', '3'])
if jogador == computador:
    print('Você escolheu {} e o computador {}, deu empate!'.format(jogador, computador))
elif jogador == '1' and computador == '2':
    print('Você escolheu {} e o computador {}, você ganhou o jogo!'.format(jogador, computador))
elif jogador == '1' and computador == '3':
    print('Você escolheu {} e o computador {}, você perdeu o jogo!'.format(jogador, computador))
elif jogador == '2' and computador == '1':
    print('Você escolheu {} e o computador {}, você ganhou o jogo!'.format(jogador, computador))
elif jogador == '2' and computador == '3':
    print('Você escolheu {} e o computador {}, você perdeu o jogo!'.format(jogador, computador))
elif jogador == '3' and computador == '1':
    print('Você escolheu {} e o computador {}, você perdeu o jogo!'.format(jogador, computador))
elif jogador == '3' and computador == '2':
    print('Você escolheu {} e o computador {}, você ganhou o jogo!'.format(jogador, computador))
