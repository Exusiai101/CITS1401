# Q1
def splitEmailAddress(Address):
    result = []
    for i in Address.split("@"):
        for j in i.split("."):
            result.append(j)
    return result
# print(splitEmailAddress("Michael.Wise@uwa.edu.au"))

# Q2
def basename(P):
    path = P.split("/")
    filename = path[-1]
    filename = filename.split(".")
    return filename[0]
# print(basename('dev/nvmen0p1/archLinux.iso'))

# Q3
def manhat(x,y):
    result = 0
    length = len(x)
    for i in range(length):
        result += abs(y[i] - x[i])
    return result
# print(manhat([1, 3, 5, 7], [1, 9, 25, 42]))

'''
4. Consider the following rather impenetrable (but correct) Python code, taken
from a function:
if os.path.exists(f):
    return [c for c in open(f,'r').read().split('\n') if c != ‘’]
a. What does the code do? [3 marks]
b. Rewrite the code so that it is easier to understand [7 Marks].
'''
# The code first exmain id the input file path exist
# then read the file Line by line, appen the none empty line to a list c
# then return the list
def easierone(f):
    import os
    assert os.path.exists(f)
    data = []
    try:
        with open(f,'r') as file:
            file_content = file.read()
            file_content = file_content.split("\n")
            for line in file_content:
                if line != '':
                    data.append(line)
    except IOError:
        return []
    return data


# Q6
def merge(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    result = []
    list1_po = 0
    list2_po = 0
    while True:
        if list1[list1_po] < list2[list2_po]:
            result.append(list1[list1_po])
            list1_po += 1
        elif list2[list2_po] < list1[list1_po]:
            result.append(list2[list2_po])
            list2_po += 1
        else:
            result.append(list1[list1_po])
            list1po += 1
            list2_po += 1
        if list1_po == len1:
            for i in list2[list2_po:]:
                result.append(i)
            break
        elif list2_po == len2:
            for i in list1[list1_po:]:
                result.append(i)
            break
    return result

# Q7
def marksdistribution(D : dict) -> dict:
    def ranks(marks):
        if marks < 50:
            return "N"
        elif 50 <= marks < 60:
            return "P"
        elif 60 <= marks < 70:
            return "Cr"
        elif 70 <= marks < 80:
            return "D"
        else:
            return "HD"
    result = {}
    for keys in D:
        rank = ranks(keys)
        if not rank in result:
            result[rank] = 1
        else:
            result[rank] += 1
    return result