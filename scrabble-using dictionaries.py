#SCRABBLE - using dictionaries to organize players, words, and points.


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_point = {key:value for key, value in zip(letters, points)}
#print(letters_to_point)
letters_to_point[""] = 0

def score_word(word):
  point_total = 0
  for letters in word:
    point_total += letters_to_point.get(letters,0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points["player"] = player_points

  print(player_to_points)

#play_word function - takes in a player and a word, and add that word to the list of words they have played
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    print("This player does not exist")

play_word("player1", "GRASSCOURT")
