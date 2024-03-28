from game_data import data
from art import logo, vs
from replit import clear
import random


def random_person():
  personA = random.choice(data)
  return personA


def format_data(user):
  name = user["name"]
  description = user["description"]
  country = user["country"]
  return (f"{name}, a {description}, from {country}")


def check_answer(guess, a_followers, b_followers):
  if guess == 'A' and a_followers > b_followers:
    return True
  elif guess == 'B' and b_followers > a_followers:
    return True
  else:
    return False


def display(game_mode):
  point = 0
  userA = random_person()
  userB = random_person()
  while game_mode:
    userA = userB
    userB = random_person()

    #A vs B
    print(logo)
    print("Compare A:", format_data(userA))

    print(vs)
    if userA == userB:
      userB = random_person()

    print("Compare B:", format_data(userB))

    print(f"Your current score is {point}")
    print("")

    #Compare the follower counts
    userACount = userA['follower_count']
    userBCount = userB['follower_count']

    guess = input("Type A or B: ")
    is_correct = check_answer(guess, userACount, userBCount)

    if is_correct:
      point += 1
      print(f"You're right! Current Score: {point}")
    else:
      print("Unlucky, You lost!")
      break
    clear()

  print(f"Your final score is {point}")


if input("Do you want to start the game? Y/N: ") == 'Y':
  game_mode = True
else:
  game_mode = False

display(game_mode)
