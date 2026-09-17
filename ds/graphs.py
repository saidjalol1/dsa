"""
A Graph is non-linear data-struture , 
it is a set of nodes or we can call them vertices which are connected by edges 


Key Terminologies:
    1) Nodes / Vertices : A fundamental unit representing an entity (city , people , etc)
    2) Edge : connection between verticies , which can be directed or undirected
        directed means one way connection between two vertices , undirected is two way connection 
    3) Weighted / Unweighted : this termins belongs to the edges , edges can be weighted which means they can have values 
        likes distenace between vertices (cities , servers ), if they do not have values which means they are unweighted 
        

There are two ways to represent graphs:
    1) Adjecency lists
    2) matrix
    
    
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

adjacency_matrix = [
    # Node 0 connects to node 1, but not itself or node 2
    [0, 1, 0],
    
    # Node 1 connects to both node 0 and node 2
    [1, 0, 1],
    
    # Node 2 connects to node 1, but not itself or node 0
    [0, 1, 0]
]