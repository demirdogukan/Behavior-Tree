from BehaviourTree.node import Node


class Leaf(Node):
    def __init__(self, name, funct):
        super().__init__()
        self._name = name
        self._funct = funct

    def process(self):
        if self._funct is not None:
            self._funct()

        return "FAILURE"
