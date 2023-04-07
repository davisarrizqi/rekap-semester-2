import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; # script by davis_arrizqi

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
        return True

    def enqueue(self, value):
        new_node = Node(value)
        if(self.length <= 0 or self.first == None):
            self.first = new_node
            self.last = new_node
            self.length = 1
        
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        return True

    def dequeue(self):
        if(self.length <= 0 or self.first == None): return None
        self.length -= 1; temp = self.first

        if(self.length == 0):
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            temp.next = None
        return temp

    def desperation(self, index):
        if(self.length <= 0 or self.first == None): return None
        elif(index < 0 or index >= self.length): return None
        elif(index == self.length-1): self.dequeue(); return True

        temp = self.first; index = self.length - index - 1
        for data in range(index): pre = temp; temp = temp.next
        pre.next = pre.next.next; self.length -= 1; return pre




if __name__ == '__main__':
    myQueue = Queue(1105); myQueue.enqueue(18)
    myQueue.enqueue(10); myQueue.enqueue(2003)
    myQueue.desperation(myQueue.length-1)
    myQueue.print_queue()
