'''
Generate deck of cards 
It's composed in this manner:

There are four suits; hearts, spades, diamonds, and clubs (H, S, D, C).
Each suit has one card for the numbers 2 to 10, plus 4 'picture' cards, Ace, Jack, Queen, and King (A, J, Q, K).
For each combination of suit and value, there should be one item in the array, which is a string, and is made up of the value followed by the suit (Whitespace between these is permitted).
On top of that, there are two Joker cards ('J').
Write in any language you please.
Golf it up! Try to produce this output in the smallest number of bytes.
It does not matter what order the output is in.
'''
print(*[a+b for a in['10',*'A23456789JQK']for b in'CHSD'],*'JJ')