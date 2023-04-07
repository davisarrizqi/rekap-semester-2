import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        if(self.adj_list == {}): return False
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
        print(''); return True

    def add_vertex(self, vertex):
        if(vertex not in self.adj_list.keys()):
            self.adj_list[vertex] = []
            return True
        return False
    
    def avoidDuplicateAppend(self, listTarget, value):
        if(value not in listTarget):
            listTarget.append(value)
            return True
        return False

    def add_edges(self, v1, v2):
        if(v1 in self.adj_list.keys() and v2 in self.adj_list.keys()):
            self.avoidDuplicateAppend(self.adj_list[v1], v2)
            self.avoidDuplicateAppend(self.adj_list[v2], v1)
            return True
        return False

    def remove_edges(self, v1, v2):
        if(v1 in self.adj_list.keys() and v2 in self.adj_list.keys()):
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except: pass
            return True
        return False

    def remove_vertex(self, vertex):
        if(vertex in self.adj_list.keys()):
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def isInGraph(self, vertex):
        if(vertex in self.adj_list.keys()): return True
        else: return False # simple dimple constantinople

    def printAllConnected(self, vertex):
        if(self.adj_list == {}): return False
        print(f'Data in {vertex} Vertex --> ', end='')
        for data in self.adj_list[vertex]: 
            print(data, end=', ' if data != self.adj_list[vertex][-1] else '')
        print(''); return True

if __name__ == '__main__':
    # starting grid
    print('\n========= FINAL RESULT =========')
    # variable declaration
    myGraph = Graph()
    listVertex = [21, 76, 44, 18, 52, 27, 82]
    listVertex = [str(data) for data in listVertex]
    for vertex in listVertex: myGraph.add_vertex(vertex)

    # 21 vertex
    myGraph.add_edges(listVertex[0], listVertex[1])
    myGraph.add_edges(listVertex[0], listVertex[2])
    myGraph.add_edges(listVertex[0], listVertex[3])

    # 76 vertex
    myGraph.add_edges(listVertex[1], listVertex[0])
    myGraph.add_edges(listVertex[1], listVertex[2])

    # 44 vertex
    myGraph.add_edges(listVertex[2], listVertex[1])
    myGraph.add_edges(listVertex[2], listVertex[0])
    myGraph.add_edges(listVertex[2], listVertex[3])

    # 18 vertex
    myGraph.add_edges(listVertex[3], listVertex[0])
    myGraph.add_edges(listVertex[3], listVertex[2])
    myGraph.add_edges(listVertex[3], listVertex[4])

    # 52 vertex
    myGraph.add_edges(listVertex[4], listVertex[3])
    myGraph.add_edges(listVertex[4], listVertex[5])

    # 27 vertex
    myGraph.add_edges(listVertex[5], listVertex[4])
    myGraph.add_edges(listVertex[5], listVertex[6])

    # 82 vertex
    myGraph.add_edges(listVertex[6], listVertex[5])
    myGraph.print_graph() # print all of the value

    # show all of the vertex that connected
    myGraph.printAllConnected(listVertex[0])
    
    # check is it contains or not
    print(f'{listVertex[-1]} is Contains' if myGraph.isInGraph(listVertex[-1]) else f'{listVertex[-1]} is not Contains')
    print('================================\n')