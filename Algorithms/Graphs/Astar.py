def Astar(graph, start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()
        if current == end:
            path = []

        while current in came_from:
            path.append(current)
            current = came_from[current]
        
            return path[::-1]
    
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + distance_between(current, neighbor)  
            
            if tentative_g_score < g_score[neighbor]:
                