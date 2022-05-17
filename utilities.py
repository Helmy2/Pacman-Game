GAME_SPEED = 10
TILE_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 2, 245)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
TILES = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

WIDTH = TILE_SIZE * len(TILES[0])
HEIGHT = TILE_SIZE * len(TILES)


def neighbors(graph, index):
    (x, y) = index
    neighbor_list = []
    if x > 0 and graph[x - 1][y] != 0:
        neighbor_list.append((x - 1, y))

    if y > 0 and graph[x][y - 1] != 0:
        neighbor_list.append((x, y - 1))

    if x < len(graph) - 1 and graph[x + 1][y] != 0:
        neighbor_list.append((x + 1, y))

    if y < len(graph[0]) - 1 and graph[x][y + 1] != 0:
        neighbor_list.append((x, y + 1))

    return neighbor_list


def bfs(graph, start, goal):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return path
        else:
            for neighbor in neighbors(graph, node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)


def get_g_cost(start, node):
    return -((abs(start[1] - node[1])) + (abs(start[0] - node[0])))


def get_h_cost(dots, node):
    if node not in dots:
        return 5
    else:
        return 0


# def get_h_cost(dots, node):
#     total_x = 0
#     total_y = 0
#     for (x, y) in dots:
#         total_x += node[0] - x
#         total_y += node[1] - y
#     return (total_y + total_x) * .1


class AI:
    def __init__(self, graph, dots, start, goal):
        self.graph, self.dots = graph, dots
        self.start, self.goal = start, goal

    def path_cost(self, path):
        g_cost = 0
        h_cost = 0
        for i in range(0, len(path)):
            g_cost += get_g_cost(self.goal, path[i])
            h_cost += get_h_cost(self.dots, path[i])
        print(g_cost, " ", h_cost)
        return g_cost + h_cost

    def bfs_escape(self):
        queue = [[self.start]]
        visited = []

        while queue:
            queue.sort(key=self.path_cost)
            path = queue.pop(0)
            node = path[-1]

            if node in visited:
                continue
            visited.append(node)

            if node == self.goal:
                return path
            else:
                for neighbor in neighbors(self.graph, node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
