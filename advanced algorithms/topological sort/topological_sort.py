visited = list()
stack = list()
def custom_sort(gf):
    for key in gf.keys():
        print(key)
        if key in visited:
            print(key)
            continue
        else:
            topo_sort(key, gf)

def topo_sort(v, gf):
    print(v, gf)
    visited.append(v)
    for child in gf[v]:
        if child not in visited:
            topo_sort(child, gf)
    stack.append(v)
    return


if __name__ == "__main__":
    gf = {
        "A": ["C"],
        "B": ["C","E"],
        "C": ["D"],
        "D": ["F"],
        "E": ["F"],
        "F": ["G"],
        "G": []
    }
    custom_sort(gf)
    print(stack)
    for i in range(0,len(stack)):
        print(stack.pop())
            

