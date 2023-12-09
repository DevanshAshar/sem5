def dfid(graph, current_node, goal_node, visited, path, depth):
    for i in range(1,depth+1):
        path, status = dfs(graph, current_node, goal_node, [], [], 0, i)        
    return path, status
def dfs(graph, current_node, goal_node, visited, path, curr_depth, depth):
    if curr_depth<=depth:
        if current_node not in visited:
            path.append(current_node)
            visited.append(current_node)
            not_visited = [i for i in graph.keys() if i not in visited]
            if current_node == goal_node:
                return path,True            
            for i in graph[current_node]:
                path, status = dfs(graph, i, goal_node, visited, path, curr_depth+1, depth)
                if status == True:
                    return path, True                
        return path,False
    else:
        return path,False
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'X'],
  'D': ['F', 'C'],
  'E': ['G', 'H'],
  'F': [],
  'X': [],
  'G': [],
  'H': [],
}
path1, status =  dfid(graph,'A','G',[],[],3)
if status:
    print(f"Found \npath = {path1}")
else:
    print("not found")
