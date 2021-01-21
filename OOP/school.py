from work_place import *


class School(WorkPlace):

    def __init__(self, name):
        super(School, self).__init__(name)
        self.expertise = 'school'

    def calc_capacity(self):
        self.capacity = int(self.level ** 0.5)

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * int(self.level ** 0.5)
