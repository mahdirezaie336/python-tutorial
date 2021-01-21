from work_place import *


class Mine(WorkPlace):

    def __init__(self, name):
        super(Mine, self).__init__(name)
        self.expertise = 'mine'

    def calc_capacity(self):
        self.capacity = self.level * self.level

    def calc_costs(self):
        return Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
