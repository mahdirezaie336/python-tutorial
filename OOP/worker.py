from person import Person, Consts


class Worker(Person):

    def __init__(self, name, age):
        super(Worker, self).__init__(name, age)
        self.job = 'worker'

    def get_price(self):
        return int(Consts.BASE_PRICE[self.job] * Consts.MIN_AGE / self.age)

    def calc_life_cost(self):
        return int(Consts.BASE_COST[self.job] / Consts.MIN_AGE * self.age)

    def calc_income(self):
        return int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age)
