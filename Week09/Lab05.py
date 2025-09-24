# Question1
def get_name(name_dict, id_num):
    if (id_num in name_dict):
        return name_dict[id_num]
    else:
        return None

# Question2 
def word_counter(input_str):
    word_list = input_str.lower().split(' ')
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        elif word != '' and word != ' ':
            word_dict[word] = 1
    return word_dict

# Question3
def find_key(input_dict, value):
    key_lst = input_dict.keys()
    for i in key_lst:
        if input_dict[i] == value:
            return i
    return None

# Question4
def make_index(words_on_page):
    '''
    input_dict = {1: ['hi', 'there', 'fred'], 2: ['there', 'we', 'go'],3: ['fred', 'was', 'there']}
    '''
    value_list = list(words_on_page.values()) 
    '''[[],[],[]]'''
    
    index_list = list(words_on_page.keys()) 
    ''' [1,2,3]'''
    result= {}
    length = len(index_list)
    for i in range(length):
        for j in value_list[i]:
            if j in result:
                result[j].append(index_list[i])
            else:
                result[j] = [index_list[i]]
    return result
make_index({1: ['hi', 'there', 'fred'], 2: ['there', 'we', 'go'],3: ['fred', 'was', 'there']})

# Q5
def make_dictionary(filename):
    word_list = []
    with open(filename, "r") as f:
        for line in f:
            striped_line = line.strip()
            if striped_line:
                word_list.append(striped_line)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


# Question 6
def isbn_dictionary(filename):
    data = []

    try:
        with open(filename,'r') as file:
            for line in file:
                line = [value for value in line.strip().split(",")]
                data.append(line)
    except FileNotFoundError:
        print("The file", filename, "was not found.")
        return None
    result = {}
    for info in data:
        result[info[-1]] = (info[0], info[1])
    return result

# Question 7
def long_enough(strings, min_length):
    result = []
    for s in strings:
        if len(s) >= min_length:
            result.append(s)
    return(result)

# Question 8
def my_enumerate(items):
    result = []
    for i in range(len(items)):
        result.append((i, items[i]))
    return(result)

# Question 9
def run_length_encode(data):
    result = []
    buffer = []
    for i in data:
        if not i in buffer:
            encode_tuple = (i, data.count(i))
            result.append(encode_tuple)
            buffer.append(i)
    return result
# print(run_length_encode([5,5,5,10,10,10,114,11,30,30]))

# Question 10
def composite2(N):
    def is_composite(num):
        if num <= 3:
            return False
        
        for i in range(2,num,1):
            if num % i == 0:
                return True
        return False
    
    count = 0
    num = 4
    while True:
        if is_composite(num) and num % 2 != 0:
            count += 1
            if count == N:
                return num
        num += 1
# print(composite2(3))
# print(composite2(5))

# Q 11
def series(x):
    init_num = 1
    result = 0
    while init_num >= x:
        result += init_num
        init_num /= 2
    return round(result,4)
# print(series(0.5))
# print(series(0.25))
# print(series(0.01))

# Q 12
def nextRound(k,scores):
    '''
        k -> int
        scores -> list(int)
    '''
    # Rank all the scores
    score_dict = {}
    rank = 0
    buffer = -1
    scores.sort(reverse=True)
    for score in scores:
        if score == buffer:
            score_dict[rank].append(score)
        else:
            rank += 1
            score_dict[rank] = [score]
            buffer = score        

    count = 0
    for i in range(1, k+1, 1):
        try:
            for j in score_dict[i]:
                if j != 0:
                    count += 1
        except KeyError:
            return count
    return count

# print(nextRound(5,[10,9,8,7,6,6,6,5,4]))
# print(nextRound(2,[0,0,0,0]))

# Q 13
def singleDigit(N):
    # Saperate the last digit

    # Add it to the result

    # keep saperate until the result is smaller than 10

    # Recurssion!!!!!!!!!!!
    if N < 10:
        return N
    else:
        result = 0
        while N != 0:
            result += N%10
            N //= 10
        return singleDigit(result)

# print(singleDigit(48))
# print(singleDigit(198))

# Q14
def sequence(n):
    # Recurssion

    # Base Case: it reaches one

    # Recursive case: not reach one
    result = []
    def recursion_sequence(n):
        result.append(n)
        if result[-1] == 1:
            return result
        else:
            if result[-1] % 2 == 0:
                new_num = result[-1] // 2
                return recursion_sequence(new_num)
            elif result[-1] % 2 == 1:
                new_num = (result[-1] * 3 + 1)
                return recursion_sequence(new_num)
    return recursion_sequence(n)
# print(sequence(12))
# print(sequence(20))

# Q 15
class car:
    def __init__(self):
        self.model = ''
        self.rego = ''
        self.year = 0
        self.color = ''
    def setModel(self, model_name):
        self.model = model_name
    
    def setRego(self,rego_name):
        self.rego = rego_name

    def setYear(self,year_num):
        self.year = year_num
    
    def setColor(self,color_str):
        self.color = color_str
    
    def getModel(self):
        return self.model
    
    def getRego(self):
        return self.rego

    def getYear(self):
        return self.year
    
    def getColor(self):
        return self.color

'''
c1 = car()
c1.setModel('Honda Accord')
print(c1.getModel())
'''

# Q 16
class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def setName(self,name_Str):
        self.name = name_Str
    
    def getName(self):
        return self.name
    
    def setAge(self, age_Int):
        self.age = age_Int
    
    def getAge(self):
        return self.age
    
    @staticmethod
    def setSport(sportName):
        player.sport = sportName
    
    @staticmethod
    def getSport():
        return player.sport
    
p1 = player("Ronaldo",37)
print(p1.getName())
player.setSport('Blyat')
print(p1.getSport())