def find_word(sentence, word):
    return sentence.find(word)

def word_swapper(sentence, word):
    return sentence.replace(word, "ABC")

def count_word(sentence, word):
    return sentence.count(word)

def top_and_tail(string):
    return string[1:-1]

def half_string(string):
    return string[:len(string)//2]

def second_half_string(string):
    return string[len(string)//2:]

def first_nth_string(string,n):
    return string[:n]

def full_name(first_name, last_name):
    return first_name + " " + last_name

def insert_item(data, item, ind):
    new_data = data.copy()
    new_data.insert(ind, item) # insert() method doesn't return values
    return new_data

def count_items(data):
    return len(data)

def third(data):
    return data[2]

def insert_item_end(data, item):
    new_data = data.copy()
    new_data.append(item)
    return new_data

def append_list_new(data1, data2):
    return data1 + data2

def append_lists(data1, data2):
    return data1 + data2

def almost_last(data):
    return data[-2]

def remove(data):
    new_data = data.copy()
    new_data.remove(data[3])
    return new_data

def nth_item(data,n):
    return data[n]

def repeat_last(data):
    new_data = data.copy()
    new_data.append(data[-1])
    return new_data

def cubed_tuple(number):
    return number, number**3

def list_swap(lst):
    new_list = lst.copy()
    for i in range(0,len(new_list),2):
        try:
            temp = new_list[i]
            new_list[i] = new_list[i+1]
            new_list[i+1] = temp
        except IndexError:
            break
    return new_list

def num_words(string):
    return len(string.split(" "))

def list_sorting(lst1, lst2):
    """
        lst1 -> list : contains name
        lst2 -> list : contains age
    """
    name_age_dict = {}
    age_name_dict = {}
    sorted_names = []
    sorted_ages = [] 

    table = list(zip(lst1, lst2))

    sorted_table = sorted(table, key=lambda x: (-x[1], x[0]))
    sorted_names, sorted_ages = zip(*sorted_table)
    sorted_names = list(sorted_names)
    sorted_ages = list(sorted_ages)
    return sorted_names, sorted_ages

lst1 = ['JZM', 'XJP', 'XBB']
lst2=[114,514,514]

print(list_sorting(['Chris','Amanda','Boris','Charlie'],[35,43,55,35]))

print(list_sorting(['Tim','Mark','Ali','Cherry','Tina'],[45,65,33,37,45]))

print(list_sorting(['George','Mark','Asad','Candy','Harry','Cira','Lee'],[35,41,35,65,41,23,41]))

print(list_sorting(['Ali','Aali','Asad','Amad','Arran','Allen','Abraham'],[41,41,41,65,41,23,41]))