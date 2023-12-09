# Define the graph
graph = {
    'S': {'A': 5, 'B': 8, 'C': 12},
    'A': {'D': 6, 'E': 9},
    'B': {'F': 10},
    'C': {'G': 11},
    'D': {'H': 8, 'I': 15},
    'E': {'J': 7},
    'F': {'K': 12},
    'G': {'L': 9},
    'H': {'M': 10},
    'I': {'N': 5},
    'J': {'N': 8},
    'K': {'N': 6},
    'L': {'N': 10},
    'M': {'N': 7},
    'N': {'Z': 0},
    'Z': {}
}
# Define the heuristic values for A* search
graph_heu = {
    'S': 20,
    'A': 16,
    'B': 18,
    'C': 15,
    'D': 12,
    'E': 10,
    'F': 8,
    'G': 6,
    'H': 6,
    'I': 5,
    'J': 4,
    'K': 3,
    'L': 2,
    'M': 1,
    'N': 0,
    'Z': 0
}
curr_node = input("Enter Start Node : ") # this is also start node at the beginning
goal_node = input("Enter Goal Node : ")
def funcofn(gl,cn): # gl <- path of previous node , cn <- current node
    g =0
    print(gl,cn) 
    for i in range(len(gl)-1):
        g += graph[gl[i]][gl[i+1]]
    g += graph[gl[-1]][cn] + graph_heu[cn] #graph['S']['A'] isme pehle graph['S'] execute hoga fir voh key se A ka value milega i.e. 5
    return g
open_list = []    
close_list = []
open_list.append([curr_node,graph_heu[curr_node],[curr_node]])
try:
    while True:
        parent_node = open_list[0][0]
        # print(parent_node)
        close_list.append(parent_node)
        print(open_list)
        current_path = open_list[0][2]
        if parent_node == goal_node:
            break
        print(f"Currently at node : {parent_node}")
        for j in graph[open_list[0][0]]:
            open_list.append([j,funcofn(current_path,j),current_path+[j]])
            open_list = sorted(open_list, key=lambda x: x[1])
        # open_list = [pair for pair in open_list if pair[0] != parent_node]
        # before:[['S', 20, ['S']], ['A', 21, ['S', 'A']], ['B', 26, ['S', 'B']], ['C', 27, ['S', 'C']]]
        #basically ye loop se parent hata diya open list se taaki next iteration mein S ki jagah A lenge as parent
        for i in open_list:
            if i[0] == parent_node:
                open_list.remove(i)
        # after:[['A', 21, ['S', 'A']], ['B', 26, ['S', 'B']], ['C', 27, ['S', 'C']]]  
        print(f"Open List is : {open_list}\nclosed List is : {close_list}\n")
except:
    print("something went wrong moslty the node not found : ( ")        
print(f"So the optimized path is from {open_list[0][2][0]} to {goal_node} is {open_list[0][2]} with distance : {open_list[0][1]}")      
