def dfs (graph,vertex):
    path = [vertex]
    visit(graph, path,vertex)
    return path

def visit(graph, path, vertex):
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path += [neighbor]
            visit(graph, path, neighbor)



graph1 = {
    'a':['c'], 'b': ['c'], 'c': ['a','b','e'],
    'd':['e','f'], 'e':['c','d','f'], 'f':['d','e','g','h'],
    'g':['f','h'], 'h':['f','g','i','k'], 'i': ['h'], 'k':['h', 'j'], 'j':['k']
}

print(dfs(graph1, 'f'))