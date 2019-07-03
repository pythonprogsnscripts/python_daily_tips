from randomness.src import random_choice as rand, generate_deck_of_cards as cards
from randomness.src.random_choice import deck
def test_random_with_seed():
    seed = rand.basic_use_of_rand()
    assert seed == '9C'

def test_random_shuffle_function():
    shuffle_list = rand.random_with_shuffle()
    assert 'J' in shuffle_list

def test_generate_deck_of_cards():
    card = cards.generate_deck_of_cards()
    assert '2D' in card

def test_random_with_choice_option():
    card = rand.random_with_choice_and_sample_attribute()
    assert '10S' in card
