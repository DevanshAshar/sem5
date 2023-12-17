adjacent_list = {
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('S', 6), ('E', 6)],
    'B': [('S', 5), ('D', 7), ('E', 6)],
    'C': [('S', 10), ('D', 6)],
    'D': [('B', 7), ('C', 6), ('F', 6)],
    'E': [('A', 6), ('B', 6), ('F', 4)],
    'F': [('E', 4), ('D', 6), ('G', 3)],
    'G': [('F', 3)],
}
heuristic = {'S': 17, 'A': 10, 'B': 13, 'C': 4, 'D': 2, 'E': 4, 'F': 1, 'G': 0}
def astar(start, destination):
    closed, opened, distance, parent = [], [start], {start: 0}, {start: start}    
    while opened:
        v = min(opened, key=lambda x: distance[x] + heuristic[x]) #sabse paas wala find karo start se
        if v == destination:
            path = [v]
            while parent[v] != v:
                path.append(parent[v])
                v = parent[v]
            path.reverse()
            print(f"Shortest path found, path: {path}\nDistance: {distance[destination]}")
            return
        for (i,j) in adjacent_list[v]:
            if i not in closed and i not in opened: # i is not visited
                opened.append(i) 
                distance[i]=j+distance[v]
                parent[i]=v
            else:    
                if j+distance[v]<distance[i]: # agar aur optimized milta hai toh
                    distance[i] = j+distance[v]
                    parent[i]=v
                    if i in closed: # optimized mila toh closed se nikaal do and open mein daalo for exploring 
                        closed.remove(i)
                        opened.append(i)
        opened.remove(v)
        closed.append(v)
        print(f"Open List: {opened}\nClosed List: {closed}")
    print(f"No path found from source {start} to destination {destination}")
astar('S', 'G')
