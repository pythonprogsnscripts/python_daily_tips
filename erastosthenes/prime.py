'''
Sieve of Eratosthenes is used to get all prime number in a given range and is a very efficient algorithm.
More information of this process is listed in README.md
'''
import math

number = int(input('Enter a number: '))

primes = []
for i in range(2,number+1):
    primes.append(i)

def sieve_algo():
    '''
    Implementing Sieve algorithm
    '''
    i = 2
    while(i <= int(math.sqrt(number))):
    #if i is in list, then delete its multiples
        if i in primes:
            #j will give multiples of i, starting from 2*i
            for j in range(i*2, number+1, i):
                if j in primes:
                    #deleting the multiple if found in list
                    primes.remove(j)
        i = i+1
    return primes

print(sieve_algo())