from BehaviourTree.btree import BehaviourTree
from BehaviourTree.leaf import Leaf
from BehaviourTree.selector import Selector
from BehaviourTree.sequence import Sequence


# ------------------------------------------------------------------------------------
# Name: Implementation of BTree
# Description:
#                                Behaviour Tree(Root)
#                                /           \
#                      STEAL(Sequence)      Open Door(Selector)
#
# hasMoney, openDoor, escape, sell diamond(Leaf) GotofrontDoor, Gobacktodoor(Leaf)
#
# TODO
# Functions will be defined later on.
# -------------------------------------------------------------------------------------


def has_money():
    pass


def escape():
    pass


def sell_diamond():
    pass


def go_to_front_door():
    pass


def go_to_back_door():
    pass


def go_to_diamond():
    pass


if __name__ == "__main__":
    # Root
    tree = BehaviourTree()
    steal = Sequence("Steal Something")
    hasMoney = Leaf("Has Money", has_money)
    openDoor = Selector("Open Door")
    escp = Leaf("Go To Van", escape)
    sellDiamond = Leaf("Sell Diamond", sell_diamond)
    goToFrontDoor = Leaf("Go To Front Door", go_to_front_door)
    goToBackDoor = Leaf("Go To Back door", go_to_back_door)
    goToDiamond = Leaf("Go To Diamond", go_to_diamond)

