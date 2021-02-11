import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}
    dv = {'UP': 0, 'DOWN': 2, 'LEFT': 1, 'RIGHT': 3}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        next_pos = ((self.get_head()[0] + self.dx[self.direction]) % consts.table_size,
                    (self.get_head()[1] + self.dy[self.direction]) % consts.table_size)
        print('head is', self.get_head(), 'next is', next_pos)
        cell = self.game.get_cell(next_pos)
        if (cell.color == consts.back_color) or (cell.color == consts.fruit_color):
            self.cells.append(next_pos)
            if cell.color == consts.back_color:
                self.game.get_cell(self.cells[0]).set_color(consts.back_color)
                del self.cells[0]
            cell.set_color(self.color)
        else:
            self.game.kill(self)

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if self.dv[self.keys[key]] % 2 == self.dv[self.direction] % 2:
                    continue
                self.direction = self.keys[key]
