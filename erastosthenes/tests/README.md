# MOCK function

The unittest.mock.patch [has][1] several keywrod arguments. But in our case, it simply replaces the built-in input() function with `unittest.mock.MagicMock` object.

Mock is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks.

[ 1 ]: https://docs.python.org/3/library/unittest.mock.html#patch
