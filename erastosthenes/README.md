# Sieve of Eratosthenes Algorithm

The sieve alogrithm is an efficient algorithm to get all prime numbers in a given range.

Below are the steps of the algorithm:

1. Make a list of all numbers from 2 to n.

    `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ……., n]`

2. Starting from 2, delete all of its multiples in the list, except itself.

    `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,……., n]`

3. Repeat the step 2 till square root of n

    `For 3 –  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
For 5 – [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
Till sqrt(n)`

The remaining list only contains prime numbers
