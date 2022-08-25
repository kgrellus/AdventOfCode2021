from collections import defaultdict
from queue import PriorityQueue
import sys

sys.path.append('../')
from shared import load_inputs


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.edges = defaultdict(lambda: -1)
        self.visited = set()

    def add_edge(self, u, v, weight):
        self.edges[get_key(u, v)] = weight
        # self.edges[u][v] = weight
        # self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.add(current_vertex)

        if len(graph.visited) % (graph.v / 100) == 0:
            print("dijkstra:", len(graph.visited) % graph.v / 100, '%')

        for neighbor in range(graph.v):
            if graph.edges[get_key(current_vertex, neighbor)] != -1:
                distance = graph.edges[get_key(current_vertex, neighbor)]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def prepare_graph(task_input: [[int]]):
    height = len(task_input[0])
    g = Graph(pow(height, 2))
    for i in range(height):
        if i % (height / 100) == 0:
            print("preparing:", i % (height / 100), '%')
        for j in range(height):
            pos = i * height + j
            if j + 1 < height:
                g.add_edge(pos, pos + 1, int(task_input[i][j + 1]))
                g.add_edge(pos + 1, pos, int(task_input[i][j]))
            if i + 1 < height:
                g.add_edge(pos, pos + height, int(task_input[i + 1][j]))
                g.add_edge(pos + height, pos, int(task_input[i][j]))
    return g


def get_key(x: int, y: int) -> str:
    return f'{x},{y}'


def task1(task_input: [str]) -> int:
    g = prepare_graph([[int(val) for val in line] for line in task_input])
    shortest_path = dijkstra(g, 0)
    return shortest_path[g.v - 1]


def task2(task_input: [str]) -> int:
    height = len(task_input)
    the_map = [[0 for _ in range(height * 5)] for _ in range(height * 5)]
    for i in range(height):
        for j in range(height):
            for k in range(5):
                for l in range(5):
                    val = ((int(task_input[i][j]) + k + l - 1) % 9) + 1
                    the_map[height * k + i][height * l + j] = val
    print("map calculating done, len=", pow(len(the_map), 2))
    g = prepare_graph(the_map)
    shortest_path = dijkstra(g, 0)
    return shortest_path[g.v - 1]


def main():
    example_input, puzzle_input = load_inputs(__file__)
    #print(f'task 1: {task1(puzzle_input)}')
    print(f'task 2: {task2(puzzle_input)}')


if __name__ == '__main__':
    main()
