def factorial(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result

def square_sum(x):
    result = 0
    if x < 0:
        while x < 0:
            result += x ** 2
            x += 1
        return result
    if x > 0:
        while x > 0:
            result += x ** 2
            x -= 1
        return result

def sum_odd_nums(target_counts):
    def check_odd_nums(num):
        if num % 2 == 0:
            return False
        else:
            return True
    # 1, 3, 5, 7, 9, 11.
    # input = 3, return: 1 + 3 + 5 = 9
    # input = 4, return 1 + 3 + 5 + 7 = 16
    num = 1
    result = 0
    count = 0
    while True:
        if count == target_counts:
            return result
        if check_odd_nums(num):
            result += num
            num += 1
            count += 1
        else:
            num += 1

def Caculate_Fibonacci(x):
    if x <= 1:
        return 0
    elif x == 2:
        return 1
    else:
        return Caculate_Fibonacci(x-1) + Caculate_Fibonacci(x-2)
    


def Sum_Fibonacci(n):
    result = 0
    if n == 0:
        return 0
    else:
        for i in range(n+1):
            result += Caculate_Fibonacci(i)
        return result

x = int(input(""))
print(Caculate_Fibonacci(x))