import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.value = value
        self.right = right

class Queue:
    def __init__(self, value, left=None, right=None):
        new_node = Node(value, left=left, right=right)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def clear_queue(self):
        temp = self.first
        self.first = None
        self.last = None
        self.length = 0
        return temp

    def enqueue(self, value, left=None, right=None):
        if(self.length <= 0):
            self.__init__(value, left=left, right=right); return True
        new_node = Node(value)
        self.last.right = new_node
        self.last = new_node
        self.length += 1
        return True

    def dequeue(self, index=-1):
        if(self.length <= 0): return None
        elif(self.length == 1): return self.clear_queue()

        if(index == -1):
            temp = self.first; pre = temp
            while temp.right:
                pre = temp
                temp = temp.right
            pre.right = None
            self.last = pre

        elif(index == 0):
            temp = self.first
            self.first = self.first.right

        self.length -= 1; return temp

    def print_queue(self):
        if(self.length <= 0): return False
        temp = self.first

        while temp:
            print(temp.value)
            temp = temp.right
        return True

    def to_list(self):
        self.result = []; temp = self.first
        while temp:
            self.result.append(temp.value)
            temp = temp.right
        return self.result

    def get_value(self, node, side=None):
        if(side == 'left'):
            try: return node.left.left.value
            except: return node.left

        elif(side == 'right'):
            try: return node.right.right.value
            except: return node.right

        else:
            try: return node.value
            except: return node

    def get_node(self, node, side=None):
        if(side == 'left'):
            try: return node.left
            except: return None

        elif(side == 'right'):
            try: return node.right
            except: return None

        else:
            return node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node = self.root
        queue = Queue(
            current_node.value, 
            left=current_node.left.value, 
            right=current_node.right.value
        ); results = Queue(18)

        while queue.length > 0:
            print('ping')
            current_node = queue.dequeue(0)
            
            results.enqueue(
                queue.get_value(current_node), 
                left=queue.get_value(current_node, side='left'), 
                right=queue.get_value(current_node, side='right')
            )
            
            if current_node.left is not None:
                queue.enqueue(
                    queue.get_value(current_node.left), 
                    left=queue.get_value(current_node, side='left'), 
                    right=queue.get_value(current_node, side='right')
                )
            
            if current_node.right is not None:
                queue.enqueue(
                    queue.get_value(current_node.right), 
                    left=queue.get_value(current_node, side='left'), 
                    right=queue.get_value(current_node, side='right')
                )
            
        results.dequeue(0); results = results.to_list() 
        return results

    def dfs_pre_order(self):
        results = []; parents = {}

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            
            return True
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return results

    def find_my_parent(self, value):
        parents = {}
        def collect_data(temp, parent):
            # bug fixed - the right side of root is uncountable
            if(temp != self.root):
                parents[temp.value] = parent.value
            cache = temp; cacheParent = parent
            
            if(temp.left != None):
                parent = temp; temp = temp.left
                collect_data(temp, parent)

            if(cache.right != None):
                cacheParent = cache; cache = cache.right
                collect_data(cache, cacheParent)
        collect_data(self.root, self.root)
        
        try:
            result = parents[value]
            return True, result

        except:
            return False, None
    
if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    # show bfs result
    print('Hasil Metode BFS')
    print('=============================')
    print(my_tree.BFS())
    print('=============================')

    