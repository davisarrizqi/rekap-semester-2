import os; os.system('cls' if os.name == 'nt' else 'clear')
import random
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Troubleshooter:
    def __init__(self, headValue):
        self.head = Node(headValue)
        self.length = 1

    def maxValue(self):
        temp = self.head
        highestValue = temp.value

        while temp:
            if(temp.value > highestValue):
                highestValue = temp.value
            temp = temp.right
        return highestValue

    def append(self, value):
        new_node = Node(value)
        temp = self.head; pre = temp

        while temp.right:
            pre = temp; temp = temp.right
        temp.right = new_node
        self.length += 1; return True

    def calculateAverage(self):
        listAverage = 0
        temp = self.head

        while temp:
            listAverage += temp.value
            temp = temp.right
        listAverage /= self.length
        return listAverage

    def calculateStandardDeviation(self):
        averageNumber = self.calculateAverage()
        temp = self.head; totalNumber = 0

        while temp:
            totalNumber += ((temp.value - averageNumber) ** 2)
            temp = temp.right
        totalNumber /= self.length
        totalNumber = round(math.sqrt(totalNumber), 2)
        return totalNumber

    def highestErrorCheck(self, binaryMaxValue):
        if(binaryMaxValue == self.maxValue()): return True
        else: return False

    def print_elements(self):
        if(self.length <= 0): return None
        temp = self.head
        while temp: print(temp.value); temp = temp.right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.troubleShooter = None

    def insert(self, value):
        new_node = Node(value)
        temp = self.root

        # new root logic
        if(self.root == None):
            self.troubleShooter = Troubleshooter(value)
            self.root = new_node; return True

        while True:
            # avoid error and replacement bug
            if(temp.value == new_node.value): return None
            
            # left node logic
            if(new_node.value < temp.value):
                if(temp.left == None):
                    temp.left = new_node
                    self.troubleShooter.append(new_node.value)
                    return True
                temp = temp.left

            # right node logic
            else:
                if(temp.right == None):
                    temp.right = new_node
                    self.troubleShooter.append(new_node.value)
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if(value < temp.value):
                temp = temp.left
            elif(value > temp.value):
                temp = temp.right
            else: return True
            # executed when it's equal 
        return False

    def min_value_node(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def max_value_node(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node

    def MaxValue(self):
        if(self.root == None): return None
        return self.max_value_node(self.root).value

    def MinValue(self):
        if(self.root == None): return None
        return self.min_value_node(self.root).value

    def AverageValue(self):
        if(self.root == None): return None
        return self.troubleShooter.calculateAverage()

    def StdDevValue(self):
        if(self.root == None): return None
        return self.troubleShooter.calculateStandardDeviation()

    def executeTroubleCheck(self):
        if(self.troubleShooter != None):
            if(self.troubleShooter.highestErrorCheck(self.max_value_node(self.root).value)): print('Note: No Error Detected!'); return True
            else: print(f'Note: Error Detected!, {self.troubleShooter.maxValue()} != {self.max_value_node(self.root).value}'); return False
    # make sure that our binary search tree is a good tree enough

    def showAllDataFromTroubleShooter(self):
        if(self.troubleShooter != None):
            self.troubleShooter.print_elements()
        # logic by davis_arrizqi

if __name__ == "__main__":
    myTree = BinarySearchTree()
    print('===== Final Result =====')
    
    # declaration and data insertion
    listNumber = [6, 2, 3, 1]
    for data in listNumber: myTree.insert(data)
    
    # method for check the trouble
    myTree.executeTroubleCheck()

    # show max value
    maxValue = myTree.MaxValue()
    print(f'Max Value: {maxValue}')

    # show average value
    averageValue = myTree.AverageValue()
    print(f'Average Value: {averageValue}')

    # show standard deviation
    stdDeviationValue = myTree.StdDevValue()
    print(f'Standard Deviation: {stdDeviationValue}')
    print('========================')

    # show all data = debug
    # myTree.showAllDataFromTroubleShooter()
