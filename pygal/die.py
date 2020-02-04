from random import randint


# 骰子类
class Die():
    def __init__(self, num_sides=6):
        super().__init__()
        self.num_sides = num_sides

    def roll(self):
        # 返回随机点数
        return randint(1, self.num_sides)
