from math import e
import random
import string
import time
categories = ['animals', 'dota', 'cars', 'marvel', 'countries']
animal_topic_list = ['elephant', 'rhinoceros', 'kangaroo', 'rooster', 'chimpanzee', 'buffalo', 'whale', 'crocodile', 'racoon', 'gazelle', 'weasel', 'donkey', 'hippopotamus', 'orangutan', 'cheetah', 'turtle', 'chinchilla', 'rooster', 'hamster', 'panda', 'reindeer']
countries_topic_list = ['canada', 'bulgaria', 'ukraine', 'poland', 'france', 'greece', 'denmark', 'niger', 'kyrgyzstan', 'germany', 'greenland', 'czechia', 'mexico', 'cyprus', 'Madagascar', 'turkmenistan', 'belgium', 'netherlands', 'sweden', 'indonesia', 'belarus']
cars = ['lexus', 'audi', 'zaporozhets', 'subaru', 'citroen', 'pagani', 'mercedes', 'chrysler', 'hyundai', 'bugatti', 'jaguar', 'suzuki', 'volkswagen', 'chevrolet', 'toyota', 'tesla', 
'cadillac', 'koenigsegg', 'ferrari', 'dodge', 'lamborghini']
dota_characters = ['abaddon', 'alchemist', 'batrider', 'broodmother', 'beastmaster', 'bloodseeker', 'clockwerk', 'bristleback', 'clinkz', 'brewmaster', 'disruptor', 'gyrocopter', 'hoodwink', 'huskar', 'invoker', 'jakiro', 'juggernaut', 'lifestealer', 'kunkka', 'lykan', 'meepo', 'necrophos', 'morphling', 'medusa', 'omniknight', 'oracle', 'pangolier', 'pudge', 'rubick', 'slardar', 'slark', 'spectre', 'snapfire', 'terrorblade', 'tinker', 'timbersaw', 'underlord', 'warlock', 'windranger', 'phantom assassin', 'phantom lancer', 'night stalker', 'arc warden', 'crystal maiden', 'death prophet']
marvel_characters = ['silver surfer', 'volverine', 'invisible woman', 'black bolt', 'cable', 'howard the duck', 'captain marvel', 'thor odinson', 'yelena belova', 'spider-man', 'iron man', 'captain america', 'human torch', 'doctor strange', 'jean gray', 'valkyrie', 'deadpool', 'bucky branes', 'scarlet witch', 'vision', 'gamora', 'star lord', 'thanos', 'black widow', 'adam warlock', 'hellstorm', 'watcher', 'daredevil', 'nick fury', 'black panther', ]
loser_quotes = ['There is no such letter!', 'What are you talking about? Not true!', 'Let them open it, but not in this word. (no such letter)', 'H-Hm (the wrong letter sounds)']
fortune_wheel_cases = ['health', 'letter reveal', 'health', 'health', 'health', 'letter reveal', 'health', 'health', 'health', 'health', 'minus health', 'minus health', 'minus health', 'minus health', 'minus health', 'minus health', 'minus health', 'minus health', 'letter reveal']
LETTERS = string.ascii_lowercase
win_counter = 0



# Creates a short history of a main character

def prehistory():
  print()
  print('** Billy was kidnaped by a guy, his face was quite familiar to him,\n but a young boy couldn\'t recognise a stranger because he lost consciousness\n')
  time.sleep(4)
  print("** After regaining consciousness Billy realised that he is in a big trouble\n")
  time.sleep(3)
  print("** He were lying tied up in an unknown room, it was dark around\n")
  time.sleep(2)
  print("** Billy thought **\n")
  time.sleep(1)
  print("Ohhhh crap!!")
  time.sleep(1)
  print("Where the hell, I am? I need to escape from here!\n")
  time.sleep(2)
  print("** The boy saw a pair of scissors lying in front of him\n")
  time.sleep(2)
  print("** He was trying to pick them up\n")
  time.sleep(2)
  print("** Struggling to pick up scissors\n")
  time.sleep(3)
  print("Finnaly he did it! It was easier than Billy thought.\n")
  time.sleep(2)
  print("** After that he tried to сut a rope\n")
  time.sleep(2)
  for i in range(1, 6):
      print(i)
      time.sleep(1)
  print()
  print("Damn it, scissors broke.\n")
  time.sleep(2)
  print("** Suddenly Billy heared some steps\n")
  time.sleep(2)
  print("** Somebody enters a room **\n")
  time.sleep(2)
  print("Oh no!\n")
  time.sleep(2)
  print("** A feeling of fear filled him\n")
  time.sleep(2)
  print("** Billy saw his face. It was Леонид Якубович\n")
  time.sleep(2)
  print("** He would rather meet any of the most dangerous persons in the world, but not him\n")
  time.sleep(2)
  print("** Якубович replied **\n")
  time.sleep(2)
  print(" Добрый вечер! Здравствуйте, уважаемые дамы и господа!\n")
  time.sleep(2)
  print(" Пятница!\n")
  time.sleep(2)
  print(" В эфире капитал-шоу «Поле чудес»!\n")
  time.sleep(2)
  print(" И как обычно, под аплодисменты зрительного зала я приглашаю в студию первую тройку игроков.\n")
  time.sleep(2)
  print(" Первая тройка, в студию!\n")
  time.sleep(2)
  print("** Lights turned on **\n")
  time.sleep(2)
  print("** Young boy saw a two other victims near him\n")
  time.sleep(2)
  print("** He understood that the only chance to escape is to win the \"Поле чудес\"")
  time.sleep(2)
  print()
  print("** Help Billy to win the game and become free, complete 3 rounds **")



# Pick up a category

def category_picker():
 not_found = True
 while not_found:
  print()
  print('Choose a category: \n1. Animals\n2. Countries\n3. Cars\n4. Dota characters\n5. Marvel characters')
  print()
  category = input(">>> ")
  spacing(8)
  if category not in categories:
    print('*   Uppps... We dont have this category. Follow the rules or you will be punished!   *')
  else:
    not_found = True
    return category.lower()



#  Generates a random word

def random_word_generator():
  category = category_picker()
  if category == 'animals':
    random_word = random.choice(animal_topic_list)
  elif category == 'cars':
    random_word = random.choice(cars)
  elif category == 'marvel':
    random_word = random.choice(marvel_characters)
  else:
    random_word = random.choice(dota_characters)
  return random_word



#  Generates a list with hidden letters

def hidden_word_to_guess(random_word):
  guess = []
  for i in random_word:
    if i != ' ':
      guess.append('_')
    else:
      guess.append(' ')
  guess[0] = random_word[0]
  guess[-1] = random_word[-1]
  return guess



# Creates a game field

def draw(used_letters, guesses_list, health):
  used_letters = set(used_letters)
  for i in guesses_list:
    print(i, end=" ")
  spacing(2)
  print(f'Used letters: {[*used_letters]}')
  print()
  print(f'Lives remained: {health}')
  print()



# Spacing

def spacing(amount):
  for _ in range(amount):
    print()



# Round generator 

def round():
  counter = 0
  used_letters = []
  round_run = True
  health = 7
  random_word = random_word_generator()
  guesses_list = hidden_word_to_guess(random_word)

  while round_run and health > 0:
    draw(used_letters, guesses_list, health)
    print('Write a letter: ')
    guessed_letter = input('>>> ')
    if guessed_letter not in LETTERS or guessed_letter == '':
      print()
      print('*   Come on?! It\'s not even a letter!  *')
      time.sleep(1)
      spacing(7)
    elif guessed_letter in used_letters:
      print()
      print('*   Do not repeat yourself!  *')
      time.sleep(1)
      spacing(7)
    elif guessed_letter in random_word[1:-1]:
      for i in range(len(random_word)):
        if random_word[i] == guessed_letter:
          guesses_list[i] = guessed_letter
          used_letters.append(guessed_letter)
      counter += 1
      print()
      print("*   Correct letter!   *")
      time.sleep(1)
      spacing(8)
    else:
      print()
      print(f"*   {random.choice(loser_quotes)}   *")
      time.sleep(1)
      spacing(7)
      health -= 1
      counter = 0
      used_letters.append(guessed_letter.lower())
    if counter == 3 and '_' in guesses_list:
      print()
      print('You guessed 3 letters in a row, now you got a fortune wheel. It can be a blessing or a curse for you.\n\n* Would you like to try it? (Yes / No)\n')
      response = input('>>> ')
      spacing(11)
      if response.lower() == 'yes':
        print("*   Spinning a wheel!!!   *\n")
        time.sleep(4)
        case = random.choice(fortune_wheel_cases)
        if case == 'health':
          print("You won a free life, lucky boy!")
          time.sleep(2)
          health += 1
          spacing(7)
        elif case == 'letter reveal':
          print("Holy wheel, you won a free letter reveal\n")
          time.sleep(2)
          print(f'*   Write a letter position in a word (0 - {len(random_word) - 1})  *\n')
          print(" ".join(guesses_list))
          print()
          try:
            position = int(input('>>> '))
          except:
            spacing(10)
            print("Follow the rules!")
            time.sleep(2)
            spacing(10)
            health -= 1
            continue
          spacing(7)
          if position > len(random_word) - 1 or position < 0:
            spacing(8)
            print("Hmmm... You are not following the rules, right?")
            health -= 1
            time.sleep(2)
            spacing(10)
          elif guesses_list[position] == " ":
            spacing(10)
            print("Oh , you picked up a white space... Nevermind, try to be more attentive")
            time.sleep(2)
            spacing(7)
          else:
            guesses_list[position] = random_word[position]
        elif case == 'minus health':
          print("Oh baby boy, you are missing 1 life")
          time.sleep(2)
          health -= 1
          spacing(7)
        counter = 0
      else:
        continue
    if not "_" in guesses_list:
      global win_counter
      win_counter += 1
      round_run = False



# Main function 

def main():
  prehistory()
  for i in range(1, 4):
    print()
    print(f"Round {i}")
    round()
  if win_counter > 2:
    spacing(10)
    time.sleep(1)
    print("** Billy opened his eyes and saw the sky\n")
    time.sleep(2)
    print("** He was feeling sick and tired\n")
    time.sleep(2)
    print("** He was lucky to be free, but some thoughts didn\'t leave him. It was thoughts about yesterday Friday\n")
    time.sleep(2)
    print("** He said thanks to God and to unknown person who made him win")
    spacing(3)
    print("**  Congrats, you won and saved Billy!  **")
    spacing(3)
  else:
    spacing(10)
    print('** Hahahahahah, you lost\n')
    time.sleep(1)
    print('** Billy is never gonna see the world, again')
  



if __name__ == "__main__":
  main()