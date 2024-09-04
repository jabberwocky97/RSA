from random import randint

def testPrimality(num):
    # Simple primality test
    if num <= 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return num

def getRandomInt():
    return randint(2**6, 2**7 - 1)  # Generate a random 7-bit integer
