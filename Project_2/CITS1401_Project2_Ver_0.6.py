# UTF-8
# Student ID: 24729742
# Name: Scout Wu / Wenbo Wu
# Date: Mat.6, 2025
# Program Description: CITS1401 Project 2

def main(csvfile_1, csvfile_2):
    
    '''
    OP1: 
        A dictionary, 
        where keys are all the age groups found inthe data, 
        as formatted  strings  of  f ormat‘lower-upper’,  
        e.g.,  ‘0-9’  and ‘80-None’. 
        
        Use ‘None’ if one of the bounds does not exist. 
        The value for each key of the dictionary needs to be a list including following three items 
        in the order below:  
            1.The name of the state with the largest population in the age group (key), 
            across all the states in the data.
            
            2.The name of the SA3 area with the largest population in the age group ( key), 
            across all the SA3 areas in the data.

            3. The name of the SA2   area with the largest population in the age group ( key), 
            across all the SA2 areas in the data.
            When there are multiple states/areas with the same largest population, 
            choose the first one in alphabetical order in terms of state/area code. 
            The codes of states/areas should be treated as strings.

    OP2: 
        A nested dictionary where keys of the outer dictionary are the codes of all the states present in the data, 
        and the value for each key will be a dictionary.

        For the inner dictionaries (which are values of outer dictionary)  , 
        the keys will be the codes of all SA3 areas of the state  (outer  key)  
        with populations of 150000 or higher in the  state  (outer  dictionary’s key).

        The value of the inner dictionary will be a list 
        containing following three elements in the order below:  
            1.
                the code of the SA2 area with the largest population,  
                across all the SA2 areas within the SA3 areas 
                identified by the key of the inner dictionary.
            2.
                the total population of this SA2 area 
                [ found in (OP2:1)]. 
            3.
                the standard deviation of populations across age groups 
                in this SA2 area 
                [ found in (OP2:1)]. 
                
                When there are multiple areas with the same largest population, 
                choose the first one in alphabetical order in terms of area code.  
                The codes of states/areas should be treated as strings. 
                Use empty inner dictionary 
                if there is no SA3 area with populations equal or greaterthan 150000. 
    
    OP3: 
        A dictionary where the keys are the names of all the SA3 areas 
        present in the data, that have 15 or more SA2 areas. 
        The value will be a list, indicating a pair of SA2 areas 
        within  the  SA3  area,  
        with  the  maximum  similarity  (measured  by  Cosine  Similarity) 
        between  the  percentages of populations  in  each  age  group.  
        
        The  list  includes following items in the order below:
        
        1.
            the name of first SA2 area in the pair 
            (the name ranks first alphabetically)  . 
        
        2.
            the name of second SA2 area in the pair 
            (the name ranks second alphabetically).
        
        3.
            the Cosine Similarity score (a  float  number) 
            between  the  percentages of populations in each age group 
            of the two SA2 areas.
            
        Use empty dictionary 
        if there is no SA3 area with 15 or more SA2 areas. 
        All returned numeric outputs must contain values 
        rounded  to  four  decimal  places 
        (if required to be rounded off).
        Do not round the values during calculations.
        Instead, round them only at the time 
        when you save them into the final output variables.
    '''
    
    # Store Error Message, meanwhile act as a flag
    # if message != "", means error occurs
    message = ""

    # initialize output
    OP1 = {}
    OP2 = {}
    OP3 = {}


    # Read CSV File to lists
    area_Data, message = read_csv_file(csvfile_1)
    if message != "":
        print(message)
        return OP1, OP2, OP3
    
    population_Data, message= read_csv_file(csvfile_2)
    if message != "":
        print(message)
        return OP1, OP2, OP3


    # Find data position:
    try:
        if area_Data != [] and population_Data != []:
            popu_sa2_code_po = find_name_position(population_Data[0], 'area_code_level2')
            area_sa2_code_po = find_name_position(area_Data[0],'sa2 code')
            area_sa2_name_po = find_name_position(area_Data[0],'sa2 name')
            area_sa3_name_po = find_name_position(area_Data[0],'sa3 name')
            area_sa3_code_po = find_name_position(area_Data[0],'sa3 code')
            area_state_code_po = find_name_position(area_Data[0],'s_t code')
            area_state_name_po = find_name_position(area_Data[0],'s_t name')
        else:
            message = "Empty File Error"
            print(message)
            return OP1, OP2, OP3
    except IndexError:
        print("File not Found or Empty File Error")
        return OP1,OP2, OP3
    
    # Check if sucefully found name position
    # find_name_position will return 0 when keyword not founded
    if [area_sa2_code_po,
        area_sa2_name_po,
        area_sa3_name_po,
        area_sa3_code_po,
        area_state_code_po,
        area_state_name_po].count(0) > 1:
        message = "Invalid header row: Insuffent data or corrupted data"
        print(message)
        return OP1, OP2, OP3
    

    # Structure population data row1
    # then put it back to population_Data
    popu_header_row = population_Data[0]
    popu_header_row = structure_and_check_popu_header_row(popu_header_row)
    population_Data[0] = popu_header_row


    # Sort the list
    # Header row became the last row after sorting
    # E.g: area_Data[-1] population_Data[-1]
    area_Data = sorted(area_Data, key=lambda x:x[area_sa2_code_po],reverse=False)
    population_Data = sorted(population_Data, key=lambda x:x[popu_sa2_code_po], reverse=False)

    
    # Convert data to objects dictionary. use sa2 code as key
    area_Data_dict = convert_to_object(area_Data,area_sa2_code_po, area_sa2_name_po, area_sa3_code_po, area_sa3_name_po, area_state_code_po,area_state_name_po)

    # put population data to the obj
    area_Data_dict = insert_data_to_obj(area_Data_dict, population_Data, popu_sa2_code_po)

    # Create dictionary for reference
    st_code_sa3_dict, sa3_code_sa2_dict = create_reference_dict(area_Data_dict)



    '''
        Preparation is done
        Calculation part for 3 OP
    '''
    # Calculate OP1
    OP1 = calculate_OP1(population_Data, area_Data_dict)
    
    # Calculate OP2
    OP2 = calculate_OP2(area_Data_dict, st_code_sa3_dict, sa3_code_sa2_dict)

    # Calculate OP3
    OP3 = calculate_OP3(area_Data_dict,sa3_code_sa2_dict)

    return OP1, OP2, OP3

def read_csv_file(csv_filename):
    """
    Read data from CSV file

    Arguments:
        csv_filename(str)

    Return:
        A list of each row, each row is a list inside the returned list.
        Also convert all str to lowercase
    """
    data = []
    message = ""

    try:
        with open(csv_filename,'r') as csv_file:
            for line in csv_file:
                line = [value.lower() for value in line.strip().split(",")]
                data.append(line)
    
    except (FileNotFoundError, IOError):
        message = "File not Found Error"
        return [], message
    
    except PermissionError:
        message = "Permission Error: You don't have the permission to open this file"
        return [], message
    
    except UnicodeDecodeError:
        message = "Not a valid utf-8 text file"
        return [], message
    
    return data, message





# Structure population data header row
# if the lower bound is grater than upper bound, exchange them
def structure_and_check_popu_header_row(header_row):
    '''
        This function structure the header row, handle lower bound upper bound exchanged situation
        Also, check duplicated data and mark them.
    '''

    header_row_length = len(header_row)
    for i in range(header_row_length):
        if header_row[i].startswith('age '):
            if not header_row[i].endswith(' and over'):
                header = header_row[i].replace('age ', '')
                header_list = header.split("-")
                if header_list[0].isdecimal() and header_list[1].isdecimal():
                    if int(header_list[0]) > int(header_list[1]):
                        header_list[0], header_list[1] = header_list[1], header_list[0]
                        header_row[i] = 'age '+ header_list[0] + '-' + header_list[1]

                    duplicated_colum = []                        
                    # Check Duplicated Header Column
                    for j in range(header_row_length):
                        if (not header_row[i].startswith("Duplicated data, original data: ")) and (not header_row[j].startswith("Duplicated data, original data: ")) and header_row[i] == header_row[j] and i != j:
                            duplicated_colum.append(i)
                            duplicated_colum.append(j)
                    for dup_col in duplicated_colum:
                        header_row[dup_col] = "Duplicated data, original data: " + header_row[dup_col]
                else:
                    # This message doesn't starts with 'age ', 
                    # won't be chcked by verification function when convert to object
                    header_row[i] = "InvalidData Remove, OriginalData: " + 'age ' + header_row[i]
    return header_row





# Link the 2 lists
class sa2_area:
    def __init__(self,sa2_code, sa2_name,sa3_code,sa3_name,st_code,st_name):
        self.sa2_code = sa2_code
        self.sa2_name = sa2_name
        self.sa3_code = sa3_code
        self.sa3_name = sa3_name
        self.st_code = st_code
        self.st_name = st_name
        self.population = {}
    
    def add_age_popu(self, age_group : str, population : str):
        self.population[age_group] = population
    
    def get_age_popu(self,age_group : str):
        try:
            return self.population[age_group]
        except KeyError:
            return 0



def convert_to_object(area_data, area_sa2_code_po, area_sa2_name_po, area_sa3_code_po, area_sa3_name_po, area_state_code_po,area_state_name_po):
    '''
        This function convert area data to object and return a dict
        Returned Dict use sa2_code as key, and object as values.

        Args:
            area_data
            position int

        Returns:
            object_dict: dict contains obj
    '''
    def verify_area_data(row,area_data_row1):
        '''
            this function check if the passed in row of area data is valid
            the condition included:
                length difference
                empty value
                invalid sa2 and sa3 code
        '''
        if len(row) != len(area_data_row1):
            return False
        elif '' in row:
            return False
        elif not row[area_sa2_code_po].isdecimal():
            return False
        elif not row[area_sa3_code_po].isdecimal():
            return False
        elif not row[area_state_code_po].isdecimal():
            return False
        
        else:
            return True

    # logic part of convert to object
    object_dict = {}

    for i in area_data[0:-1]:

        # If duiplicated data, remove the object from that dict
        if (i[area_sa2_code_po] in object_dict):
            object_dict.pop(i[area_sa2_code_po])

        # If data invalid, don't add object to dictionary
        elif not verify_area_data(i,area_data[-1]):
            continue

        # if data valid and not duplicated, create obj and add to dict.
        else:
            new_area_object = sa2_area(i[area_sa2_code_po],i[area_sa2_name_po], i[area_sa3_code_po],i[area_sa3_name_po],i[area_state_code_po],i[area_state_name_po])
            object_dict[i[area_sa2_code_po]] = new_area_object

    return object_dict





def insert_data_to_obj(area_data_dict, population_Data, popu_sa2_code_po):
    '''
        in the initialized area data obj.
        add the popu into it
        use the info in the header row as key, and popu data as values
        Check if the population data is valid. if not, remove the whole obj in the dict.

        The inserted data will be interger!!!!!!
    '''
    def verify_popu_data(row_to_check, header_row, header_row_length) -> bool:
        '''
            this function check if the population data is valid
            And insert population data to obj

            The condition checked are followes:
            Negative value
            None value
            letters in numbers

            Returens
                True if valid
                False if invalid
        '''
        # length error
        if len(row_to_check) != header_row_length:
            return False
        
        # None Value error
        elif '' in row_to_check:
            return False
        
        # letter/negativeValue/FloatValue
        for i in range(header_row_length):
            if header_row[i].startswith('age '):
                if not row_to_check[i].isdecimal():
                    return False
        return True
    
    # logic part of insert data

    # initilize
    header_row_length = len(population_Data[-1])
    data_to_remove = []

    # insert population data
    for sa2_code in area_data_dict:
        for row in population_Data[0:-1]:
            if row[popu_sa2_code_po] == sa2_code:
            # check if data valid
                if verify_popu_data(row, population_Data[-1], header_row_length):
                    # if valid, insert data
                    for sa2_to_remove in range(header_row_length):
                        if population_Data[-1][sa2_to_remove].startswith('age '):
                            agegroup = population_Data[-1][sa2_to_remove].replace('age ','')
                            if ' and over' in agegroup:
                                agegroup = agegroup.replace(' and over','-None')
                            area_data_dict[sa2_code].add_age_popu(agegroup, int(row[sa2_to_remove]))
                # if invalid, prepare to remove obj
                else:
                    data_to_remove.append(row[popu_sa2_code_po])
    # remove obj
    for sa2_to_remove in data_to_remove:
        area_data_dict.pop(sa2_to_remove)

    return area_data_dict





def find_name_position(data_row1, name):       #return the position contains keyword
    """
        Find the position of data in a row contains specific string:

        Args:
            area_data_row1 -> list : a list contains string, normally the first row of a table
            name -> str : a string contains the keyword you want to look for
            
        Returns:
            The first position number in the list contains keyword
    """

    for i in range(len(data_row1)):
        # Only returns 100% matches value
        if name == data_row1[i]:
            return i
    return 0





def create_reference_dict(area_Data_dict):
    '''
        This function create dictionary for reference
        dict1: state code as key, sa3 code as values
        dict2: sa3 code as key, sa2 code as values

        Duplicated data already removed when convert to object
    '''
    # Initialize
    st_code_sa3_dict = {}
    sa3_code_sa2_dict = {}

    # Iteration
    for area in area_Data_dict:
        state_code_to_add = area_Data_dict[area].st_code
        sa3_code_to_add = area_Data_dict[area].sa3_code
        sa2_code_to_add = area_Data_dict[area].sa2_code

        # Add to st code to sa3 code dict
        if not state_code_to_add in st_code_sa3_dict:
            st_code_sa3_dict[state_code_to_add] = []
            st_code_sa3_dict[state_code_to_add].append(sa3_code_to_add)
        else:
            # check duplicated data
            if not sa3_code_to_add in st_code_sa3_dict[state_code_to_add]:
                st_code_sa3_dict[state_code_to_add].append(sa3_code_to_add)

        # Add to sa3 code to sa2 code dict
        if not sa3_code_to_add in sa3_code_sa2_dict:
            sa3_code_sa2_dict[sa3_code_to_add] = []
            sa3_code_sa2_dict[sa3_code_to_add].append(sa2_code_to_add)
        else:
            # check duplicated data
            if not sa2_code_to_add in sa3_code_sa2_dict[sa3_code_to_add]:
                sa3_code_sa2_dict[sa3_code_to_add].append(sa2_code_to_add)
    return st_code_sa3_dict, sa3_code_sa2_dict





def calculate_OP1(population_Data, area_Data_dict):
    '''
        OP1: 
        A dictionary, 
        where keys are all the age groups found inthe data, 
        as formatted  strings  of  format‘lower-upper’,  
        e.g.,  ‘0-9’  and ‘80-None’. 
        
        Use ‘None’ if one of the bounds does not exist. 
        The value for each key of the dictionary 
        needs to be a list including following three items 
        in the order below:  
        
        1.
        The name of the state with the largest population 
        in the age group (key), 
        across all the states in the data.
            
        2.
        The name of the SA3 area with the largest population
        in the age group ( key), 
        across all the SA3 areas in the data.

        3. The name of the SA2 area with the largest population 
        in the age group ( key), 
        across all the SA2 areas in the data.
        When there are multiple states/areas with the same largest population, 
        choose the first one in alphabetical order in terms of state/area code. 
        The codes of states/areas should be treated as strings.

    '''

    def initialize_dict(population_Data):
        '''
            Thif functon put all key in a dictionary in a alphabetical order
            Args:
                population_Data: only the first row
            Returns:
                an initialized dict
                use age group as key, empty list as values
        '''
        sorted_first_row = sorted(population_Data)
        initialized = {}
        for word in sorted_first_row:
            if word.startswith('age ') :
                age_group = word.replace('age ', '')
                if ' and over' in age_group:
                    age_group = age_group.replace(' and over', '-None')
                initialized[age_group] = []
        return initialized
    
    def find_largest_state_popu(age_group:str, area_Data_dict) -> str:
        '''
            return the name of the state who have the largest population across all states

            Variable:
                result_dict:
                    a dict, use state name as key. state population as values
                Example:
                    {Western Australia: int, Victoria: int}....

            Return:
                str
        '''
        result_dict = {}
        code_to_name = {}

        # Caculate the total popu
        for i in area_Data_dict:
            if not area_Data_dict[i].st_code in result_dict:
                code_to_name[area_Data_dict[i].st_code] = area_Data_dict[i].st_name
                result_dict[area_Data_dict[i].st_code] = 0
                result_dict[area_Data_dict[i].st_code] += int(area_Data_dict[i].get_age_popu(age_group))
            else:
                result_dict[area_Data_dict[i].st_code] += int(area_Data_dict[i].get_age_popu(age_group))
                                                              
        # find the largest popu:
        max_code = ''
        max_value = -1 

        for i in result_dict:
            if result_dict[i] > max_value:
                max_value = result_dict[i]
                max_code = i
                continue
            elif result_dict[i] == max_value:
                # alphabetical order
                if sorted([max_code,i]) != [max_code,i]:
                    max_value = result_dict[i]
                    max_code = i
                    continue
        return code_to_name[max_code]

    def find_largest_sa3_popu(age_group:str,input_dict) -> str:
        '''
            this function find the sa3 area with the largest population

            Variable:
                result_dict:
                    a dict use sa3 name as key, population as values
        '''
        result_dict = {}
        for i in input_dict:
            if not input_dict[i].sa3_name in result_dict:
                result_dict[input_dict[i].sa3_name] = 0
                result_dict[input_dict[i].sa3_name] += int(input_dict[i].get_age_popu(age_group))
            else:
                result_dict[input_dict[i].sa3_name] += int(input_dict[i].get_age_popu(age_group))
        # find the name of sa3 area with largest popu
        max_name = ''
        max_value = -1
        for i in result_dict:
            if result_dict[i] > max_value:
                max_value = result_dict[i]
                max_name = i
            elif result_dict[i] == max_value:
                max_name = sorted([max_name,i])[0]
        return max_name

    def find_largest_sa2_popu(age_group:str,input_dict) -> str:
        '''
            this function find the sa2 area with the largest population

            Variable:
                result_dict:
                    a dict use sa2 name as key, population as values
        '''
        result_dict = {}
        for i in input_dict:
            if not input_dict[i].sa2_name in result_dict:
                result_dict[input_dict[i].sa2_name] = 0
                result_dict[input_dict[i].sa2_name] += int(input_dict[i].get_age_popu(age_group))
            else:
                result_dict[input_dict[i].sa2_name] += int(input_dict[i].get_age_popu(age_group))
        # find the name of sa3 area with largest popu
        max_name = ''
        max_value = -1
        for i in result_dict:
            if result_dict[i] > max_value:
                max_value = result_dict[i]
                max_name = i
            elif result_dict[i] == max_value:
                max_name = sorted([max_name,i])[0]
        return max_name
    

    # initialize the result{}, put all key in the dictionary
    result = initialize_dict(population_Data[-1])

    # Logic part for OP1
    for age_group in result:
        # find the name of state with the largest population
        result[age_group].append(find_largest_state_popu(age_group,area_Data_dict))
        # find the name of sa3 area with the largest population
        result[age_group].append(find_largest_sa3_popu(age_group,area_Data_dict))
        # find the name of sa2 area with the largest population
        result[age_group].append(find_largest_sa2_popu(age_group,area_Data_dict))
    return result





def calculate_OP2(area_Data_dict : dict, st_code_sa3_dict, sa3_code_sa2_dict):
    '''
    OP2: 
        A nested dictionary where keys of the outer dictionary are the codes of all the states present in the data, 
        and the value for each key will be a dictionary.
        Example: {WA: [inner dict], Tasmania: [inner dict], ......}

        For the inner dictionaries (which are values of outer dictionary)  , 
        the keys will be the codes of all SA3 areas of the state  (outer  key)  
        with populations of 150000 or higher in the  state  (outer  dictionary’s key).

        The value of the inner dictionary will be a list 
        containing following three elements in the order below:  
            1.
                the code of the SA2 area with the largest population,  
                across all the SA2 areas within the SA3 areas 
                identified by the key of the inner dictionary.
            2.
                the total population of this SA2 area 
                [ found in (OP2:1)]. 
            3.
                the standard deviation of populations across age groups 
                in this SA2 area 
                [ found in (OP2:1)]. 
                
                When there are multiple areas with the same largest population, 
                choose the first one in alphabetical order in terms of area code.  
                The codes of states/areas should be treated as strings. 
                Use empty inner dictionary 
                if there is no SA3 area with populations equal or greaterthan 150000. 
    '''
    def initialize_outer_dict(area_Data_dict, st_code_sa3_dict):
        '''
            return a dict, state code is key, with empty value
        '''
        outer_dict = {}

        for state_code in st_code_sa3_dict.keys():
            outer_dict[state_code] = {}
        
        if not outer_dict:
            for sa2_code, area_obj in area_Data_dict.items():
                if hasattr(area_obj, 'st_code') and area_obj.st_code:
                    outer_dict[area_obj.st_code] = {}
        
        return outer_dict
        
        '''
        # previous version
        for stateCode in st_code_sa3_dict:
            sa3_codes = st_code_sa3_dict[stateCode]
            if sa3_codes:
                sa3_code = sa3_codes[0]
                if sa3_code in sa3_code_sa2_dict:
                    sa2_codes = sa3_code_sa2_dict[sa3_code]
                    if sa2_codes:
                        sa2_code = sa2_codes[0]
                        outer_dict[area_Data_dict[sa2_code].st_code] = {}
        return outer_dict
        '''
        '''
        # previous version
            state_name = 
            area_Data_dict[sa3_code_sa2_dict
                            [st_code_sa3_dict[stateCode]]
                            [0]].st_name
            if not state_name in outer_dict:
                outer_dict[state_name] = {}
        
        return outer_dict
        '''

    def create_sa2_popu_dict(area_Data_dict : dict):
        '''
            this fuction returns a dictionary
            sa2 code as key
            total population of that sa2 area as values
        '''
        result = {}
        for sa2_area in area_Data_dict:
            result[sa2_area] = 0
            for age_group in area_Data_dict[sa2_area].population:
                result[sa2_area] += int(area_Data_dict[sa2_area].get_age_popu(age_group))
        return result
    
    def create_sa3_popu_dict_within_state(st_code_sa3_dict,
                                          sa3_code_sa2_dict,
                                          sa2_popu_dict,
                                          state_code):
        '''
            this function returns a dict
            sa3 code in the required state as key
            total popu in that sa3 area as values
        '''
        # check if state code exist
        flag = False
        for i in st_code_sa3_dict:
            if st_code_sa3_dict[i]:
                sa3s = st_code_sa3_dict[i]
                if sa3s[0]:
                    sa3 = sa3s[0]
                    if sa3_code_sa2_dict[sa3]:
                        sa2s = sa3_code_sa2_dict[sa3]
                        if sa2s[0]:
                            sa2 = sa2s[0]
                            if sa2:
                                if state_code == area_Data_dict[sa2].st_code:
                                    state_code = area_Data_dict[sa2].st_code
                                    flag = True
                                    break
        if flag == False:
            return {}
        '''
        for i in st_code_sa3_dict:
            if area_Data_dict[sa3_code_sa2_dict[st_code_sa3_dict[i][0]][0]].st_code == state_code:
                state_code = area_Data_dict[sa3_code_sa2_dict[st_code_sa3_dict[i][0]][0]].st_code
                break
        '''
        # create dict
        sa3_popu_dict = {}
        for sa3_code in st_code_sa3_dict[state_code]:
            sa3_popu_dict[sa3_code] = 0
            for sa2_code in sa3_code_sa2_dict[sa3_code]:
                sa3_popu_dict[sa3_code] += sa2_popu_dict[sa2_code]
        return sa3_popu_dict
                        
    def find_sa3_code_with_150000_popu(sa3_popu_dict):
        '''
        return a list of sa3 code which has popu
        greater than 150000
        if nothing found, return []
        '''
        result = []
        for i in sa3_popu_dict:
            if sa3_popu_dict[i] >= 150000:
                result.append(i)
        return result

    def find_sa2_code_with_largest_popu_within_sa3(sa2_popu_dict,
                                                   sa3_code,
                                                   sa3_code_sa2_dict):
        '''
            this function retuns a str, sa2 code
            the sa2 area has the largest population within that sa3 area
        '''
        max_code = ''
        max_popu = 0
        for sa2 in sa3_code_sa2_dict[sa3_code]:
            if sa2_popu_dict[sa2] > max_popu:
                max_code = sa2
                max_popu = sa2_popu_dict[sa2]
        return max_code, max_popu

    def calc_standard_deviation(area_Data_dict, sa2_code):
        '''
            This function calculate the standard_deviation in that age group
            
            Args:
                area_Data_dict: 
                sa2_code: str
        '''
        # get a list contain all the population data
        popu_list = []
        for popu in area_Data_dict[sa2_code].population:
            popu_list.append(int(area_Data_dict[sa2_code].get_age_popu(popu)))
        length = len(popu_list)


        # if no data or 1 data, return 0
        # Handles 0 data or 1 data
        if length == 0 or length == 1:
            return 0
        
        else:
            average_popu = sum(popu_list) / length
            upper = 0
            for i in popu_list:
                upper += (i - average_popu) ** 2
            result = pow(upper / (length - 1), 0.5)
            return round(result,4)
        
    # initialize outer dictionary
    outer_dict = initialize_outer_dict(area_Data_dict, st_code_sa3_dict)

    sa2_popu_dict = create_sa2_popu_dict(area_Data_dict)
    # calculate inner dictionary

    # calculate popu of each sa3 area
    for state_code in outer_dict:
        sa3_popu_dict = create_sa3_popu_dict_within_state(st_code_sa3_dict,
                                          sa3_code_sa2_dict, 
                                          sa2_popu_dict, 
                                          state_code)
        sa3_code_with_150000_popu = find_sa3_code_with_150000_popu(sa3_popu_dict)
        
        # if nothing found, continue
        if len(sa3_code_with_150000_popu) == 0:
            continue

        for sa3 in sa3_code_with_150000_popu:
            max_code, max_popu = find_sa2_code_with_largest_popu_within_sa3(sa2_popu_dict, sa3, sa3_code_sa2_dict)
            standard_deviation = calc_standard_deviation(area_Data_dict, max_code)
            inner_list = [max_code, max_popu,standard_deviation]
            outer_dict[state_code][sa3] = inner_list
    return outer_dict
        
    # find the sa3 area with 150000 or higher popu in the state

    # calc the population of sa2 area within sa3
    # find the sa2 with the largest population
    # add the code, total population, standard deviation across age groups in this sa2area





def calculate_OP3(area_Data_dict:dict, 
                  sa3_code_sa2_dict: dict):
    '''
        OP3: 
        A dictionary where the keys are the names of all the SA3 areas 
        present in the data, that have 15 or more SA2 areas. 
        The value will be a list, indicating a pair of SA2 areas 
        within  the  SA3  area,  
        with  the  maximum  similarity  (measured  by  Cosine  Similarity) 
        between  the  percentages of populations  in  each  age  group.  
        
        The  list  includes following items in the order below:
        
        1.
            the name of first SA2 area in the pair 
            (the name ranks first alphabetically)  . 
        
        2.
            the name of second SA2 area in the pair 
            (the name ranks second alphabetically).
        
        3.
            the Cosine Similarity score (a  float  number) 
            between  the  percentages of populations in each age group 
            of the two SA2 areas.
            
        Use empty dictionary 
        if there is no SA3 area with 15 or more SA2 areas. 
        All returned numeric outputs must contain values 
        rounded  to  four  decimal  places 
        (if required to be rounded off).
        Do not round the values during calculations.
        Instead, round them only at the time 
        when you save them into the final output variables. 
    '''
    # initialization
    def initialize(area_Data_dict, sa3_code_sa2_dict):
        '''
            this fuction returns a dict, 
            use the sa3 area code contains more than 15 sa2 area as key

            Args: 
            sa3_code_sa2_dict. a dict, 
            key is sa3 code, 
            a list contain sa2 code is values

            Returns:
            result : dictionary
                key: sa3 code contains more than 15 sa2 area
                values: empty list
        '''
        result_code = {}
        result_name = {}
        for sa3 in sa3_code_sa2_dict:
            if len(sa3_code_sa2_dict[sa3]) >= 15:
                result_code[sa3] = []
                result_name[area_Data_dict[sa3_code_sa2_dict[sa3][0]].sa3_name] = []
        return result_code, result_name


    def calc_cosine_simil_sa2(area_Data_dict : dict,
                              sa2_code_A:str,
                              sa2_code_B:str) :
        '''
            this function returns the cosine similarity
            between the 2 sa2 areas
        '''
        # extract the data
        data_A = list(area_Data_dict[sa2_code_A].population.values())
        data_B = list(area_Data_dict[sa2_code_B].population.values())

        # Calculate the cosine similaraity
        # saperate the divisor and divider

        '''
            calculate by percentage and raw data are mathimaticaly equiviliant.

            but i still try to use percentage
        '''

        # Initialize number
        upper = 0
        lower_A = 0
        lower_B = 0
        sumA = sum(data_A)
        sumB = sum(data_B)
        cosine_similarity = 0

        # Handles numbles are 0
        if sumA == 0 or sumB == 0:
            return 0
        for i in range(len(data_A)):
            num_A = int(data_A[i])
            num_B = int(data_B[i])
            upper += (num_A/sumA) * (num_B/sumB)
            lower_A += (num_A/sumA) ** 2
            lower_B += (num_B/sumB) ** 2
        
        # Check if will divided by 0
        if not (lower_A == 0 or lower_B == 0):
            cosine_similarity = upper / (pow(lower_A,0.5) * pow(lower_B,0.5))
        return cosine_similarity


    def find_largest_cosine_simil_within_sa3(area_Data_dict : dict,
                                             sa3_code_sa2_dict:dict,
                                             sa3_code):
        '''
            this function returns a list,contains following values
            indicating a pair of SA2 areas 
        within  the  SA3  area,  
        with  the  maximum  similarity  (measured  by  Cosine  Similarity) 
        between  the  percentages of populations  in  each  age  group.  
        
        The  list  includes following items in the order below:
        
        1.
            the name of first SA2 area in the pair 
            (the name ranks first alphabetically)  . 
        
        2.
            the name of second SA2 area in the pair 
            (the name ranks second alphabetically).
        
        3.
            the Cosine Similarity score (a  float  number) 
            between  the  percentages of populations in each age group 
            of the two SA2 areas.
        '''

        max_pair = []
        max_cos_similarity = -1

        current_pair = []
        current_sa2_code_A = ""
        current_sa2_code_B = ""
        current_cos_similarity = -1

        return_list = []

        sa3_codes_list = sa3_code_sa2_dict[sa3_code]
        length = len(sa3_codes_list)
        for i in range(0, length-1):
            for j in range(i+1,length): 
                current_sa2_code_A = sa3_codes_list[i]
                current_sa2_code_B = sa3_codes_list[j]
                current_cos_similarity = calc_cosine_simil_sa2(area_Data_dict,current_sa2_code_A,current_sa2_code_B)
                current_pair = [current_sa2_code_A, current_sa2_code_B]
                
                # compare cos similarity
                if current_cos_similarity > max_cos_similarity:
                    max_cos_similarity = current_cos_similarity
                    max_pair = sorted(current_pair)
                    
                
                # if cos similarity equals
                elif current_cos_similarity == max_cos_similarity:
                    # Compare first elements
                    if current_pair[0] < max_pair[0]:
                        max_pair = current_pair
                    # If first elements equal, compare second elements
                    elif current_pair[0] == max_pair[0] and current_pair[1] < max_pair[1]:
                        max_pair = current_pair
    
        return_list = max_pair
        return_list.append(round(max_cos_similarity, 4))

        return return_list 


    # initialize the result
    result_code, result_name = initialize(area_Data_dict, sa3_code_sa2_dict)
    
    # logic part for op3
    for sa3 in result_code:
        result_list = find_largest_cosine_simil_within_sa3(area_Data_dict,sa3_code_sa2_dict, sa3)
        if '' in result_list:
            continue
        sa3_name = area_Data_dict[result_list[0]].sa3_name
        sa2_name_A = area_Data_dict[result_list[0]].sa2_name
        sa2_name_B = area_Data_dict[result_list[1]].sa2_name
        cos_simi = result_list[2]
        # arrange the sa2 name

        append_list = sorted([sa2_name_A, sa2_name_B])
        append_list.append(cos_simi)
        result_name[sa3_name] = append_list
    return result_name


# Testing code
# OP2,OP2,OP3 = main('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv')
# print(OP1,'\n',OP2,'\n',OP3,'\n')
# main('www.png','www.pdf')

'''
OP1_GT = {
'0-9': ['western australia', 'wanneroo', 'baldivis - south'],
'10-19': ['western australia', 'wanneroo', 'baldivis - south'],
'20-29': ['western australia', 'stirling', 'adelaide'],
'30-39': ['western australia', 'stirling', 'enfield - blair athol'],
'40-49': ['western australia', 'wanneroo', 'baldivis - south'],
'50-59': ['western australia', 'wanneroo', 'mindarie - quinns rocks - jindalee'],
'60-69': ['western australia', 'onkaparinga', 'glenelg (sa)'],
'70-79': ['western australia', 'onkaparinga', 'victor harbor'],
'80-None': ['western australia', 'stirling', 'victor harbor']
}


flag = True
if OP1.keys() != OP1_GT.keys():
    flag = False
else:
    for i in OP1_GT.keys():
        if len(OP1[i]) != len(OP1_GT[i]):
            flag = False
        else:
            for j in range(3):
                if OP1[i][j].lower() != OP1_GT[i][j].lower():
                    flag = False
print(flag)
'''


'''
OP3_GT = {
'wanneroo': ['carramar', 'landsdale', 0.9975],
'onkaparinga': ['aldinga', 'seaford rise - moana', 0.9992],
'swan': ['beechboro', 'lockridge - kiara', 0.9974],
'stirling': ['dianella - south', 'yokine - coolbinia - menora', 0.9984],
'launceston': ['legana', 'riverside', 0.9982]
}

flag = True
if OP3.keys() != OP3_GT.keys():
    flag = False
else:
    for i in OP3_GT.keys():
        if len(OP3[i]) != len(OP3_GT[i]):
            flag = False
        else:
            if OP3[i][0].lower() != OP3_GT[i][0].lower():
                flag = False
            if OP3[i][1].lower() != OP3_GT[i][1].lower():
                flag = False
            if abs(OP3[i][2] - OP3_GT[i][2]) >= 0.0001:
                flag = False
print(flag)
'''

'''
Debugging Document Templet

Issue 1 (Date 10 May 2025):

-Error Description:
    Wrong Output for OP 1
        {'0-9': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '10-19': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '20-29': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '30-39': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '40-49': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '50-59': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '60-69': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '70-79': ['western australia', 'onkaparinga', 'wilderness - west'], 
        '80 and over': ['western australia', 'onkaparinga', 'wilderness - west']}

    Excepted:
        {'0-9': ['western australia', 'wanneroo', 'baldivis - south'], 
        '10-19': ['western australia', 'wanneroo', 'baldivis - south'], 
        '20-29': ['western australia', 'stirling', 'adelaide'], 
        '30-39': ['western australia', 'stirling', 'enfield - blair athol'], 
        '40-49': ['western australia', 'wanneroo', 'baldivis - south'], 
        '50-59': ['western australia', 'wanneroo', 'mindarie - quinns rocks - jindalee'], 
        '60-69': ['western australia', 'onkaparinga', 'glenelg (sa)'], 
        '70-79': ['western australia', 'onkaparinga', 'victor harbor'], 
        '80 and over': ['western australia', 'stirling', 'victor harbor']}

-Erroneous Code Snippet:
    for data_obj in area_data_dict:
        for row in population_Data[1:]:
            # check if data valid
            if verify_popu_data(row, population_Data[0], header_row_length):
                # if valid, insert data
                for i in range(header_row_length):
                    if 'age ' in population_Data[0][i]:
                        area_data_dict[data_obj].add_age_popu(population_Data[0][i].replace('age ',''), row[i])
            # if invalid, prepare to remove obj
            else:
                data_to_remove.append(row[popu_sa2_code_po])

- Test Case
main('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv')

-Reflection
    I forgot to match the sa2 code for each data. I added a new condition check:
    if row[popu_sa2_code_po] == sa2_code
    problem fixed 




Issue 2 (Date 10 May 2025):

-Error Description:
    Traceback (most recent call last):
  File "/run/user/1000/gvfs/onedrive:host=340f4e1681c81e17/Bundles_b896e2bb7ca3447691823a44c4ad6ad7/StudyAbroad/UWA/CITS1401/Project_2/CITS1401_Project2_Ver_0.2.py", line 693, in <module>
    print(main('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/run/user/1000/gvfs/onedrive:host=340f4e1681c81e17/Bundles_b896e2bb7ca3447691823a44c4ad6ad7/StudyAbroad/UWA/CITS1401/Project_2/CITS1401_Project2_Ver_0.2.py", line 145, in main
    OP2 = calculate_OP2(area_Data_dict, st_code_sa3_dict, sa3_code_sa2_dict)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/run/user/1000/gvfs/onedrive:host=340f4e1681c81e17/Bundles_b896e2bb7ca3447691823a44c4ad6ad7/StudyAbroad/UWA/CITS1401/Project_2/CITS1401_Project2_Ver_0.2.py", line 621, in calculate_OP2
    outer_dict = initialize_outer_dict(st_code_sa3_dict, sa3_code_sa2_dict)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/run/user/1000/gvfs/onedrive:host=340f4e1681c81e17/Bundles_b896e2bb7ca3447691823a44c4ad6ad7/StudyAbroad/UWA/CITS1401/Project_2/CITS1401_Project2_Ver_0.2.py", line 533, in initialize_outer_dict
    state_name = sa3_code_sa2_dict[ st_code_sa3_dict[stateCode] ] [0].st_name
                 ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'


-Erroneous Code Snippet:
    def initialize_outer_dict(area_Data_dict, st_code_sa3_dict, sa3_code_sa2_dict):
        outer_dict = {}
        for stateCode in st_code_sa3_dict:
            state_name = area_Data_dict[sa3_code_sa2_dict[st_code_sa3_dict[stateCode]][0]].st_name
            if not state_name in outer_dict:
                outer_dict[state_name] = {}
        return outer_dict

- Test Case
    main('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv')

-Reflection
    The way I access value is very dangerous, hard to understand.
    Then I switched create dict using statecode as key. And rewrite the code
    Use st_code_sa3_dict to create dictionary
    if initialized failed, go to object diction and initialize dictionary
    if all failed, it will return empty dictionary



Issue 3 (Date 10 May 2025):

-Error Description:
Traceback (most recent call last):
  File "/home/scout/Desktop/Study/CITS1401/Project_2/CITS1401_Project2_Ver_0.3.py", line 707, in <module>
    print(main('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/scout/Desktop/Study/CITS1401/Project_2/CITS1401_Project2_Ver_0.3.py", line 145, in main
    OP2 = calculate_OP2(area_Data_dict, st_code_sa3_dict, sa3_code_sa2_dict)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/scout/Desktop/Study/CITS1401/Project_2/CITS1401_Project2_Ver_0.3.py", line 642, in calculate_OP2
    sa3_popu_dict = create_sa3_popu_dict_within_state(st_code_sa3_dict,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/scout/Desktop/Study/CITS1401/Project_2/CITS1401_Project2_Ver_0.3.py", line 576, in create_sa3_popu_dict_within_state
    if area_Data_dict[st_code_sa3_dict[i][0][0]].st_name == state_name:
       ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: '4'

-Erroneous Code Snippet:
    def create_sa3_popu_dict_within_state(st_code_sa3_dict,
                                          sa3_code_sa2_dict,
                                          sa2_popu_dict,
                                          state_name):
        # find state code
        for i in st_code_sa3_dict:
            if area_Data_dict[st_code_sa3_dict[i][0][0]].st_name == state_name:
                state_code = st_code_sa3_dict[i][0][0].st_code
                break
    
                
    def create_reference_dict(area_Data_dict):
    st_code_sa3_dict = {}
    sa3_code_sa2_dict = {}
    for area in area_Data_dict:
        if not area_Data_dict[area].st_code in st_code_sa3_dict:
            st_code_sa3_dict[area_Data_dict[area].st_code] = []
            st_code_sa3_dict[area_Data_dict[area].st_code].append(area_Data_dict[area].sa2_code)
        else:
            st_code_sa3_dict[area_Data_dict[area].st_code].append(area_Data_dict[area].sa2_code)

        if not area_Data_dict[area].sa3_code in sa3_code_sa2_dict:
            sa3_code_sa2_dict[area_Data_dict[area].sa3_code] = []
            sa3_code_sa2_dict[area_Data_dict[area].sa3_code].append(area_Data_dict[area].sa2_code)
        else:
            sa3_code_sa2_dict[area_Data_dict[area].sa3_code].append(area_Data_dict[area].sa2_code)
    return st_code_sa3_dict, sa3_code_sa2_dict

- Test Case

-Reflection
    wrong data was appended when creating reference list. I moved the create_reference_dict()
    to the global frame and rewrote the code. 
    used safer way to create dict. 
    I created a few more variable for readibility
    I realized that when accessing nested dictionary or lists,
    its so easy to encounter IndexError.
    This highlights the importance of memory safty. the good news is python handles memory for you.
    But in other language like C,it might pass the compiler check, leave a sneky error cause program crash. 

'''