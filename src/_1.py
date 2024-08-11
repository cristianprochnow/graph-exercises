class Graph(object):
    def __init__(self):
        self.size = 10
        self.edges = [
            (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
            (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)
        ]
        self.nodes = self.create_blank()

        self.build_matrix()

    def create_blank(self) -> list[list[int]]:
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def build_matrix(self) -> None:
        for (x, y) in self.edges:
            self.nodes[x - 1][y - 1] = 1
            self.nodes[y - 1][x - 1] = 1

    def count_edges(self) -> int:
        edges_amount = 0

        for row in self.nodes:
            for col in row:
                if col == 1:
                    edges_amount += 1

        return edges_amount


print(Graph().count_edges())
