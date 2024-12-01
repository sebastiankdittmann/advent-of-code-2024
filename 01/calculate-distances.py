from list_module import read_number_lists_from_file

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
    list1, list2 = read_number_lists_from_file('./01/lists.txt')

    sum_of_distances = calculate_sum_of_distances(list1, list2)
    print("The sum of distances is :", sum_of_distances)
