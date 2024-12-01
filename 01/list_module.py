import os

def read_number_lists_from_file(file_path):
    print("Current Working Directory:", os.getcwd())

    # load text file line by line
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # read two numbers separated by space into two lists
    list1 = []
    list2 = []

    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    print("List 1 length:", len(list1))
    print("List 2 length:", len(list2))
    
    return list1,list2