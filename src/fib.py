from itertools import takewhile


class Fibi():
    x = 0
    y = 1
    z = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.z = self.x + self.y
        self.x = self.y
        self.y = self.z
        return self.x


fibionaci = Fibi()

res = filter(lambda x: x % 2 == 0, takewhile(lambda x: x < 4000000, Fibi()))
# res = filter(lambda x: True, takewhile(lambda x: x < 4000000, Fibi()))
print(list(res))
