
def cleaningdata(csvfile_1,csvfile_2):
    csvfile_2_a = open(csvfile_2,"r")
    
    #find the length of the file for reference
    data_length = open(csvfile_2,"r")
    data_length_reference = len(list(data_length))
    #print(data_length_reference)#testing length of data file #539
    data_length.close()
    
    #cleaning duplicated rows
    clean_SampleData_Areas_P2_list = []
    count = 0
    marker = ''
    for i in range (data_length_reference):
        readlines = csvfile_2_a.readline()
        reading_line = readlines.lower()
        reading_line = reading_line.split(",")
        reading_line[-1] = reading_line[-1].strip()
        if count > 0: 
            reading_line[2:11] = map(int,reading_line[2:11])
        count = count + 1
        
        if marker != reading_line[0]: 
            clean_SampleData_Areas_P2_list.append(reading_line)
            marker = reading_line[0]
        
        
    clean_SampleData_Areas_P2_list = sorted(clean_SampleData_Areas_P2_list, key=lambda x:x[0])
    clean_SampleData_Areas_P2_list.insert(0,clean_SampleData_Areas_P2_list[-1])
    clean_SampleData_Areas_P2_list.pop(-1)
    #print(len(clean_SampleData_Areas_P2_list))#539
    #print(clean_SampleData_Areas_P2_list)
    
    return clean_SampleData_Areas_P2_list
   
    
#cleaningdata('SampleData_Areas_P2.csv','SampleData_Populations_P2.csv')

def op1(csvfile_1,csvfile_2):
    cleanfile_csv = cleaningdata('SampleData_Areas_P2.csv','SampleData_Populations_P2_test.csv')
    
    
    csvfile_2_a = open(csvfile_2,"r")
    largest_population_dictionary = {}
    
    #only read and take out the heading of the data and construct a dictionary with [] as vaule
    for i in range (1):
        readlines_population = csvfile_2_a.readline()
        reading_line_population = readlines_population.split(",")
        #print(reading_line_population)
        reading_line_population[-1] = reading_line_population[-1].strip()
        reading_line_population.remove('Area_Code_Level2')
        reading_line_population.remove('Area_Name_Level2')
        
    
    for l in range(len(reading_line_population)):
        string_age_group = reading_line_population[l]
        string_age_group = string_age_group.replace('Age ','')
        reading_line_population[l]= string_age_group.replace(' and over','-None')
    
    reading_line_population = sorted(reading_line_population)    
    
    #print(reading_line_population)
    
    for l in range(len(reading_line_population)):
        largest_population_dictionary[reading_line_population[l]] = []
    print(largest_population_dictionary)
    
    csvfile_2_a.close()
    
    #find the length of the file for reference
    data_length = open(csvfile_2,"r")
    
    data_length_reference = len(list(data_length))
    #print(data_length_reference)#testing length of data file #539
    
    data_length.close()
    
    #find the position of the age group
    position_dictionbary = {}
    readlines = cleanfile_csv[0]
    age_position_index_list = []
    
    for i in readlines:
        if i in readlines:
            age_position = readlines.index(i)
            age_position_index_list.append(age_position)
    #print(age_position_index_list)
    
    for i in range(len(readlines)):
        position_dictionbary[readlines[i]] = age_position_index_list[i]
    print(position_dictionbary)
    
    
        
            
     
    #find the maxiumm in age group in SA2
    max_list = []
    
    position_key = readlines.copy()
    
    position_key.pop(0)
    position_key.pop(0)
    
    print(position_key)
    for i in range(len(position_key)):
        max_list.append([])
    #print(max_list)
    step = 0
    for k in position_key:
        if k != position_key[0]:
            step = step + 1
        for i in range(data_length_reference):#539
            max_list[step].append(cleanfile_csv[i][0:position_dictionbary[k]+1])
            #print(max_list)
#         max_list_10_to_19.append(cleanfile_csv[i][0:position_dictionbary['Age 10-19']+1])
#         max_list_20_to_29.append(cleanfile_csv[i][0:position_dictionbary['Age 20-29']+1])
#         max_list_30_to_39.append(cleanfile_csv[i][0:position_dictionbary['Age 30-39']+1])
#         max_list_40_to_49.append(cleanfile_csv[i][0:position_dictionbary['Age 40-49']+1])
#         max_list_50_to_59.append(cleanfile_csv[i][0:position_dictionbary['Age 50-59']+1])
#         max_list_60_to_69.append(cleanfile_csv[i][0:position_dictionbary['Age 60-69']+1])
#         max_list_70_to_79.append(cleanfile_csv[i][0:position_dictionbary['Age 70-79']+1])
#         max_list_80_to_more.append(cleanfile_csv[i][0:position_dictionbary['Age 80 and over']+1])
    #print(max_list)
    #print(len(max_list))
#     print(max_list_10_to_19)
#     print(max_list_20_to_29)
#     print(max_list_30_to_39)
#     print(max_list_40_to_49)
#     print(max_list_50_to_59)
#     print(max_list_60_to_69)
#     print(max_list_70_to_79)
#     print(max_list_80_to_more)
#     #max_list = [max_list_0_to_9, max_list_10_to_19, max_list_20_to_29, max_list_30_to_39, max_list_40_to_49, max_list_50_to_59, max_list_60_to_69, max_list_70_to_79, max_list_80_to_more]
#     number_list0 = []
#     number_list1 = []
#     number_list2 = []
#     number_list3 = []
#     number_list4 = []
#     number_list5 = []
#     number_list6 = []
#     number_list7 = []
#     number_list8 = []
    number_list = []
    for i in range(len(max_list)):
        number_list.append([])
    #print(number_list)    
    for l in range(len(max_list)):
        for i in range(1,len(max_list[l])):
            number_list[l].append(max_list[l][i][-1])
    #print(number_list) 
#     for i in range(1,len(max_list_10_to_19)):
#         number_list1.append(max_list_10_to_19[i][-1])
#     
#     for i in range(1,len(max_list_20_to_29)):
#         number_list2.append(max_list_20_to_29[i][-1])
#     
#     for i in range(1,len(max_list_30_to_39)):
#         number_list3.append(max_list_30_to_39[i][-1])
#     
#     for i in range(1,len(max_list_40_to_49)):
#         number_list4.append(max_list_40_to_49[i][-1])
#     
#     for i in range(1,len(max_list_50_to_59)):
#         number_list5.append(max_list_50_to_59[i][-1])
#     
#     for i in range(1,len(max_list_60_to_69)):
#         number_list6.append(max_list_60_to_69[i][-1])
#     
#     for i in range(1,len(max_list_70_to_79)):
#         number_list7.append(max_list_70_to_79[i][-1])
#     
#     for i in range(1,len(max_list_80_to_more)):
#         number_list8.append(max_list_80_to_more[i][-1])

  
    for i in range(len(number_list)):
        #print(max(number_list[i]),number_list[i].index(max(number_list[i])))
        ans0 = cleanfile_csv[number_list[i].index(max(number_list[i]))+1][1]
        #print(ans0)#op1(3)
        
#     
#     print('')
#     print(max(number_list0),number_list0.index(max(number_list0)))#4814 at 381 position, correct
#     print(cleanfile_csv[number_list0.index(max(number_list0))+1])
#     ans0 = cleanfile_csv[number_list0.index(max(number_list0))+1][1]
#     print(ans0)
    
#     print('')
#     print(max(number_list1),number_list1.index(max(number_list1)))#4812 at 381 position, correct
#     print(cleanfile_csv[number_list1.index(max(number_list1))+1])
#     ans1 = cleanfile_csv[number_list1.index(max(number_list1))+1][1]
#     print(ans1.lower())
#     
#     print('')
#     print(max(number_list2),number_list2.index(max(number_list2)))#8104 at 1 position, correct
#     print(cleanfile_csv[number_list2.index(max(number_list2))+1])
#     ans2 = cleanfile_csv[number_list2.index(max(number_list2))+1][1]
#     print(ans2.lower())
#     
#     print('')
#     print(max(number_list3),number_list3.index(max(number_list3)))#5194 at 36 position, correct
#     print(cleanfile_csv[number_list3.index(max(number_list3))+1])
#     ans3 = cleanfile_csv[number_list3.index(max(number_list3))+1][1]
#     print(ans3.lower())
#     
#     print('')
#     print(max(number_list4),number_list4.index(max(number_list4)))#4118 at 381 position, correct
#     print(cleanfile_csv[number_list4.index(max(number_list4))+1])
#     ans4 = cleanfile_csv[number_list4.index(max(number_list4))+1][1]
#     print(ans4.lower())
#     
#     print('')
#     print(max(number_list5),number_list5.index(max(number_list5)))#3955 at 286 position, correct
#     print(cleanfile_csv[number_list5.index(max(number_list5))+1])
#     ans5 = cleanfile_csv[number_list5.index(max(number_list5))+1][1]
#     print(ans5.lower())
#     
#     print('')
#     print(max(number_list6),number_list6.index(max(number_list6)))#3096 at 59 position, correct
#     print(cleanfile_csv[number_list6.index(max(number_list6))+1])
#     ans6 = cleanfile_csv[number_list6.index(max(number_list6))+1][1]
#     print(ans6.lower())
#     
#     print('')
#     print(max(number_list7),number_list7.index(max(number_list7)))#3664 at 151 position, correct
#     print(cleanfile_csv[number_list7.index(max(number_list7))+1])
#     ans7 = cleanfile_csv[number_list7.index(max(number_list7))+1][1]
#     print(ans7.lower())
#     
#     print('')
#     print(max(number_list8),number_list8.index(max(number_list8)))#1933 at 151 position, correct
#     print(cleanfile_csv[number_list8.index(max(number_list8))+1])
#     ans8 = cleanfile_csv[number_list8.index(max(number_list8))+1][1]
#     print(ans8.lower())
    
#     ans0 = cleanfile_csv[number_list0.index(max(number_list0))+1][1].lower()
#     ans1 = cleanfile_csv[number_list1.index(max(number_list1))+1][1].lower()
#     ans2 = cleanfile_csv[number_list2.index(max(number_list2))+1][1].lower()
#     ans3 = cleanfile_csv[number_list3.index(max(number_list3))+1][1].lower()
#     ans4 = cleanfile_csv[number_list4.index(max(number_list4))+1][1].lower()
#     ans5 = cleanfile_csv[number_list5.index(max(number_list5))+1][1].lower()
#     ans6 = cleanfile_csv[number_list6.index(max(number_list6))+1][1].lower()
#     ans7 = cleanfile_csv[number_list7.index(max(number_list7))+1][1].lower()
#     ans8 = cleanfile_csv[number_list8.index(max(number_list8))+1][1].lower()

    
    
    #find the maximum in age group in SA3 code
    cleanfile_csv_0 = cleanfile_csv.copy()
    sample = ''
    unique_sa3_code = []
    cleanfile_csv_0.pop(0)
    #print(cleanfile_csv_0)
    #print(cleanfile_csv)
    for i in cleanfile_csv_0:
        if i[0][0:5] != sample:
            sample = i[0][0:5]
            unique_sa3_code.append(i[0][0:5])
    print(unique_sa3_code)
   
    unique_sa3_code_population = []
    for i in range(len(unique_sa3_code)):#77
        unique_sa3_code_population.append([])
    
    unique_sa3_code_population_summing = []
    for i in range(len(unique_sa3_code)):#77
        unique_sa3_code_population_summing.append([])
    
    
   
    check = ''
    step = 0
    steps = 0
    #position_key_list =
    for k in position_key: #(position_dictionbary[k])
        print(position_dictionbary[k])
        if k != position_key[0]:
            steps = steps + 1
             
    for l in range(len(unique_sa3_code)):
        for i in cleanfile_csv_0:
            if i[0][0:5] == unique_sa3_code[l]:
                unique_sa3_code_population[l].append(i[2])#change the number '2'
                unique_sa3_code_population_summing[l].append(sum(unique_sa3_code_population[l]))
                
    print(unique_sa3_code_population)
    print(unique_sa3_code_population_summing)
    
    unique_sa3_code_population_sum = []
    for i in unique_sa3_code_population_summing:
        unique_sa3_code_population_sum.append(i[-1])
    print(unique_sa3_code_population_sum)
    print(unique_sa3_code_population_sum.index(max(unique_sa3_code_population_sum)))
    print(unique_sa3_code[unique_sa3_code_population_sum.index(max(unique_sa3_code_population_sum))])   
    
    dictionary_with_population = {}
    for i in range(len(position_key)):
        dictionary_with_population[position_key[i]] = unique_sa3_code_population
    #print(dictionary_with_population)
        
            
    

op1('SampleData_Areas_P2.csv','SampleData_Populations_P2_test.csv')
