# Prime numbers
def check_prime_number(num):
    if num <= 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primeN(N):
    result = []
    for i in range(N):
        if check_prime_number(i):
            result.append(i)
    return result