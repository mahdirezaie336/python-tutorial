from work_place import *


class Company(WorkPlace):

    def __init__(self, name):
        super(Company, self).__init__(name)
        self.expertise = 'company'

    def calc_capacity(self):
        self.capacity = self.level

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * self.level
