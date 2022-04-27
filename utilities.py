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
