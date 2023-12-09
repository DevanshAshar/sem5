def bfs(visited, graph, src, goal):
    visited.append(src)
    queue.append(src)    
    while queue:
        m = queue.pop(0)
        print(m)        
        if m == goal:
            break
        for i in graph[m]:
            if i == " ": 
                continue
            elif i not in visited:
                visited.append(i)
                queue.append(i)
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [" "],
    "E": ["F"],
    "F": [" "],
    "G": [" "],
}
visited = []
queue = []
src = input("Enter source node: ")
goal = input("Enter goal node: ")
bfs(visited, graph, src, goal)
