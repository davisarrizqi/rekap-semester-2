import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if(my_list[j] < my_list[min_index]):
                min_index = j

        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

def descend_bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] < my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def descend_selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if(my_list[j] > my_list[min_index]):
                min_index = j

        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def descend_insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp > my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


# if you want to run this one, change the __main_ into __main__
if __name__ == '__main_': #--> __main__ for true
    my_list = [4, 2, 6, 5, 1, 3]
    print('============ FINAL RESULT ============')
    print('Ascending Bubble Sort:', bubble_sort(my_list))
    print('Descending Bubble Sort:', descend_bubble_sort(my_list), end='\n\n')

    print('Ascending Selection Sort:', selection_sort(my_list))
    print('Descending Selection Sort:', descend_selection_sort(my_list), end='\n\n')

    print('Ascending Insertion Sort:', insertion_sort(my_list))
    print('Descending Insertion Sort:', descend_insertion_sort(my_list))
    print('======================================')




# another version, by @davis_arrizqi
class Sorting:
    def __init__(self, my_list):
        self.my_list = my_list
        self.errorHandling()

    def errorHandling(self):
        # check is it a true data type or not
        if(isinstance(self.my_list, list)): pass
        else: print(f'Peringatan!, Value Tidak Boleh Berjenis {type(self.my_list)}'); return False

        # check is it a true value in the list or not
        for data in self.my_list:
            if(isinstance(data, int) or isinstance(data, float)): pass
            else: print(f'Peringatan!, Data Pada List Tidak Boleh Berjenis {type(data)}'); return False

    def ascending_bubble_sort(self):
        # make sure that if there is the potential value then bubbled it
        for data in range(len(self.my_list) - 1, 0, -1):
            for num in range(data):
                if(self.my_list[num] > self.my_list[num + 1]):
                    self.my_list[num], self.my_list[num + 1] = self.my_list[num + 1], self.my_list[num]
        return True

    def descending_bubble_sort(self):
        # just the same, but it's descending
        for data in range(len(self.my_list) - 1, 0, -1):
            for num in range(data):
                if(self.my_list[num] < self.my_list[num + 1]):
                    self.my_list[num], self.my_list[num + 1] = self.my_list[num + 1], self.my_list[num]
        return True

    def ascending_selection_sort(self):
        # make a note for the step
        stepValue = len(self.my_list)
        startValue = 0; temp = None

        for counter in range(len(self.my_list)):
            # data declaration
            minValueIndex = counter
            
            # found the minimum index value
            for data in range(startValue, len(self.my_list), +1):
                if(self.my_list[minValueIndex] > self.my_list[data]):
                    minValueIndex = data
            # animation src: https://www.youtube.com/watch?v=xWBP4lzkoyM

            # switch the minimum value with the present value of counter
            temp = self.my_list[counter]; stepValue -= 1; startValue += 1
            self.my_list[counter] = self.my_list[minValueIndex] 
            self.my_list[minValueIndex] = temp

        # be prepared for true or false situation check 
        return True

    def descending_selection_sort(self):
        # make a note for the step
        stepValue = len(self.my_list)
        startValue = 0; temp = None

        for counter in range(len(self.my_list)):
            # data declaration
            maxValueIndex = counter
            
            # found the minimum index value
            for data in range(startValue, len(self.my_list), +1):
                if(self.my_list[maxValueIndex] < self.my_list[data]):
                    maxValueIndex = data
            # animation src: https://www.youtube.com/watch?v=xWBP4lzkoyM

            # switch the minimum value with the present value of counter
            temp = self.my_list[counter]; stepValue -= 1; startValue += 1
            self.my_list[counter] = self.my_list[maxValueIndex] 
            self.my_list[maxValueIndex] = temp

        # be prepared for true or false situation check 
        return True

    def ascending_insertion_sort(self):
        # make a note for the data counter
        tempData = len(self.my_list)
        selectedIndex = self.my_list[0]

        # let's make a repeat logic
        for counter in range(len(self.my_list)):
            
            # when it's count is 0, it's skipped
            if(counter == 0): continue
            selectedIndex = counter
            # keep it up so that we can compare with the descend
            
            # make an analysis logic for exchange
            for data in range(counter, -1, -1):
                if(self.my_list[counter] < self.my_list[data]):
                    tempData = self.my_list[data]
                    self.my_list[data] = self.my_list[counter]
                    self.my_list[counter] = tempData

        # same as before
        return True

    def descending_insertion_sort(self):
        # make a note for the data counter
        tempData = len(self.my_list)
        selectedIndex = self.my_list[0]

        # let's make a repeat logic
        for counter in range(len(self.my_list)):
            
            # when it's count is 0, it's skipped
            if(counter == 0): continue
            selectedIndex = len(self.my_list) - counter
            
            # make an analysis logic for exchange
            for data in range(selectedIndex, -1, -1):
                if(self.my_list[selectedIndex] > self.my_list[data]):
                    tempData = self.my_list[data]
                    self.my_list[data] = self.my_list[selectedIndex]
                    self.my_list[selectedIndex] = tempData

        # same as before
        return True

# avoid the auto run when it's imported from the other files
if __name__ == '__main__':
    mySorting = Sorting([18, 1, 10, 205, 203])
    mySorting.descending_insertion_sort()
    print(mySorting.my_list)