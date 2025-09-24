# Prime numbers
def check_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primeN(N):
    result = []
    for i in range(N+1):
        if check_prime_number(i):
            result.append(i)
    return result

def Nprime(n):
    primelist = []
    count = 0
    currentNum = 0
    while count <= n:
        if check_prime_number(currentNum):
            primelist.append(currentNum)
            count += 1
        currentNum += 1
    return primelist