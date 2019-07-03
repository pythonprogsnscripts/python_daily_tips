import pytest
from randomness.src import random_choice as rand, generate_deck_of_cards as deck

def test_random_with_seed():
    seed = rand.basic_use_of_rand()
    assert seed == '9C'

def test_random_shuffle_function():
    shuffle_list = rand.random_with_shuffle()
    assert 'J' in shuffle_list
    
def test_generate_deck_of_cards():
    cards = deck.generate_deck_of_cards()
    assert '2D' in cards