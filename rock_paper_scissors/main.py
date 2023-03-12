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
game_images = [rock, paper, scissors]


choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors ")
print(" ")
user_choice = int(choice)
import random
list = [rock, paper, scissors]
choice_made  = list[user_choice]
print( f"You choose \n" + choice_made)
computer_choice = random.choice(list)
print(f"Computer choose \n" + computer_choice)

if computer_choice == choice_made:
  print("TIE")
elif computer_choice == 2 and choice_made == 1:
  print("Computer win")
elif computer_choice == 0 and choice_made == 2:
  print("Computer win")
elif computer_choice == 1 and choice_made == 0:
  print("Computer win")
else:
    print("You win")