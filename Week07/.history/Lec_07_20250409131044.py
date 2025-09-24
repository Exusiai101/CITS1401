# Prime numbers
def check_prime_number(num):
    for i in range(1, num+1):
        if num % i != 0:
            return False
    return True