graph = {
'5': ['3', '8'],
'3': ['2', '4'],
'9': ['7'],
'2': [],
'4': [],
'7': [],
}
visited = set()  
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
    for neighbor in graph[node]:
        dfs(visited, graph, neighbor)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')