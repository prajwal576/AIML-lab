from queue import PriorityQueue

def bfs(graph, start, target, heuristics):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start]))
    visited.add(start)

    while not pq.empty():
        h, node, path = pq.get()

        if node == target:
            return path, h
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                pq.put((heuristics[neighbor], neighbor, path + [neighbor]))

    return None, None
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    heuristics = {
        'A': 10, 
        'B': 8,
        'C': 5,
        'D': 6,
        'E': 4,
        'F': 0
    }

    path, cost = bfs(graph, 'A', 'F', heuristics)
    print(f"Path found by BFS: {path} with Target Heuristic: {cost}")