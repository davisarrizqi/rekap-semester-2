import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)

def descend_merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1

    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined

def descend_merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = descend_merge_sort(my_list[:mid_index])
    right = descend_merge_sort(my_list[mid_index:])

    return descend_merge(left, right)

def descend_pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] > my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def descend_quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = descend_pivot(my_list, left, right)
        descend_quick_sort_helper(my_list, left, pivot_index-1)
        descend_quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def descend_quick_sort(my_list):
    descend_quick_sort_helper(my_list, 0, len(my_list)-1)


if __name__ == '__main_':
    
    # merge sort
    original_list = [3, 1, 4, 2]
    sorted_list = merge_sort(original_list)
    descend_sorted_list = descend_merge_sort(original_list)
    
    # show us - merge sort
    print('======= Merge Sort =======')
    print('Original List:', original_list)
    print('Sorted List:', sorted_list)
    print('Descend Sorted ListL:', descend_sorted_list)
    print('==========================\n')

    # quick sort - proccess and print
    print('======= Quick Sort =======')
    my_list = [4, 6, 1, 7, 3, 2, 5]
    print('Original List:', my_list)
    
    quick_sort(my_list)
    print('Sorted List:', my_list)
    
    descend_quick_sort(my_list)
    print('Descend Sorted List:', my_list)
    print('==========================\n')


# another version, by @davis_arrizqi - ascending
def isHaveSorted(my_list):
    for counter in range(len(my_list)-1):
        for data in range(counter, len(my_list), +1):
            if (my_list[counter] <= my_list[data]): pass
            else: return False
    return True

def quick_sort_system(my_list):
    # avoid particle list bugs
    if(len(my_list) == 2):
        if(my_list[0] > my_list[1]):
            my_list[0], my_list[1] = my_list[1], my_list[0]
            return my_list 
    elif(len(my_list) <= 1): return my_list

    # declare it first
    indexNumber = -1; pos = -1; pivot = my_list[pos]; highest_value = my_list[0]
    leftSide = []; rightSide = []; lowest_value = my_list[0]

    # avoid quick sort common bugs, when -1 index is the lowest or highest value
    for data in range(len(my_list)):
        if(my_list[data] < lowest_value): lowest_value = my_list[data]

    for data in range(len(my_list)):
        if(my_list[data] > highest_value): highest_value = my_list[data]
    
    if(my_list[-1] == lowest_value or my_list[-1] == highest_value): 
        pos = random.randint(1, len(my_list)-2)
        my_list[pos], my_list[-1] = my_list[-1], my_list[pos]
        pos = -1; pivot = my_list[pos]

    # list analyze
    for counter in range(len(my_list)-1):
        if(my_list[counter] < pivot):
            indexNumber += 1
            my_list[counter], my_list[indexNumber] = my_list[indexNumber], my_list[counter]

    # make a place for zero index - troubleshoot method
    for counter in range(len(my_list)-1):
        if(my_list[0] < my_list[counter+1] and my_list[0] > my_list[counter]): 
            my_list.insert(counter+1, my_list[0])
            del my_list[0]; break
    
    # make a place for the pivot number - troubleshoot method
    for counter in range(len(my_list)-1):
        if(pivot < my_list[counter+1] and pivot > my_list[counter]): 
            my_list.insert(counter+1, my_list[pos])
            del my_list[pos]; break
    
    divideNumber = len(my_list)/2 if len(my_list)%2==0 else (len(my_list)+1)/2
    leftSide = my_list[:int(divideNumber)]
    rightSide = my_list[int(divideNumber):len(my_list)]
    
    while not isHaveSorted(leftSide):
        leftSide = quick_sort_system(leftSide)

    while not isHaveSorted(rightSide):
        rightSide = quick_sort_system(rightSide)

    my_list = leftSide + rightSide
    selected_value = my_list[0]; value_index = 0
    
    # try to evaluate the result, because of it's bugs
    if(not isHaveSorted(my_list) and len(my_list) > 2):
        # looking about bad element index
        for data in range(len(my_list)-1):
            if(data == 0): continue
            if(my_list[data] < my_list[data+1] and my_list[data] > my_list[data-1]): pass
            else: selected_value = my_list[data]; value_index = data; break
        
        for data in range(len(my_list)-1):
            if(data == 0): continue
            if(value_index != 0 and selected_value < my_list[data+1] and selected_value > my_list[data-1]):
                my_list.insert(data, selected_value); del my_list[data]

    return my_list

def quick_sort(my_list):
    # avoid -1 index minimum and maximum value bugs, fixed
    if(my_list[-1] == min(my_list)):
        pos = random.randint(0, len(my_list)-2)
        my_list[-1], my_list[pos] = my_list[pos], my_list[-1]
    
    while not isHaveSorted(my_list):
        my_list = quick_sort_system(my_list)
        if(not isHaveSorted(my_list)): random.shuffle(my_list)
    return my_list

def quick_sort_troubleshooter(listResult):
    for data in listResult:
        result = quick_sort(data)
        if(isHaveSorted(result)): pass
        else: return False
    return True

if __name__ == '__main__':
    listResult = []; my_list = []
    print('============= Daftar List =============')
    my_list = [10, 80, 30, 90, 40, 50, 70]
    listResult.append(my_list)
    my_list = quick_sort(my_list)
    print(my_list)
    
    my_list = [18, 10, 2003, 2005, 2004, 2002]
    listResult.append(my_list)
    my_list = quick_sort(my_list)
    print(my_list)

    my_list = [13, 21, 34, 124, 41, 12, 7]
    listResult.append(my_list)
    my_list = quick_sort(my_list)
    print(my_list)

    my_list = [41, 2131, 213213, 123213, 32123]
    listResult.append(my_list)
    my_list = quick_sort(my_list)
    print(my_list)

    my_list = [4212, 12312312, 123, 12312, 31231]
    listResult.append(my_list)
    my_list = quick_sort(my_list)
    print(my_list)
    print('======================================')


    print('\n=========== Status Eksekusi ==========')
    result = quick_sort_troubleshooter(listResult)
    if(result): print('Berhasil!, Tidak Ada Error!')
    print('======================================')
