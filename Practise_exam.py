# Q1
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:   
        return fib(n-1) + fib(n-2)
# Q2
def Fibonacci(n):
    count = 0
    result = []
    while True:
        if count == 0 or count == 1:
            result.append(1)
            count += 1
        else:
            result.append(result[-1] + result[-2])
            count += 1
        if count == n:
            break
    return result
# print(Fibonacci(10))

# Q3
def FibonacciSum(n):
    return sum(Fibonacci(n))

# Q4
def FibonacciFilter(n):
    sequence = Fibonacci(n)
    remove = []
    for i in range(len(sequence)):
        if not (sequence[i] % 2 == 0 or sequence[i] % 5 == 0):
            remove.append(i)
    for i in range(len(remove)-1,0,-1):
        sequence.pop(remove[i])
    return sum(sequence), sequence

# Q5
def num_to_word(n):
    ten = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
    }
    one = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Tweleve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    if n in ten:
        return ten[n]
    elif n in one:
        return one[n]
    else:
        return ten[n//10] +' ' + one[n%10]

# Q6
def matrices_add(mat1 : list, mat2: list):
    if len(mat1) == len(mat2):
        for i, j in mat1, mat2:
            if len(i) != len(j):
                print("Invalid input")
                return []
        result = []
        for i in range(0,len(mat1)):
            inner_list = []
            for j in range(0,len(mat1[i])):
                inner_list.append(mat1[i][j] + mat2[i][j])
            result.append(inner_list)
        return result
    else:
        print("Invalid Input")
        return []
# print(matrices_add([[1,2],[3,4]], [[1,2],[3,4]]))

# Q7
def num2str(n):
    return num_to_word(n)

# Q8
def mergelists(list1, list2):
    if len(list1) != len(list2):
        print("Invalid input")
        return []
    result = []
    for i, j in zip(list1, list2) :
        result.append(i)
        result.append(j)
    return result

# Q9
def sortoddeven(nums):
    odd = []
    even = []
    for i in nums:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    return sorted(odd) + sorted(even)

# Q10
# matrix multiply
def matrix_multiply(mat1:list,mat2:list):
    '''
    mat1: [[nums],[nums]]
    mat2:[[nums],[nums]]
    '''
    mat1_row = len(mat1)
    mat1_column = len(mat1[0])

    mat2_row = len(mat2)
    mat2_column = len(mat2[0])
    
    # initialize result
    result = []
    for i in range(mat1_row):
        row = []
        for j in range(mat2_column):
            num = sum(mat1[i][k] * mat2[k][j] for k in range(mat1_column))
            row.append(num)
        result.append(row)
    return result
print(matrix_multiply([[1,2],[3,4]],[[1,2],[3,4]]))
