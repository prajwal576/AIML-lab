from queue import PriorityQueue

# Graph represented as adjacency list
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': [],
    
}

# Heuristic values
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 6,
    'E': 4,
    'F': 0,
    
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    # Add starting node
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, current = pq.get()

        if current in visited:
            continue

        print(current, end=" ")

        visited.add(current)

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("\nGoal not found!")

# Driver code
best_first_search('A', 'F')
