import os; import random
os.system("cls" if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # error handling
        if(self.length == 0): return None

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return True

    def append(self, value):
        new_node = Node(value)
        if(self.length <= 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        if(self.length <= 0): return None
        temp = self.head; pre = self.head

        self.length -= 1
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre

        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if(self.length <= 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            self.length += 1
        return True

    def pop_first(self):
        if(self.length <= 0): return None
        temp = self.head

        self.head = self.head.next
        self.length -= 1

        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if(index < self.length * -1): return None
        if(index >= self.length): return None
        elif(index < 0 and index < self.length): index = self.length + index

        temp = self.head
        for data in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value 
        return True

    def insert(self, index, value):
        if(index < 0 or index > self.length): return False
        elif(index == 0): return self.prepend(value)
        elif(index == self.length): return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        pre = temp.next; temp.next = new_node
        temp.next.next = pre; self.length += 1
        return True

    def remove(self, index):
        if(index < 0 or index > self.length): return None
        elif(index == 0): return self.pop_first()
        elif(index == self.length - 1): return self.pop()
        
        temp = self.get(index - 1); pre = temp.next
        temp.next = temp.next.next; self.length -= 1

        if(self.length <= 0):
            self.head = None
            self.tail = None
        return pre

    def reverse_list(self):
        if(self.length < 2): return False

        counter = self.length/2 if self.length %2 == 0 else (self.length-1)/2
        for data in range(int(counter)):
            leftValue = self.get(data).value
            rightValue = self.get(self.length - data - 1).value
            self.set_value(data, rightValue)
            self.set_value(self.length - data - 1, leftValue)
        return True
            

if __name__ == '__main__':
    # deklarasi class
    linkedList = LinkedList(23)
    
    # fungsi append
    linkedList.append(43); linkedList.append(12)
    linkedList.append(71); linkedList.append(87)
    
    # fungsi untuk melakukan reverse dan print
    linkedList.reverse_list()
    linkedList.print_list()
    