class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end):
        self.add_node(start)
        self.add_node(end)
        self.graph[start].append(end)
        self.graph[end].append(start)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                result.append(current_node)
                visited.add(current_node)
                queue.extend(self.graph[current_node])
        return result

    # def show_graph(self):
    #     for node in self.graph:
    #         print(f"{node}: {', '.join(map(str, self.graph[node]))}")


def operation(p_graph, p_n, p_k):
    for node in range(1, p_n + 1):
        neighbors = p_graph.graph[node]
        if len(neighbors) >= 2:  # Check whether the current node has neighbors more than or equal to 2
            for main_neighbor in neighbors:  # main neighbor is the current neighbor that is being checked
                for sub_neighbor in neighbors:
                    if (main_neighbor != sub_neighbor) and ((main_neighbor == sub_neighbor * p_k) or (sub_neighbor == main_neighbor * p_k)):
                        p_graph.add_edge(main_neighbor, sub_neighbor)
                        # p_graph.add_edge(sub_neighbor, main_neighbor)

    for node in range(1, p_n + 1):
        p_graph.graph[node].sort()

    return p_graph


def main():
    # Begin to build graph
    graph = Graph()
    n, m, k, s = map(int, input().split())
    for i in range(m):
        start, end = map(int, input().split())
        graph.add_edge(start, end)
    # Complete building graph
    operation(graph, n, k)
    ans = graph.bfs(s)
    for i in ans:
        print(i, end=' ')
    # print('-------------------------')
    # test = graph.show_graph()
    # print(test)


main()
