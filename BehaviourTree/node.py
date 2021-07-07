class Node:
    def __init__(self, name):
        self._children = list()
        self._currentChild = 0
        self._name = name
        self._status = None

    def add_child(self, child):
        self._children.append(child)
