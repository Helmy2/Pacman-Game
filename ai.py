class AI:
    def __init__(self, graph, dots, start, goal):
        self.graph, self.dots = graph, dots
        self.start, self.goal = start, goal

    def path_cost(self, path):
        g_cost = 0
        h_cost = 0
        for i in range(0, len(path)):
            h_cost += self.get_h_cost(path[i])
        g_cost += self.get_g_cost( path[-1])
        return g_cost + h_cost

    def escape(self):
        queue = [[self.start]]
        visited = []

        while queue:
            queue.sort(key=self.path_cost)
            path = queue.pop(0)
            node = path[-1]

            if node in visited:
                continue
            visited.append(node)

            if node in self.dots:
                return path
            else:
                for neighbor in self.neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    def get_g_cost(self, node):
        return -((abs(self.goal[1] - node[1])) + (abs(self.goal[0] - node[0])))

    def get_h_cost(self, node):
        if node not in self.dots:
            return .3
        else:
            return 0

    def neighbors(self, index):
        (x, y) = index
        neighbor_list = []
        if x > 0 and self.graph[x - 1][y] != 0:
            neighbor_list.append((x - 1, y))

        if y > 0 and self.graph[x][y - 1] != 0:
            neighbor_list.append((x, y - 1))

        if x < len(self.graph) - 1 and self.graph[x + 1][y] != 0:
            neighbor_list.append((x + 1, y))

        if y < len(self.graph[0]) - 1 and self.graph[x][y + 1] != 0:
            neighbor_list.append((x, y + 1))

        return neighbor_list

    def follow(self):
        queue = [[self.start]]
        visited = []

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node in visited:
                continue
            visited.append(node)

            if node == self.goal:
                return path
            else:
                for neighbor in self.neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)