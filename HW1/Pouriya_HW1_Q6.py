def isPrime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, (int(n**(0.5))) + 1):
        if n % i == 0:
            return False
    return True

A, B = map(int, input('enter your searching range: '.title()).split())

prime_list = [i for i in range(A+1, B) if isPrime(i)]
print(prime_list)
