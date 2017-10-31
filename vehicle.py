class Vehicle(object):
    from Node import *
    from TrafficLight import *
    from window import *

    def __init__(self, node):
        self.current_node = node

    def setPath(self, path):
        self.path = path

    def move(self, current_list, list_to_move):
        if current_list == list_to_move[0]:
            list_to_move[1].append(self)
        else:
            list_to_move[0].append(self)