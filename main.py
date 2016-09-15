class PolyItem:
    """
    class represents one pair of variables and coefficients in polynomial
    """
    def __init__(self, factor: float, power: int):
        assert isinstance(factor, float)
        assert isinstance(power, int)

        self.factor = factor
        self.power = power

    def __eq__(self, other):
        """
        :param other: PolyItem
        :return: bool
        """
        return self.power == other.power

    def __lt__(self, other):
        assert isinstance(other, PolyItem)
        return self.power < other.power

    def __repr__(self, *args, **kwargs):
        return "{}; {}".format(self.factor, self.power)

    def __str__(self):
        return self.__repr__()


class Poly:
    """
    class represents polynomial
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        :param item: PolyItem
        :return: None
        """
        assert isinstance(item, PolyItem)

        # check if already in list of items
        if item in self.items:
            self._add_existing(item)
            return

        self.items.append(item)
        self.items.sort(reverse = True)

    def _add_existing(self, item):
        item_index = self.items.index(item)
        temp_ref = self.items.pop(item_index)
        new_factor = temp_ref.factor + item.factor
        self.items.append(PolyItem(new_factor, item.power))
        self.items.sort(reverse = True)

    def _sort(self):
        self.items.sort(reverse = True)

    def __add__(self, other):
        assert isinstance(other, Poly)

        newPoly = Poly()

        for s_item in self.items:
            newPoly.add_item(s_item)

        for o_item in other.items:
            newPoly.add_item(o_item)

        newPoly._sort()
        return newPoly

    def __str__(self):
        string = "Poly: " + str([''.join(str(item)) for item in self.items])
        return string


i1 = PolyItem(5.5, 3)
p1 = Poly()
p1.add_item(i1)
p1.add_item(i1)
p1.add_item(i1)
i2 = PolyItem(3.5, 3)
i3 = PolyItem(2.2, 4)
p1.add_item(i2)
p1.add_item(i3)
print(p1)

p2 = Poly()

i21 = PolyItem(1.1, 4)
i22 = PolyItem(4.3, 8)

p2.add_item(i21)
p2.add_item(i22)

print(p2)

p3 = p1 + p2
print(p3)
