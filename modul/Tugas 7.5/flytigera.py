import os; os.system('cls' if os.name == 'nt' else 'clear')
import random

class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        if(self.length <= 0): return None
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next
        return True

    def append(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        if(self.length <= 0): return None
        self.length -= 1

        if(self.length == 0):
            self.head = None
            self.tail = None
        
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if(self.length <= 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        if(self.length <= 0): return None
        self.length -= 1

        if(self.length <= 0):
            self.head = None
            self.tail = None

        else:
            temp = self.head
            self.head = self.head.next
            self.prev = None
        return temp

    def get(self, index):
        temp = self.head
        for data in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if(temp): temp.value = value; return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if(index == 0): self.prepend(value); return True
        elif(index == self.length): self.append(value); return True

        # else logic
        temp = self.get(index - 1)
        pre = temp.next; new_node.prev = temp
        new_node.next = pre; temp.next = new_node
        return True

    def remove(self, index):
        if(self.length <= 0): return None
        if(index < 0 or index >= self.length): return None
        
        temp = self.get(index - 1)
        pre = temp; self.length -= 1

        if(self.length <= 0):
            self.head = None
            self.tail = None

        else:
            temp.next = temp.next.next
            temp.prev = pre
        return True

    def getValue(self, node):
        try: return node.value
        except: return None
    
    def nodeValueCheck(self):
        temp = self.head
        for data in range(self.length):
            print(f"{temp.value}, Prev {self.getValue(temp.prev)}, dan Next {self.getValue(temp.next)}")
            temp = temp.next
        # untuk mengecek semua node, terlihat semua prev dan next serta value 

if __name__ == '__main__':
    myDoubly = DoublyLinkedList(10)
    myDoubly.append(18)
    myDoubly.append(10)
    myDoubly.append(2003)
    
    print('Hasil Analisis: ')
    myDoubly.nodeValueCheck()