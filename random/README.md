# Info on Random function

One of the most useful function in Python is the random function. It's also called as Pseudo Random Number Generator or PRNG.

The random function provides pseudo randomness, put simply the random data generated from random's methods are not random. A true random number generated would be True Random Number Generator (TRNG). For eg: rolling a dice.

## What makes random pseudo random?

Random has a method random, which generates random number between 0 and 1.
`0 <= n < 1`

The random number generated using the random function is inclusive of value 0 and exclusive of 1.

``` 
>>> random.random()
0.5719304361110644
>>> random.random()
0.9928294047230436
```
Under the hood the algorithm used is `Mersenne Twister `

numpy also do have a random method
