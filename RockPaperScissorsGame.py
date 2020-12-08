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
import random
usr_choice=int(input("What do you choose? Type  for Rock, 1 for Paper or 2 for Scissors: "))
game_list = [rock,paper,scissors]
print(game_list[usr_choice])
com_choice = random.randint(0,2)
print(f"computer choice is:  {com_choice}")
print(game_list[com_choice])

if (usr_choice==com_choice):
  print("Game Drawn")
elif(usr_choice==1) and (com_choice == 0):
  print("Player Win")
elif(usr_choice==0) and (com_choice == 2):
  print('Player Win')
elif(usr_choice==2) and (com_choice == 1):
  print('Player wins')
else:
  print("Computer Wins")

