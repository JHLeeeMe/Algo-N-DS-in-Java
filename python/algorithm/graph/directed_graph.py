from .graph_base import GraphBase


Node = GraphBase.Node


class DirectedGraph(GraphBase):
    def __init__(self, size: int):
        self.__size = size
        self.__nodes = []

    def add_edge(self, _from: int, _to: int):
        if (_from < 0) or (_to < 0) or \
                (self.__size < _from) or (self.__size < _to):
            raise IndexError("")

        n1 = self.node_at(_from)
        n2 = self.node_at(_to)

        if n2 not in n1.adjacent:
            n1.adjacent.append(n2)

    def node_at(self, idx: int) -> Node:
        return self.__nodes[idx]

    @property
    def size(self) -> int:
        return self.__size
