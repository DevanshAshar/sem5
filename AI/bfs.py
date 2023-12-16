def bfs(graph, src,goal,visited):
    visited.append(src)
    queue.append(src)
    not_visited = [i for i in graph.keys() if i not in visited]   
    print(f"{visited}\t\t{not_visited}\t\tFalse") 
    while queue:
        m = queue.pop(0)     
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                not_visited = [i for i in graph.keys() if i not in visited]
                if goal in visited:
                    print(f"{visited}\t\t{not_visited}\t\tTrue")                
                    exit()
                else:
                    print(f"{visited}\t\t{not_visited}\t\tFalse")
graph = {
  'A': ['B','C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}
queue = []
src = input("Enter source node: ")
goal = input("Enter goal node: ")
bfs(graph, src, goal,visited=[])
