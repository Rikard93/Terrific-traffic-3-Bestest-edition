class Node(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #returnerar posisjonen til noden
    def get_both_positions(self):
        return self.x, self.y

    def get_x_position(self):
        return self.x

    def get_y_position(self):
        return self.y
