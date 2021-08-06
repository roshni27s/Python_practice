# // rock paper scissors
import random
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
print("Welcome to the Rock Paper Scissors Game!")
list=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if(user_choice>=3 or user_choice<0):
  print("Invalid number. You lose!")
else:
  print(list[user_choice])
  computer_choice=random.randint(0,2)
  print("Computer chose: ")
  print(list[computer_choice])
  if user_choice==0 and computer_choice==2:
    print("You win!")
  elif computer_choice==0 and user_choice==2:
    print("You Lose!")
  elif user_choice<computer_choice:
    print("You Lose!")
  elif user_choice>computer_choice:
    print("You Win!")
  elif user_choice==computer_choice:
    print("Draw!")
