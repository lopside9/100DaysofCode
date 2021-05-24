# Creating a higher / lower game
# Compare two items against each other and guess which one has a higher count
# Continue the game until a wrong answer is chosen, after which it's game over

# Import random module so that we can randomise choices from the game data
# Import the art module and the game_data module for the logos and data
import random
import art
import game_data
import replit

# Ask if the user wants to play a game
wants_to_play = input("Would you like to play a game of higher or lower? 'y' or 'n':\n")
if wants_to_play == "y":
  game_continue = True
else:
  game_continue = False
replit.clear()
print(art.logo)
player_score = 0


# Creating a function to pick a random integer to select from the list in game_data
# Then creating a new dictionary for 'A' and printing the statement to help the player see who they are comparing
def random_pick_a():
  random_a = {}
  random_element_a = random.randint(0, len(game_data.data) - 1)
  for i in game_data.data[random_element_a]:
    random_a[i] = game_data.data[random_element_a][i]
  print(f"Compare A: {random_a['name']}, a {random_a['description'].lower()}, from {random_a['country']}")
  return random_a


# Creating a function to pick a random integer to select from the list in game_data
# Then creating a new dictionary for 'B' and printing the statement to help the player see who they are comparing against
def random_pick_b():
  random_b = {}
  random_element_b = random.randint(0, len(game_data.data) - 1)
  for i in game_data.data[random_element_b]:
    random_b[i] = game_data.data[random_element_b][i]
  while random_b == a:
    random_element_b = random.randint(0, len(game_data.data) - 1)
    for i in game_data.data[random_element_b]:
      random_b[i] = game_data.data[random_element_b][i]
  print(f"Compare B: {random_b['name']}, a {random_b['description'].lower()}, from {random_b['country']}")
  return random_b
    

# Ask user who they think has the higher follower count and check against the correct guess
def check_guess():
  score = 0
  user_guess = input("Who do you think has the higher follower count? 'A' or 'B'?:\n").lower()
  a_followers = a["follower_count"]
  b_followers = b["follower_count"]
  correct_guess = max(a_followers, b_followers)
  # print(f"A: {a_followers}, B: {b_followers}")
  if correct_guess == a_followers:
    correct_guess = "a"
    correct_name = a["name"]
  else:
    correct_guess = "b"
    correct_name = b["name"]
  if user_guess == correct_guess:
    print(f"Correct! The right answer was {correct_name}.")
    score += 1
  else:
    print(f"Sorry, you chose wrong. The correct answer was {correct_name}. Game Over.")
  return score


# Starting the game by picking a random entry from the game_data dictionary
a = random_pick_a()
print(art.vs)
# Picks another random entry from the game_data dictionary, checks it's not the same as a, and then assigns it to value b
b = random_pick_b()
# Asks the player to choose which has the higher IG follower count, and checks if it is correct
if check_guess() == 1:
  player_score += 1
  print(player_score)
  # If correct, it choose another and carries on looping
  print(art.logo)
  while game_continue:
    # Checks if option a should change to the previous option b (which was correct / higher)
    if a["follower_count"] < b["follower_count"]:
      a = b
      print(f"Compare A: {a['name']}, a {a['description'].lower()}, from {a['country']}")
      print(art.vs)
      b = random_pick_b()
    else:
      print(f"Compare A: {a['name']}, a {a['description'].lower()}, from {a['country']}")
      print(art.vs)
      b = random_pick_b()
    if check_guess() == 1:
      player_score += 1
      print(player_score)
      print(art.logo)
    else:
      game_continue = False
else:
  game_continue = False
print(f"Your final score was {player_score}.")
print("End")
