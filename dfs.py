# Implemantation of Depth First Search

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

color = {}
parent = {}
trav_time = {}
dfs_traversal_output = []

for node in graph_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)

    for v in graph_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

dfs_util("A")
print(dfs_traversal_output)