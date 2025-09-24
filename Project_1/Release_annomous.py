# UTF-8
# Student ID: 
# Name:
# Date: Mar. 10, 2025
# Program Desccription: UCB Project 1 Process population Data



def main(csvfile_1, csvfile_2, age, sa2_1, sa2_2):
    """
    Main Function to analyze population data

    Args:
        csvfile_1(str): CSV file containing relationship data of areas of each state
        csvfile_2(str): CSV file containing record of population
        age(int): Age
        sa2_1(str): Code of an SA2 area
        sa2_2(str): Code of another SA2 area

    Return:
        OP1, OP2, OP3, OP4
        
        OP1:
            A list containing 2 integers, 
            The lower bound and the upper bound of the age group containing the input age
            None as the element if one of the bounds does't exise
        
        OP2:
            A list of 2 Lists
            
            The first list includes three elements in the order below:  
                1.the code of the SA3 area where inputIP4 (sa2_1) is located, 
                2.the average of populations in the identifiedage group (OP1), across all SA2 areasin this SA3 area, 
                3.the standard deviations of populations in the identifiedage group (OP1),   across all SA2 areas in this SA3 area.   
            
            The second list is similar to the first one, but for input IP5   (sa2_2)
    
        OP3:
            A list of Lists
            Each inner list conatins 3 elements:
                1. The state name
                2. the name of the SA3 area with the largest population in the identifiedage group (OP1), in the state, 
                3. the percentage of the population which you found above with respect to the total population across all age groups in the same SA3 area.

        OP4:
            A aloat number
            which correlation coeficcient between the populations in each group in IP4(sa_2_1)
            and IP5(sa2_2)

        All return numeric optputs rounded to 4 decimal places(if required)
    """

    # Pre process the file, read the file into list
    area_data = read_csv_file(csvfile_1)
    population_data = read_csv_file(csvfile_2)

    # find the position of data in the table
    sa2_po = find_name_position(area_data[0], 'sa2 code')
    sa3_po = find_name_position(area_data[0], 'sa3 code')

    OP1, age_position= find_age_group(age, population_data[0])
    OP2 = caculate_population_statistics(sa2_1, sa2_2, area_data, population_data, age_position, sa2_po, sa3_po)
    OP3 = find_largest_population_statistics(age_position, area_data, population_data, sa2_po, sa3_po)
    OP4 = caculate_correlation(sa2_1, sa2_2, population_data)

    return OP1, OP2, OP3, OP4

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
    try:
        with open(csv_filename,'r') as csv_file:
            for line in csv_file:
                line = [value.lower() for value in line.strip().split(",")]
                data.append(line)
    except FileNotFoundError:
        return []
    return data

def find_name_position(data_row1, name):       #return the position of state name
    """
        Find the position of data in a row contains specific string:

        Args:
            area_data_row1 -> list : a list contains string, normally the first row of a table
            name -> str : a string contains the keyword you want to look for
            
        Returns:
            The first position number in the list contains keyword
    """
    try: 
        for i in range(len(data_row1)):
            if name in data_row1[i]:
                return i
    except TypeError:
        return 0

# the following 4 functions Caculate OP1 to OP 4

def find_age_group(age,group_data):
    """
        Find the age group that contains input age

        Args:
            age(int): input age
            population_data(list of string): A list that contains age group

        Returns:
            A list contains 2 integers
            The lower bound and the upper bpund of the age group containing the input age
            None as the element if one of the bounds does't exise
    """
    def check_in_bounds(age, bounds):   # Helper Function
        """
            Check if age is in the bounds

            Args:
                age(int): input age
                bounds: A list of 2 int contains the lower bound and upper bound

            Returns:
                True if in the bounds
                Otherwise False
        """
        if bounds[0] <= age and (bounds[1] == None or age <= bounds[1]):
            return True
        else:
            return False
    
    def extract_age_group(age_group): # Normalize group data
        """
            Extract the age group to a list that contains lower bound and upper bound

            Args:
                age_group: A string contains the bound of the age
                like 
                    "age 0-4"
                    "age 5-8"
                    "age 10-14"
                    "age 85 and over"

            Returns:
                A list of 2 int. First is the lower bound, second is the upper bound
        """
        if not "age" in age_group:  # Check if the input contains Age bounds
            return [None]

        age_group = age_group.replace("age ", "")
        if "and over" in age_group:
            bounds = age_group.replace("and over","")
            bounds = int(bounds)
            return [bounds, None]
        else:
            bounds = age_group.split("-")
            return [int(bounds[0]), int(bounds[1])]

    # Logic part of Find_age_group()

    for i in range(len(group_data)):
        age_group = extract_age_group(group_data[i])
        if age_group != [None]:
            if check_in_bounds(age, age_group):
                return age_group, i
    return [None, None], 0


def caculate_population_statistics(sa2_1, sa2_2, area_data, population_data, age_position, sa2_position, sa3_position):
    """
        This function caculate population satistics for each SA3 where SA2 areas located in

        Args:
            sa2_1 (str): Code of an SA2 area
            sa2_2 (str): Code of another SA2 area
            age_position: the position of the identified age group in population data
            area_data ([str]): List contains area data
            population_data ([str]): List contains population data
            sa2_position, sa3_position: position of sa2 sa3 code in area data

        Returns:
            [   
                [sa3_code_1, average_population_1, standard_deviations_1] ,
                [sa3_code_2, average_population_2, standard_deviations_2] 
            ]
    """
    


    def find_sa3_code(sa2_code, area_data, sa2_position, sa3_position):
        """
            Finds the sa3 code based on the given sa2_code and list of area data

            Args:
                sa2_code (int):
                area_data ( [str] ): List of string, contains area data

            Returns:
                sa3_code (str)
        """
        for i in area_data[1:]:
            if i[sa2_position] == sa2_code:
                return i[sa3_position]
        return None
        
    
    def calculate_average_population_statistics(sa3_code, sa2_position, sa3_position, area_data, population_data,age_position):
        """
            Calculate average population

            Args:
                sa3_code (int)
                sa2_position (int) : sa2 code position in area code
                sa3_position (int) : sa3 code position in area code
                population_data ([str]) : a list that cotains rows of populations data
                area_data ([str]): A list contains area data
                age_position (int): A int indicate the position of selected age group in the age data

            Returns:
                average_population_satistics (float)
        """

        count = 0
        population_count = 0
        population_list = []
        sa3_code_str = str(sa3_code)
        for area_code in area_data: # Read each row in area_data
            if area_code[sa3_position] == sa3_code_str: # Find the row contains required sa3 code
                for population in population_data:
                    if area_code[sa2_position] in population: # Find the row in
                        population_count += int(population[age_position])
                        count += 1
                        population_list.append(int(population[age_position]))
                        break
        return population_count / count, count, population_list


    def calculate_standard_deviations(average_population, data_count, population_list):
        """
            Calculate standard_deviations

            Args:
                population_list -> [int]: list contains selected population data.
                average_population -> int
                data_count (intif bounds[0] <= age and (bounds[1] > age or bounds[1] == 0): the amount of data of the population
            
            Returns:
                Standard_deviations -> float
        """

        result = 0
        for i in population_list:
            result += pow(i-average_population, 2)
        return pow(result / (data_count-1), 0.5)
    

    # Logic part for OP2

    # Find sa3 code related to sa2 code from area_data
    sa3_code_1 = find_sa3_code(sa2_1, area_data, sa2_position, sa3_position)
    sa3_code_2 = find_sa3_code(sa2_2, area_data, sa2_position, sa3_position)

    # Caculate data, prepare to caculate the standard devotion
    average_population_1, data_count_1, population_list_1 = calculate_average_population_statistics(sa3_code_1, sa2_position, sa3_position, area_data, population_data, age_position)
    average_population_2, data_count_2, population_list_2 = calculate_average_population_statistics(sa3_code_2, sa2_position, sa3_position, area_data, population_data, age_position)

    # Caculate the standard_devoation
    standard_devoations_1 = calculate_standard_deviations(average_population_1, data_count_1, population_list_1)
    standard_devoations_2 = calculate_standard_deviations(average_population_2, data_count_2, population_list_2)

    # Structure and return the result
    return [ [sa3_code_1, round(average_population_1, 4), round(standard_devoations_1,4)] , [sa3_code_2, round(average_population_2 , 4), round(standard_devoations_2 , 4)] ]


def find_largest_population_statistics(age_position, area_data, population_data, sa2_po, sa3_po):
    """
        Find sa3 area with largest population in the identified group(op1)

        Args: 
            age_position (int): The position of the selected age group in the first row of population data
            area_data ( [ [str] ] ): A list contains area data
            population_data ( [ [ str ] ] ): A list contains all population data
            sa2_po (int) : The position of sa2 code in area_data
            sa3_po (int) : 

        Returns: 
            a list contains lists: [ [state_name, sa3_name, percentage] ]
            state_name: The state name
            sa3_name: The name of sa3 area with largest population in the identified age froup
            percentage: The percentage of identified age population in the sa3 area
                        (sa3_age_population / sa3_total_population)
    """
    # Find state name
    def find_state_name(area_data,state_po):
        """
            Return a list contains the name of each states (lowercase)

            Args:
                area_data
                state_po -> int : the position of state name in the list

            Returns:
                state ([str]): a list of string contains 
        """
        state = []
        for j in area_data[1:]:
            if not j[state_po] in state:
                state.append(j[state_po])
        return state
    
    # Preprocess the data
    def create_dictionary(area_data, value_po,index_po):
        """
            Create a dictionary based on a table

            Args: 
                area_data:
                value_po -> int : the value position in the list
                index_po -> int : the index position in the list
            
            Returns:
                dictionary { index : value}
        """
        code_dict = {}
        for area in area_data[1:]:
            if not area[index_po] in code_dict:
                code_dict[area[index_po]] = []
                code_dict[area[index_po]].append(area[value_po])
            else: 
                code_dict[area[index_po]].append(area[value_po])
        return code_dict
            

    def create_nested_dict(inner_dict, area_data, index_po):
        """
            Create a nested list based on the given data and index

            Args:
                area_data -> [ [str] ] : a list contains area data, used as index here
                inner_dict -> { } : a dictionary used as inner dictionary

            returns:
                {idex : {inner dict} }
        """
        nested_dict = {}
        for i in area_data[1:]:
            if not i[index_po] in nested_dict:
                nested_dict[i[index_po]] = {}
                nested_dict[i[index_po]] [i[sa3_po]] = inner_dict[i[sa3_po]]
            else:
                nested_dict[i[index_po]] [i[sa3_po]] = inner_dict[i[sa3_po]]
        return nested_dict
    # Pre process data end

    # Calculation helper function 
    def caculate_population_in_grouop(state_name,st_sa3_sa2_dict,sa2_popu_dict):
        """
            This function caculate each sa3 population in specific group

            Args: 
                state_name -> str : A string of statename
                st_sa3_sa2_dict -> dictionary : A nested dictionary {state name -> str : sa3 code -> str : sa2 code -> str}
                sa2_popu_dict -> dictionary : A dictionary {sa2 code -> str : population -> str}

            Returns:
                a dictionary, sa3 code as index, value is population in specific group
                {sa3 code -> str : population -> int}
        """
        result = {}
        for i in st_sa3_sa2_dict[state_name]:
            result[i] = 0
            for j in st_sa3_sa2_dict[state_name][i]:
                result[i] += int(sa2_popu_dict[j][0])
        return result
    
    def find_sa3_largest_population(sa3_popu_dict):
        """
            Find the sa3 area who has the largest population

            Args:
                sa3_popu_dict ( {'sa3 code' : population} )

            Returns:
                max_list:
                    A list contains sa3 code and population
                    [sa3_code -> str, population -> int]
                    
                    If multiple area has the same population, it will choose the one in alphabetical ascending order
                    in terms of area code
        """
        max = 0
        max_code = ''
        max_list = []
        code_list_temp = []
        for i in sorted(list(sa3_popu_dict)):
            if sa3_popu_dict[i] > max:
                max = sa3_popu_dict[i]
                max_code = i
        max_list.append(max_code)
        max_list.append(max)
        return max_list

    def cal_total_sa3_population(sa3_code, population_data,sa3_sa2_dict):
        """
            Caculate the total population of each sa3 area

            Args:
                sa3_code
                population_data
                sa3_sa2_dict

            Returns:
                An interger of total population of that sa3 area
        """
        sa3_code_po_popu = find_name_position(population_data[0], 'code')
        population = 0
        for i in sa3_sa2_dict[sa3_code]:
            for row in population_data[1:]:
                if row[sa3_code_po_popu] == i:
                    for j in row[2:]:
                        population += int(j)
        return population
    
    def find_sa3_name_in_area_data(area_data, sa3_name_po, sa3_code,sa3_po):
        """
            Look up the sa3 area name based on sa3 code

            Return:
                String of sa3 area name
        """
        for row in area_data[1:]:
            if row[sa3_po] == sa3_code:
                return row[sa3_name_po]
        return None
    # Calculation helper function end


    # Logic part for OP3

    # create dictionary, index is sa3code, value is sa2 code
    sa3_sa2_dict = create_dictionary(area_data, sa2_po, sa3_po)

    # Find the position of data in the table
    sa3_name_po = find_name_position(area_data[0],'sa3 name')
    state_po = find_name_position(area_data[0], 's_t name')
    sa2_po_population = find_name_position(population_data[0],'code')

    # Sort the state name to alphabetical sequence
    state = sorted(find_state_name(area_data,state_po))

    # Convert necessary data to dictionary
    sa2_population_dict = create_dictionary(population_data, age_position, sa2_po_population)
    st_sa3_sa2_dict = create_nested_dict(sa3_sa2_dict, area_data, state_po)


    OP3 = []

    for i in state:
        state_sa3_popu_dict = caculate_population_in_grouop(i, st_sa3_sa2_dict,sa2_population_dict)

        # max_list store the name and population of a state -> [str, int]
        max_list = find_sa3_largest_population(state_sa3_popu_dict)
        sa3_code = max_list[0]

        state_total_popu = cal_total_sa3_population(max_list[0], population_data, sa3_sa2_dict)
        sa3_name = find_sa3_name_in_area_data(area_data, sa3_name_po, sa3_code, sa3_po)
        OP3.append([i, sa3_name, round(max_list[1] / state_total_popu,4)])

    return OP3


def caculate_correlation(sa2_1, sa2_2, population_data):
    """
        caculate the correlation of 2 area in all age group

        Args: 
            sa2_1, sa2_2 : Integer input
            population_data: list contain str
        
        Returns:
            a float  equals to the correlation result, rounded
    """

    # put are population in all age group in a list
    def organize_population_in_group(sa2_code, sa2_po, population_data):
        """
            Return a list contains interger, which are the population data of each age group in the same sa2 area
        """
        population_list = []
        for row in population_data[1:]:
            if row[sa2_po] == sa2_code:
                for data in row[2:]:
                    population_list.append(int(data))
                break
        return population_list
    
    # caculate the result.
    def caculate_correlation_coefficient(data_x, data_y):
        """
            Caculate the correlation coefficient base on the given data

            Args:
                data1, data2:
                    list contains integer, length are same
            
            Returns:
                correlation coefficient
        """

        if len(data_x) == len(data_y):
            data_count = len(data_x)
        else:
            # data incorrect
            return 0
        
        aver_x = sum(data_x) / data_count
        aver_y = sum(data_y) / data_count

        numerator = 0
        denominator = 0
        denominator_x = 0
        denominator_y = 0
        for i in range(data_count):
            # Caculate the numerator
            numerator += (data_x[i] - aver_x) * (data_y[i] - aver_y)

            # Caculate the ndominator
            denominator_x += ( (data_x[i] - aver_x) ** 2 )
            denominator_y += ( (data_y[i] - aver_y) ** 2 )
        denominator = pow(denominator_x * denominator_y, 0.5)

        if denominator != 0:
            return (numerator / denominator)
        return 0

    # Logic part for OP4

    # Find position of sa2 code in populaion data table
    code_po_population = find_name_position(population_data[0], 'code')

    # Put the data into lists
    list1 = organize_population_in_group(sa2_1, code_po_population, population_data)
    list2 = organize_population_in_group(sa2_2, code_po_population, population_data)

    result = caculate_correlation_coefficient(list1, list2)

    return round(result,4)


"""
    Debugging Documentation

    Issue 1 (Mar.29 2025):
        -Test Case:
            main('SampleData_Areas.csv','SampleData_Populations.csv', 18, '401011001', '401021003')

        -Error Description
            ZeroDivisionError: division by zero
        
        -Erroneous Code Snippet:
            In calculate_average_population

        for area_code in area_data: # Read each row in area_data
            if int(area_code[sa3_position]) == sa3_code_str: # Find the row contains required sa3 code
                for population in population_data:
                    if area_code[sa2_position] in population: # Find the row in
                        population_count += int(population[age_position])
                        count += 1
                        population_list.append(int(population[age_position]))
                        break
        return population_count / count, count, population_list
            
        -Reflection
            Actually it was triggered in another line. I incorrectly tring to compare a str with an int.
            I found sometimes the bug wasn't triggered at the line when the error occures.
            Mighe be a variable far away from the line where error occures
        
    Issue 2 (Mar.29 2025):
        -Test Case
            main('SampleData_Areas.csv','SampleData_Populations.csv', 18, '401011001', '401021003')
            
        -Error Description
            TypeError: unsupported operand type(s) for +=: 'int' and 'str'

        -Erroneous Code Snippet
            population_count += population[age_position]
            
        -Reflection    
            Didn't convert data type. The 2 issues above made me realized data type restricted some operations.
            Once the data became more, its harder to keep in track of data type.
            I think thats why its important to seperate codes into different functions.

    Issue 3 (Apr. 6 2025)

        - Test Case
            >>> OP1, OP2, OP3, OP4 = main('SampleData_Areas.csv', 'SampleData_Populations.csv', 18, '401011001', '401021003')
            >>> OP2
            ([['40101', 782.5, 376.8879], ['40102', 689.625, 493.9609]], 4, 2)

        - Error Description
            Output error. Not as excepted

        - Erroneous Code Snippet
            return [ [sa3_code_1, round(average_population_1, 4), round(standard_devoations_1,4)] , [sa3_code_2, round(average_population_2 , 4), round(standard_devoations_2 , 4)] ], sa2_position, sa3_position
        
        - Reflection
            I used to put the calculating code position in OP2 part. 
            But after I restructure the code, I forgot to remove it.
            I found restructuring the code when in the middle of the development will always cause this issue.
            Although is not hard to avioid.
            
    Issue 4 (Apr.8 2025)
    
        - Test Case
            main('SampleData_Areas.csv', 'SampleData_Populations.csv', 85, '401011001', '401021003')

        - Error Description
            if bounds[0] <= age and (bounds[1] > age or bounds[1] == 0):
                                     ^^^^^^^^^^^^^^^
            TypeError: '>' not supported between instances of 'NoneType' and 'int'

        - Erroneous Code Snippet
            if bounds[0] <= age and (bounds[1] > age or bounds[1] == 0
        
        - Reflection
            I accidently compare a none type with a int. That will cause type error.
            I changed the code to follows:
                if bounds[0] <= age and (bounds[1] == None or age <=bounds[1])
            So python will first check if it is none, this will not result to an type error.
            I realized sometimes the squence of each command will matter even in 'or' statment.
"""