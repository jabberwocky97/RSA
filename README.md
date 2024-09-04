# RSA Algorithm Implementation
This project implements the RSA cryptographic algorithm using Python. RSA is a widely-used asymmetric encryption algorithm that relies on the mathematical properties of prime numbers to secure data.


## Components

### `rsa.py`

This script contains the core RSA functionality:

- **`rand_num()`**: Generates a random number with a specific bit pattern. Used for prime generation.
- **`primality_test(n)`**: Tests if a number `n` is prime using the Miller-Rabin primality test.
- **`fastExp(a, x, n)`**: Computes modular exponentiation efficiently.
- **`euclid(a, b)`**: Uses the Extended Euclidean Algorithm to compute the greatest common divisor and coefficients.
- **`eFinder(phi)`**: Finds a valid `e` (public exponent) that is coprime with φ(n) and calculates the modular inverse `d`.
- **`display(string)`**: Formats binary strings to 32-bit length for display purposes.
- **`main()`**: Executes the RSA key generation process, including selecting primes, calculating `n`, φ(n), `e`, and `d`, and displaying the results.

### `test.py`

This script provides utility functions for testing and random number generation:

- **`testPrimality(num)`**: Checks if a number is prime.
- **`getRandomInt()`**: Generates a random 7-bit integer.

## Installation

1. Clone the Repository or copy the source code from both `rsa.py` and `test.py`

2. Navigate to the Project Directory:
   ```bash
   cd RSA
   ```

3. Install Dependencies:
   Ensure you have Python 3.12 or higher installed. 


## Usage

1. Generate RSA Keys:
    - Run the `rsa.py` script to generate RSA keys.
    - The script will print the primes `p` and `q`, their product `n`, φ(n), the public exponent `e`, and the private exponent `d`.

   ```bash
   python rsa.py
   ```

2. Understand the Output:
    - **Primes (`p` and `q`)**: Two randomly selected prime numbers.
    - **`n`**: The product of `p` and `q`, used as the modulus for encryption and decryption.
    - **φ(n)**: Euler's totient function of `n`.
    - **`e`**: Public exponent chosen to be coprime with φ(n).
    - **`d`**: Private exponent, calculated as the modular inverse of `e` modulo φ(n).

   Example output:
   ```
   ---------------------------------------------------------------------------------------------------
   ---------------------------------------------------------------------------------------------------
   ---------------------------------------------------------------------------------------------------
   p and q are: 101, 73
   n = p x q = 101 x 73 = 7373

   (p-1)(q-1)= 7200

   Calculating e:

   s(n): 0   t(n): 1
   gcd of e = 3 and 7200 is not 1

   s(n): 0   t(n): 1
   gcd of e = 4 and 7200 is not 1

   s(n): 0   t(n): 1
   gcd of e = 5 and 7200 is not 1

   s(n): 0   t(n): 1
   gcd of e = 6 and 7200 is not 1

   7200 = 1028 x 7 + 4  ......s[i]: 1  t[i]: 0
   7 = 1 x 4 + 3  ......s[i]: 0  t[i]: 1
   4 = 1 x 3 + 1  ......s[i]: 1  t[i]: -1028
   3 = 3 x 1 + 0  ......s[i]: -1  t[i]: 1029
   s(n): 2   t(n): -2057
   e = 7   d = 5316

   p: 00000000000000000000000001100101
   q: 00000000000000000000000001001001
   n: 00000000000000000001110011001101
   e: 00000000000000000000000000000111
   d: 00000000000000000001010011000100
   ```

## Code Explanation

### `rsa.py`

- **`rand_num()`**: Generates a random number with a specific bit pattern for prime generation.
- **`primality_test(n)`**: Tests if a number `n` is prime using the Miller-Rabin primality test.
- **`fastExp(a, x, n)`**: Computes modular exponentiation efficiently.
- **`euclid(a, b)`**: Uses the Extended Euclidean Algorithm to compute the greatest common divisor and coefficients.
- **`eFinder(phi)`**: Finds a valid `e` (public exponent) that is coprime with φ(n) and calculates the modular inverse `d`.
- **`display(string)`**: Formats binary strings to 32-bit length for display purposes.
- **`main()`**: Executes the RSA key generation process, including selecting primes, calculating `n`, φ(n), `e`, and `d`, and displaying the results.


### `test.py`

- **`testPrimality(num)`**: Checks if a number is prime.
- **`getRandomInt()`**: Generates a random 7-bit integer.

