import unittest.mock as mock

number = 10
def test_accept_input():
    with mock.patch('builtins.input', return_value=number):
        assert input() == 10

prime = []
def test_append_prime():
    for i in range(2,number +1):
        prime.append(i)
    assert 3 in prime