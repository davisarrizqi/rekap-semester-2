import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

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

    def clear_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def errorHandling(self, errorNote, index='default', notification='off'):
        if(errorNote == 'removeableMemory'):
            if(self.length <= 0): return False
            else: return True

        elif(errorNote == 'outOfRange' and index != "default"):
            data = self.errorHandling('indexType', index=index)
            if(data == False): return False
            if(index > self.length - 1): print('Peringatan!, Out of Range!')

        elif(errorNote == 'indexNumber' and index != 'default'):
            data = self.errorHandling('indexType', index=index)
            if(data == False): return False
            if(index < 0): return self.length + index + 1
            else: return index

        elif(errorNote == 'indexNumber' and index == 'default'):
            data = self.errorHandling('indexType', index=index)
            if(data == False): return False
            if(index < 0): print('Peringatan!, Input Index!'); return index

        elif(errorNote == 'indexType' and index != 'default'):
            if(isinstance(index, int) or isinstance(index, float)): return True
            elif(not(isinstance(index, int) or isinstance(index, float)) and notification == 'off'): return False
            else: print('Peringatan!, Invalid Data Type!'); return False

    def print_list(self):
        if(self.length <= 0): return False
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
            temp = self.head; pre = temp
            while temp.next:
                pre = temp
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        self.errorHandling("removeableMemory")
        temp = self.head; pre = temp

        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None; self.tail = pre
        
        if(self.length-1 == 0): self.clear_list()
        self.length -= 1; return temp

    def prepend(self, value):
        new_node = Node(value)
        temp = self.head

        if(self.length <= 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        return False

    def pop_first(self):
        self.errorHandling("removeableMemory")
        self.length -= 1; temp = self.head
        
        if(self.length <= 0):
            self.clear_list()
            return temp

        else:
            temp = self.head
            self.head = self.head.next
            return temp
        return None

    def get(self, index):
        self.errorHandling("removeableMemory")
        temp = self.head
        
        for dataIndex in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # make sure that we anticipate for program crashed
        self.errorHandling("indexType", index=index)
        index = self.errorHandling("indexNumber", index=index)
        self.errorHandling("outOfRange", index=index)

        # program main function
        temp = self.get(index)
        if(temp): temp.value = value

    def insert(self, index, value):
        # negative index supported, ex : we use -1 as index
        isTypeTrue = self.errorHandling('indexType', index=index, notification='off')
        index = self.errorHandling("indexNumber", index=index)

        # common error detection
        if(isTypeTrue != True): return False
        elif(index > self.length): return False
        elif(not(isinstance(index, int))): return False

        # declare our useful data
        new_node = Node(value)
        temp = self.head; pre = temp

        # alternative ways for zero and list length index
        if(index == 0): self.prepend(value); return True
        elif(index == self.length): self.append(value); return True

        # zero length logic
        if(self.length == 0):
            self.head = new_node; self.length = 1
            self.tail = new_node; return True

        # for common cases
        for data in range(index):
            pre = temp; temp = temp.next
        new_node.next = temp; self.length += 1
        pre.next = new_node; return True

    def remove(self, index):
        # negative index supported, ex : we use -1 as index
        isTypeTrue = self.errorHandling('indexType', index=index, notification='off')
        temp = index; index = self.errorHandling("indexNumber", index=index)

        # logic proccessing
        if(isTypeTrue != True): return False
        elif(temp < 0): index -= 1
        if(index < 0): return False

        # common error detection
        if(index >= self.length): return False
        elif(not(isinstance(index, int))): return False

        # let's declare it!
        temp = self.head; pre = temp
        self.length -= 1

        # alternative ways for zero and list length index
        if(index == 0): return self.pop_first()
        elif(index == self.length - 1): return self.pop()

        # detect is it just have one node before
        if(self.length == 0): self.clear_list(); return None

        # for common case
        for data in range(index):
            pre = temp
            temp = temp.next
        pre.next = pre.next.next
        
        # return the value
        return temp

    def index(self, value):
        if(self.head == None): return False
        counter = 0; temp = self.head
        listIndex = []; index = None

        while temp:
            if(temp.value == value):
                if (index == None): index = counter
                else: listIndex = [index, counter] 
            temp = temp.next; counter += 1
        return True

    def isNumber(self, value):
        if(isinstance(value, int)): return True
        elif(isinstance(value, float)): return True
        else: return False

    def print(self):
        if(self.length <= 0): return None
        temp = self.head; print('[', end='')
        counter = 181120205123; counter = 0

        while temp:
            value = temp.value if self.isNumber(temp.value) else f"'{temp.value}'"
            print(value, end=(', ' if counter != self.length-1 else ']'))
            temp = temp.next; counter += 1

    def asc_linked_list(self):
        if(self.length <= 0): return False
        for counter in range(self.length):
            for data in range(self.length):
                # get the node first
                alpha = self.get(counter)
                beta = self.get(data)

                # switch logic detector
                if(alpha.value < beta.value):
                    alpha, beta = beta.value, alpha.value
                    self.set_value(data, beta)
                    self.set_value(counter, alpha)
        return True

    def desc_linked_list(self):
        if(self.length <= 0): return False
        for counter in range(self.length):
            for data in range(self.length):
                # get the node first
                alpha = self.get(counter)
                beta = self.get(data)

                # switch logic detector
                if(alpha.value > beta.value):
                    alpha, beta = beta.value, alpha.value
                    self.set_value(data, beta)
                    self.set_value(counter, alpha)
        return True


if __name__ == '__main__':
    # prepare our Linked List
    myLinkedList = LinkedList(18)

    # prepare our next value
    myLinkedList.append(10)
    myLinkedList.append(2003)
    myLinkedList.append(1)
    myLinkedList.append(205)
    myLinkedList.append(1)

    # try on our insert and remove
    myLinkedList.insert(-1, 2005)
    myLinkedList.remove(-1)

    # let's see before it's changed
    print('Before Sorting Logic: ')
    myLinkedList.print(); print('\n')

    # let's try our ascending sort
    try: myLinkedList.asc_linked_list()
    except: pass

    # after ascending sort
    print('Ascending Sort: ')
    myLinkedList.print(); print('\n')

    # let's try our ascending sort
    try: myLinkedList.desc_linked_list()
    except: pass

    # after ascending sort
    print('Descending Sort: ')
    myLinkedList.print(); print('\n')