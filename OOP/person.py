import math


class Consts:
    MIN_AGE = 18
    AGE_MUL = 15
    BASE_PRICE = {'teacher': 100, 'worker': 110, 'engineer': 500}
    BASE_COST = {'teacher': 100, 'worker': 110, 'engineer': 500}
    BASE_INCOME = {'teacher': {'mine': 1, 'school': 1, 'company': 2},
                   'worker': {'mine': 1, 'school': 1, 'company': 2},
                   'engineer': {'mine': 1, 'school': 1, 'company': 2}}


class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.job = ''
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        return self.do_level(self.calc_income()) - self.calc_life_cost()

    @staticmethod
    def calc_all():
        summation = 0
        for i in Person.instances:
            summation += i.calc()
        return summation

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1
