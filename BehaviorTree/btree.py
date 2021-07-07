from BehaviourTree.node import Node


class BehaviourTree(Node):
    def __init__(self, name="Tree"):
        self._name = name
        super().__init__(name)

    def process(self):
        return self._children[self._currentChild].process()

    def print_tree(self, node):
        print(node._name)
        for child in node._children:
            if child._children is not None:
                child.print_tree(child)
