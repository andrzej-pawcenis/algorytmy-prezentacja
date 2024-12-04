import json
import tracemalloc
import heapq
import argparse

def heuristic(node):
    return {'A': 7, 'B': 6, 'C': 2, 'D': 0, 'E': 1, 'F': 2}[node]

def set_default_scores(graph):
    return {node: float('inf') for node in graph}

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    scores = set_default_scores(graph)
    
    scores[start] = 0
    came_from = {}

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            
            return path, scores[goal]

        for neighbor, cost in graph[current_node]:
            tentative_score = scores[current_node] + cost

            if tentative_score < scores[neighbor]:
                came_from[neighbor] = current_node
                scores[neighbor] = tentative_score
                total_score = tentative_score + heuristic(neighbor)
                heapq.heappush(open_set, (total_score, neighbor))

    return None, float('inf')


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path


def get_graph_data(filename):
    with open(filename, "r") as _file:
        return json.load(_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    graph = get_graph_data(args.filename)
    tracemalloc.start()
    path, cost = a_star(graph, 'A', 'D', heuristic)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    print(f"Najkrótsza ścieżka: {path} z kosztem: {cost}")

