from Node import *

class TrafficLight (object):

    #Tar to lister, som skal inneholde 2 tall kvar, koordianatane til Node, og ein boolean som forteller om lyset er grønt eller ikkje
    def __init__(self, is_green, possible_roads_green, possible_roads_red, x, y):
      self.node = Node(x, y)
      self.possible_roads_green = possible_roads_green
      self.possible_roads_red = possible_roads_red
      self.is_green = is_green

    #Endrar lysene og returnerar dei vegane som er opne etter lysskiftet

    def change_light(self):
      if self.is_green == False:
        self.is_green = True
        return self.possible_roads_green
      else:
        self.is_green = False
        return self.possible_roads_red

     #returnerar posisisjonen til trafikklyset
    def get_position(self):
        return self.node.get_both_positions()

    def get_x_position(self):
        return self.node.get_x_position()

    def get_y_position(self):
        return self.node.get_y_position()
