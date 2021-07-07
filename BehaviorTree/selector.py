from BehaviourTree.node import Node


class Selector(Node):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def process(self):
        child = self._children[self._currentChild].process()

        if child == "RUNNING":
            return "RUNNING"

        if child == "SUCCESS":
            self._currentChild = 0
            return "SUCCESS"

        if self._currentChild > len(self._children):
            self._currentChild = 0
            return "FAILURE"
        self._currentChild += 1
