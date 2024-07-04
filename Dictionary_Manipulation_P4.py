def sort_dict_by_values(d: dict)->dict:
    listd = list(d.items()) #store dict items as lists

    for i in range(1, len(listd)):
        current_item = listd[i]  # store the current value tuple to be inserted
        j = i - 1
        while (j >= 0 & listd[j][1] > current_item[1]): # Shift elements of the sorted part
            listd[j + 1] = listd[j]
            j -= 1
        listd[j + 1] = current_item #Insert the current tuple into its correct position
    
    sort_dict = {}
    for item in listd:   # Convert the sorted list of tuples back
        sort_dict[item[0]] = item[1]
    
    return sort_dict

input_dict = {'a': 2, 'b': 1, 'c': 3}
sorted_dict = sort_dict_by_values(input_dict)
print(sorted_dict)
