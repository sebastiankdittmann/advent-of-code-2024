from list_module import read_number_lists_from_file

def calculate_occurences(list1, list2):
    grouped_list2 = {}
    
    for number in list2:
        if number in grouped_list2:
            grouped_list2[number] += 1
        else:
            grouped_list2[number] = 1
    
    return grouped_list2

def calculate_similarities(list1, list2):
    grouped_list2 = calculate_occurences(list1, list2)
    similarity = 0
    
    for number in list1:
        if number in grouped_list2:
            print("Number", number, "occurs", grouped_list2[number], "times in list2")
            similarity += grouped_list2[number] * number
        else:
            print("Number", number, "does not occur in list2")
            
    return similarity
    

def main():
    list1, list2 = read_number_lists_from_file('./01/lists.txt')
    similarity = calculate_similarities(list1, list2)
    print("The similarity is :", similarity)    
    
if __name__ == "__main__":
    main()