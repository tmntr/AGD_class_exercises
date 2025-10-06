import math

class test_coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def test_distance(self):
        assert False

testvalues = (((0,0),(0,0),0),
            ((10,0),(0,0),10),
            ((1,1),(0,0),math.sqrt(2)),
            ((0,0),(0,0),0),
            ((0,0),(0,0),0),
            ((0,0),(0,0),0),
            ((0,0),(0,0),0),
              )