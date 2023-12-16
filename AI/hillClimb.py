graph = [
    [5, 12, 8, 3, 19, 25, 10, 7],
    [15, 22, 18, 13, 29, 35, 20, 17],
    [25, 32, 34, 23, 39, 45, 30, 27],
    [35, 42, 38, 33, 49, 55, 40, 37],
    [45, 52, 48, 43, 59, 65, 50, 47],
    [55, 62, 58, 53, 69, 75, 60, 57],
    [65, 72, 68, 63, 79, 85, 70, 67],
    [75, 82, 78, 73, 89, 95, 80, 77]
]
state = [0, 0] 
max_val = float('-inf') 
while True:
    old_val = max_val
    x = state[0]
    y = state[1]
    possible_moves = [[x+1, y], [x-1, y], [x+1, y+1],[x-1, y-1], [x+1, y-1], [x-1, y+1], [x, y-1], [x, y+1]]
    for x1, y1 in possible_moves:
        if 0 <= x1 < 8 and 0 <= y1 < 8:
            val = (graph[x1][y1])
            if val > max_val:
                print(val)
                max_val = val 
                state = [x1, y1]
    if old_val == max_val:
        print(state)
        break
print(f"Max Value is {max_val} at state {state}")
