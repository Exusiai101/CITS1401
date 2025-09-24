# Prime numbers
def check_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True