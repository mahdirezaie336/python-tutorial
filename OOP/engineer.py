from person import Person, Consts


class Engineer(Person):

    def __init__(self, name, age):
        super(Engineer, self).__init__(name, age)
        self.job = 'engineer'

    def get_price(self):
        return int(Consts.BASE_PRICE[self.job] * (Consts.MIN_AGE / self.age) ** 0.5)

    def calc_life_cost(self):
        return int(Consts.BASE_COST[self.job] * (self.age / Consts.MIN_AGE) ** 0.5)

    def calc_income(self):
        return int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * (Consts.MIN_AGE / self.age) ** 0.5)
