# Breadth First Search implimantation
from queue import Queue

graph_list = {
    "A":["B","C"],
    "B":["H","E","A"],
    "C":["A","D","F","E"],
    "D":["C"],
    "E":["C","B","G","F"],
    "F":["C","E"],
    "G":["E","H"],
    "H":["G","B"],
}

visited = {}
level = {}
parent = {}
bsf_traversal_output = []
queue = Queue()

for node in graph_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bsf_traversal_output.append(u)
    
    for v in graph_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

print(bsf_traversal_output)