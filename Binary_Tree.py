# First input: Number of runs
# Second input: Number of nodes in the tree
# Edge 1: Parent node 1 connected to child node 2
# Edge 2: Parent node 1 connected to child node 3
# Edge 3: Parent node 3 connected to child node 4

class Parser:
    def readfromConsole(self):

        n = int(input(''))
        tree = Tree()
        for i in range(n-1):
            parent,child = input().split()
            parent,child = int(parent), int(child)
            tree.add(parent,child)

        return tree

class Tree:
    def __init__(self):
        self.__root = Vertex(1)

    def get_root(self):
        return self.__root

    def search(self,u):
        if self.__current.get_index() == u:
            return self.__current
        for vertex in self.__current.get_children():
            self.__current = vertex
            result = self.search(u)

            if isinstance(result,Vertex) and result.get_index()== u:
                return result
    def add(self,u,v):
        self.__current = self.__root
        to_add_to = self.search(u)
        to_add_to.add_child(v)


class Vertex:
    def __init__(self,index):
        self.__index = index
        self.__children = []

    def get_index(self):
        return self.__index

    def get_children(self):
        return self.__children

    def calculate_point(self):
        total = self.calculate_Num_Vertices()
        for vertex in self.__children:
            total += vertex.calculate_point()
        return total
    def calculate_Num_Vertices(self):
        total = 1

        for vertex in self.__children:
            total += vertex.calculate_Num_Vertices()
        return total

    def add_child(self,v):
        self.__children.append(Vertex(v))

num_runs = int(input(""))
for i in range(num_runs):
    print(Parser().readfromConsole().get_root().calculate_point())
