class level(object):

    def __init__(self):
        self.nodes = []
        self.roads = []
        self.lights = []
        
    def get_roads(self, node):
        if node in self.nodes:
            res = []
            for x in self.roads:
                if x.nodes[0] == node:
                    res.append(x)
            return res



