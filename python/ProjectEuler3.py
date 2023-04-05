from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

index = 2
num = 600851475143
maxPrime = None

while index <= num:
    if isPrime(index) and num % index == 0:
        num /= index
        maxPrime = index
    index += 1
    print index

print maxPrime
