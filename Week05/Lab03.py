def my_abs(value):
    if value < 0:
        return 'positive'
    elif value > 0:
        return 'negative'
    else:
        return "zero"
    
def is_odd(number):
    return number % 2 == 1

def bmi_risk(bmi,age):
    if bmi < 22 and age < 45:
        return "Low"
    elif bmi < 22 and age >= 45:
        return "Medium"
    elif bmi >= 22 and age < 45:
        return "Medium"
    else:
        return 'High'
    
def buy_goods(cost, saving):
    return cost/saving <= 0.05

def record_check(age, gender, location):
    if age > 18 and gender == "M" and (location == "Perth" or location == "Sydney"):
        print('Found him!')
    else:
        print("Did not find him.")

def balance_list(items):
    length = len(items)
    if length % 2 == 1:
        items.append(items[length - 1])
        return items
    else:
        return items
    
def double_list(items):
    length = len(items)
    if length % 2 == 0:
        for i in range(length):
            items.append(items[i])
        return items
    else :
        items.append(items[length - 1])
        return items

def are_anagrams(word1,word2):
    list1,list2 = list(word1),list(word2)
    list1_sorted ,list2_sorted = list(word1),list(word2)
    list1_sorted.sort()
    list2_sorted.sort()

    if list1 != list2 and list1_sorted == list2_sorted:
        return True
    else:
        return False

def locate_person(age_list, name_list, age, name):
    length = len(age_list)
    for i in range(length):
        if age_list[i] == age and name_list[i] == name:
            return i

def hunting_animals(weather, animal, n) :
    assert n>0
    assert weather == 'rainy' or weather == "sunny"
    sunny_bullet_cost = {'rabbit': 1,'deer': 2}
    rainy_bullet_cost = {"rabbit": 2, 'deer': 3}
    if weather == "sunny":
        return n // sunny_bullet_cost[animal]
    else:
        return n // rainy_bullet_cost[animal]

def check_temperature(temperature, limit):
    temperature = temperature * 9 / 5 + 32
    if temperature < limit:
        return True
    else :
        return False
#print(check_temperature(30.0, 140))
#print(check_temperature(30.0, 80.0))

def compare_strings(string1, string2):
    if string1[0] == string2[0]:
        if len(string1) == len(string2):
            return 'error'
        elif len(string1) > len(string2):
            return string1
        else :
            return string2
    else :
        if string1[-1] > string2[-1] :
            return string1
        elif string1[-1] < string2[-1] :
            return string2
        else :
            return "error"
#print(compare_strings("band", "bread"))
#print(compare_strings("sky", "cloud"))

def can_jump(speed, power, name, injured):
    if injured == True:
        meters = speed * power * 0.8
        if meters < 1 :
            return name + ' made a false attempt!'
        return name + ' can jump ' + '%.2f' %meters + "m!"
    else :
        meters = speed * power
        if meters < 1 :
            return name + ' made a false attempt!'
        return name + " can jump " + '%.2f' %(speed * power) + 'm!'
    
def should_shutdown(battery_level, time_on):
    if time_on < 60 and battery_level < 4.7 :
        return True
    elif time_on >= 60 and battery_level <4.8 :
        return True
    else :
        return False
    
def gcd(int1, int2): # The Greatest Common Divisor
    if int1 >= int2 :
        divisor = int2
    else :
        divisor = int1
    
    while divisor >= 1:
        if int1 % divisor == 0 and int2 % divisor == 0 :
            return divisor
        divisor -= 1
#print(gcd(18, 12))
#print(gcd(24, 36))
#print(gcd(13, 19))

def bitshift(s, k, b):
    # s - string, k - integer, b - boolean
    # b True - shift left, False - right
    def swap(a,b):
        return b,a
    
    def left_shift_one_bit(s):
        length = len(s)
        for i in range(length-1):
            s[i],s[i+1] = swap(s[i], s[i+1])
        return s
        
    def right_shift_one_bit(s):
        length = len(s)
        for i in range(length-1,0,-1):
            s[i],s[i-1] = swap(s[i],s[i-1])
        return s
    
    list_s = list(s)
    
    if b == True:
        for i in range(k):
            list_s = left_shift_one_bit(list_s)
    else:
        for i in range(k):
            list_s = right_shift_one_bit(list_s)
    return ''.join(list_s)
#print(bitshift("10011",1,True))
#print(bitshift("110011",2,True))
#print(bitshift("10011",2,False))
#print(bitshift("100101",3,0))
#print(bitshift("10110100101",5,False))

def binarytodecimal(binary):
    list_binary = list(binary)
    result = 0
    length = len(list_binary)
    for i in range(length):
        if list_binary[i] == '1':
            result += pow(2,length - i - 1)
    return result
print(binarytodecimal('00000100'))
print(binarytodecimal('00111100'))