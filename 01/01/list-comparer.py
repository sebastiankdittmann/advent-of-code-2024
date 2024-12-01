import os

def read_lists_from_file(file_path):
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

def calculate_sum_of_distances(list1, list2):
    number_of_pairs = min(len(list1), len(list2))
    counter = 0
    sum_of_distances = 0
    
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    while counter < number_of_pairs:
        if(list1[counter] <= list2[counter]):
            distance = list2[counter] - list1[counter]
            sum_of_distances += distance
        else:
            distance = list1[counter] - list2[counter]
            sum_of_distances += distance
        counter += 1
    
    return sum_of_distances
    

def main():
    list1, list2 = read_lists_from_file('./lists.txt')

    sum_of_distances = calculate_sum_of_distances(list1, list2)
    print("The sum of distances is :", sum_of_distances)
    

if __name__ == "__main__":
    main()
