def dfs(graph, visited, src, goal):
    if src not in visited:
        visited.append(src)
        if src == goal:
            exit()
        print(graph[src])
        for i in graph[src]: #points to values of obj like agar src A hai toh ["B", "C"] ko point karega
            dfs(graph, visited, i, goal)
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": [],
}
visited = []
src = input("Enter source node: ")
goal = input("Enter goal node: ")
dfs(graph, visited, src, goal)
