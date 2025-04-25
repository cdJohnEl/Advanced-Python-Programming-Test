"""
5. Generators and Iterators
Create a generator function `prime_gen()` that yields an infinite sequence of prime numbers. Then,
write code to retrieve the first 10 primes.
"""



def prime_gen():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):  
            if num % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_generator = prime_gen()
for p in range(10):
    print(next(prime_generator))
