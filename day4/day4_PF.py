rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

jogador = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors "))

lista = [rock, paper, scissors]
comp = random.choice(lista)

if jogador == 0:
  print(rock)
  print(f'escolha do computador{comp}')
elif jogador == 1:
  print(paper)
  print(f'escolha do computador{comp}')
elif jogador >= 3 or jogador < 0:
  print('numero invalido!')
else:
  print(scissors)
  print(f'escolha do computador{comp}')

if jogador== 0 and comp== rock:
  print('gave a tie')
elif jogador== 0 and comp== paper:
  print('you lose')
elif jogador== 0 and comp== scissors:
  print('you win')
elif jogador== 1 and comp== rock:
  print('you win')
elif jogador== 1 and comp== paper:
  print('gave a tie')
elif jogador== 1 and comp== scissors:
  print('you lose')
elif jogador== 2 and comp== rock:
  print('you lose')
elif jogador== 2 and comp== paper:
  print('you win')
elif jogador== 2 and comp== scissors:
  print('gave a tie')
else:
  print('you lose')
