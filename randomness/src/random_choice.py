import random

deck = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC','J', 'J']

def basic_use_of_rand():
  '''
  This function shows the basic use of random function
  '''
  random.seed(62)
  hello = random.choice(deck)
  return hello

def random_with_choice_and_sample_attribute(option='choice'):
  '''
  The output when using choice may contain duplicates
  Even method choices will have duplicates
  the random.sample method will not have duplication
  '''
  cards = []
  for _ in range(0,15):
    cards.append(random.choice(deck))
  if (option == 'choice'):
    return cards
  else:
    return random.sample(deck,k=15)

def random_with_shuffle():
  '''
  Shuffle method - need to input mutable list. Once we shuffle it the original sequence is lost
  '''
  print('Shuffle')
  random.shuffle(deck)
  return deck

def retain_original_sequence_and_shuffle():
  '''
  You cannot assign the output of shuffle to a variable, it will return 'None',
  because it does the operation on the original list
  '''
  deck2 = deck[:]
  return random.shuffle(deck2)

print(basic_use_of_rand())
print(random_with_choice_and_sample_attribute())
print(random_with_shuffle())
