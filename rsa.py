from random import randint
from test import testPrimality, getRandomInt


def rand_num():
    """
    Generates a 32-bit integer with the first and last bits set to 1,
    and 5 random bits in between.
    """
    # Initialize the binary string with 25 leading '0's and ending with '1'
    string = '0' * 25 + '1'


    # Generate 5 random bits and append them to the string
    bits = [randint(1, 10) % 2 for _ in range(5)]
    for bit in bits:
        print(f"{bit} mod 2 = {bit % 2}")
        string += str(bit % 2)


        print(string)
        print(int(string, 2))
        return int(string, 2)


    # Append '1' to the end of the string to complete the 32-bit integer
    string += '1'
    result = int(string, 2)
    print(string)
    print(result)
    return result


def primality_test(n):
    """
    Performs the Miller-Rabin primality test on a number.
    Returns the number if it is possibly prime, otherwise 0.
    """
    count = 0
    arr = []
    # Perform the test with 20 different values of 'a'
    while count < 20:
        a = 0
        # discard the # if a is 0
        while a == 0:
            a = rand_num() % n
        # checks to see if a has been checked already
        if a > 0 and a not in arr:
            print(f"\na = {a}")
            arr.append(a)
            count += 1
            # Use modular exponentiation to test primality
            if fastExp (a, n-1, n) !=1:
                print(f"{a}^{n - 1}(mod {n}) != 1")
                print(f"\n{n} is not prime. Fails primality test when a = {a}\n\n")
                return 0


            # If 20 values of 'a' pass the test, declare the number as possibly prime
            if count == 20:
                print(f"{n} is possibly prime")
                print("------------------------------")
                return n

            # If the test says it is possibly a prime, look for another
            # number that you know not to be a prime.



def fastExp(a, x, n):
    """
    Performs modular exponentiation using binary exponentiation.
    """
    # Convert the exponent 'x' to binary
    bin_exp = bin(x)[2:]
    print(f"Binary exponent: {bin_exp}\n")
    ans = 1
    temp = a


    # Perform binary exponentiation
    for char in bin_exp:
        ans = (ans ** 2) % n
        if char == "1":
            ans = (ans * temp) % n
        print(f"{char}   {temp}^2(mod {n})   {ans} x {temp}")
        temp = ans

    return ans


def euclid(a, b):
    """
    Computes the greatest common divisor (GCD) of 'a' and 'b'
    using the Euclidean algorithm. Also computes the coefficients
    for the extended Euclidean algorithm.
    """
    high = max(a, b)
    low = min(a, b)
    remainder = high % low
    i = 0

    # Arrays to keep track of quotients and coefficients
    qi = []
    si = [1, 0]
    ti = [0, 1]

    # Apply the Euclidean algorithm
    while remainder != 0:
        i += 1
        temp = remainder
        mult = high // low  # Integer division
        qi.append(mult)

        # Update coefficients for extended Euclidean algorithm
        if i >= 2:
            si.append(si[-2] - qi[-2] * si[-1])
            ti.append(ti[-2] - qi[-2] * ti[-1])
        remainder = high - (mult * low)
        print(f"{high} = {mult} x {low} + {remainder}  ......s[i]: {si[i - 1]}  t[i]: {ti[i - 1]}")
        high = low
        low = remainder

    # Ensure `temp` is correctly assigned when the loop ends
    if remainder == 0:
        temp = high

    print(f"s(n): {si[-1]}   t(n): {ti[-1]}")
    return (temp, ti[-1])


def eFinder(phi):
    """
    Finds a suitable value for 'e' that is coprime with 'phi'
    and computes the modular inverse of 'e' modulo 'phi'.
    """
    e = 3
    # use fast euclidean to get the gcd and ti
    gcd, ti = euclid(e, phi)
    while gcd != 1:
        print(f"gcd of e = {e} and {phi} is not 1\n")
        e += 1
        gcd, ti = euclid(e, phi)
    return (e, ti)


def display(string):
    """
    Pads the binary string with leading zeros to ensure it is 32 bits long.
    """
    return string.rjust(32, '0')


def main():
    """
    Main function to demonstrate RSA key generation and display results.
    """
    p, q = 0, 0

    print("---------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------")

    # Find two distinct prime numbers p and q
    while p == 0:
        num = getRandomInt()
        p = testPrimality(num)
    while q == 0 or q == p:
        num = getRandomInt()
        q = testPrimality(num)

    print(f"p and q are: {p}, {q}")
    n = p * q
    print(f"n = p x q = {p} x {q} = {n}\n")

    # Compute phi and find e and d
    phi = (p - 1) * (q - 1)
    print(f"(p-1)(q-1)= {phi}\n\nCalculating e: \n")
    e, ti = eFinder(phi)

    # Normalize d if negative
    d = ti + n if ti < 0 else ti
    print(f'e = {e}   d = {d}')

    # Display binary representations of p, q, n, e, and d
    print(f"\np: {display(bin(p)[2:])}")
    print(f"q: {display(bin(q)[2:])}")
    print(f"n: {display(bin(n)[2:])}")
    print(f"e: {display(bin(e)[2:])}")
    print(f"d: {display(bin(d)[2:])}")

if __name__ == "__main__":
    main()