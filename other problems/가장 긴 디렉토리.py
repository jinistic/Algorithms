def dfs(node, temp):
    temp += "/" + dirnames[node]
    if not graph[node]:
        directory.append(temp)
    else:
        for i in graph[node]:
            dfs(i, temp)
    

def solution(N, relation, dirname):
    """[summary]

    Args:
        N ([type]): [description]
        relation ([type]): [description]
        dirname ([type]): [description]

    Returns:
        [type]: [description]
    """    
    global dirnames, graph, directory
    dirnames = [0] + dirname
    graph = [[] for _ in range(N + 1)]
    for i in relation:
        graph[i[0]].append(i[1])

    directory = []
    dfs(1, "")
    print(graph)
    print(directory)
    return max(map(len, directory)) - 1


print(solution(8, [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [4, 7], [7, 8]], \
["root", "circle", "triangle", "square", "red", "orange", "blue", "yellow"]))