import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; # script by davis_arrizqi

class Node:
    def __init__(self, value):
        self.value = value
        self.lower = None
        self.higher = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = None
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.lower
        return True

    def print_from_bottom(self):
        temp = self.bottom
        while temp:
            print(temp.value)
            temp = temp.higher
        return True

    def push(self, value):
        new_node = Node(value)

        if(self.height <= 0):
            self.top = new_node
            self.height = 1
            return True

        new_node.lower = self.top
        self.top = new_node
        self.top.lower.higher = self.top
        self.height += 1

        if(self.height >= 2):
            temp = self.top
            while temp.lower:
                temp = temp.lower
            self.bottom = temp
        return True

    def pop(self):
        if(self.height <= 0): return None
        temp = self.top
        self.top = self.top.lower
        self.height -= 1

        if(self.height < 2):
            self.bottom = None
        return temp

    def sisip_stack(self, index, value):
        new_node = Node(value)
        if(index < 0 or index > self.height): return None
        elif(index == self.height): self.push(value); return True
        elif(index == 0):
            temp = self.top
            while temp.lower:
                pre = temp
                temp = temp.lower
            new_node.higher = temp.lower
            pre.lower.lower = new_node
            self.height += 1
            return True

        if(self.height <= 0):
            self.top = new_node; self.bottom = None
            self.height = 1; return True

        else:
            temp = self.bottom; pre = temp
            for data in range(index):
                pre = temp
                temp = temp.higher
            new_node.higher = temp; temp.lower = new_node
            pre.higher = new_node; temp.lower.lower = pre
            self.height += 1; return True
        return False

if __name__ == '__main__':
    myStack = Stack(2003)
    myStack.push(18); myStack.push(10)
    myStack.sisip_stack(2, 110)
    myStack.print_stack()