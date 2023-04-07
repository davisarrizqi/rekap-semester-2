import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

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
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
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
    
    # show dfs pre order result
    print('\nHasil Metode Pre Order DFS')
    print('=============================')
    print(my_tree.dfs_pre_order())
    print('=============================')

    # show dfs in order result
    print('\nHasil Metode In Order DFS')
    print('=============================')
    print(my_tree.dfs_in_order())
    print('=============================')
    
    # show dfs post order result
    print('\nHasil Metode Post Order DFS')
    print('=============================')
    print(my_tree.dfs_post_order())
    print('=============================')

    # show the parent of the value that chosen
    print('\n======== Here We Are ========')
    value = 82 #--> you can change this value
    isTrue, result = my_tree.find_my_parent(value)
    if(isTrue): print(f'Ditemukan!, Parent dari {value} adalah {result}')
    else: print(f'Parent dari {value} tidak ditemukan!')
    print('=============================\n')