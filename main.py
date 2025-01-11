import json
import tracemalloc
import heapq
import argparse
import math


def calc_heuristic(node, goal):
    cur_x, cur_y = node.split("_")
    goal_x, goal_y = goal.split("_")
    x_dist = ord(goal_x) - ord(cur_x)
    y_dist = int(goal_y) - int(cur_y)

    return math.sqrt(
        abs(x_dist) + abs(y_dist)
        )

def set_default_scores(graph):
    return {node: float('inf') for node in graph}

def a_star(graph, start, goal):
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
            current_score = scores[current_node] + int(cost)

            if current_score < scores[neighbor]:
                came_from[neighbor] = current_node
                scores[neighbor] = current_score
                total_score = current_score + calc_heuristic(neighbor, goal)
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
    parser.add_argument('start')
    parser.add_argument('goal')
    args = parser.parse_args()
    graph = get_graph_data(args.filename)
    tracemalloc.start()
    path, cost = a_star(graph, args.start, args.goal)
    print(len(graph), tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print(f"Najkrótsza ścieżka: {path} z kosztem: {cost}")

