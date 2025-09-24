'''
Define a Python function stringexpand(name) which, given a string name, returns the
expanded string such that white space is added after each character of the input string.
For example, stringexpand(“Adam”) returns “A d a m”.
'''
def stringexpand(name):
    if len(name) == 1:
        return name[0]
    else:
        return name[0] + " " + stringexpand(name[1:])

'''
Q2
'''
def palindrome(word):
    word_reverse = ""
    word = word.lower()
    length = len(word)
    if length % 2 == 0:
        for i in range(length):
            if word[i] != word[-i - 1]:
                return False
        return True
    else:
        half_len = length // 2
        for i in range(length):
            if word[i] != word[-i - 1]:
                return False
            if i == half_len:
                return True
        return True
'''
Q3
'''
def sortdict(dict):
    result = []
    for i in dict:
        result.append((i,dict[i]))
    result = sorted(result, key=lambda x:x[1], reverse= True)
    return result

'''
Q4
'''
def sumdigits(n):
    if n < 10 :
        return n
    else :
        return n % 10 + sumdigits(n // 10)
    
'''
Q5
'''
def seriesexp(x,tol):
    def factorial(num):
        '''
            this function returns the factorial using recursion
        '''
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num-1)
    result = 0
    count = 0
    current = 0
    while True:
        current = (x ** count) / factorial(count)
        if current < tol :
            break
        result += current
        count += 1

    return result

'''
Q6
'''
def multiply_lists(lst):
    result = 1
    for i in lst:
        if type(i) != list:
            result *= i
        else:
            result *= multiply_lists(i)
    return result

'''
Q7
'''
def team_maker(pool1,pool2,pool3):
    result = []
    for i in pool1:
        for j in pool2:
            for k in pool3:
                result.append(i + ' ' + j + ' ' + k)
    return result
print(team_maker(['Smith','Finch'],['Cummins','Lyon'],['Adam','Payne']))

'''
Q8
'''
def user_account(filename):

    def find_name_position(row1,keyword):
        for i in range(len(row1)):
            if row1[i] == keyword:
                return i
    
    data = []
    try:
        with open(filename,'r') as datafile:
            for line in datafile:
                line = [value.strip for value in line.strip.split(',')]
                data.append(line)
    except FileNotFoundError:
        return "File not found"
    # create reference
    fName = find_name_position(data[0],"First name")
    lName = find_name_position(data[0],"Last name")
    dob = find_name_position(data[0],"Date of birth")

    # create password
    passwd = []
    for row in data[1:]:
        DOB = row[dob]
        DOB = DOB.split('/')
        pwdob = dob[0] + dob[1]+ dob[2]
        passwd.append(row[fName] + '.' + row[lName] + ',' + row[lName] + '$' + pwdob)
    try:
        with open('logins.txt','w') as login:
            for i in passwd:
                login.write(i + '\n')
    except FileExistsError:
        return "File Exists Error"