from collections import defaultdict


class GraphBFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        q = list()
        q.append(start)
        visited[start] = True

        while q:
            tmp = q.pop(0)
            print("{} -> ".format(tmp), end=" ")

            for i in self.graph[tmp]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = GraphBFS()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.bfs(2)