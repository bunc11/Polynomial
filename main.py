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
        print("called __eq__")
        return self.power == other.power

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
            item_index = self.items.index(item)
            item_ref = self.items[item_index]
            new_factor = item_ref.factor + item.factor
            item_ref.factor = new_factor
            return

        self.items.append(item)

    def __str__(self):
        string = "Poly: " + str([''.join(str(item)) for item in self.items])
        return string


# result should be 16.5
i1 = PolyItem(5.5, 3)
p1 = Poly()
p1.add_item(i1)
p1.add_item(i1)
p1.add_item(i1)
print(p1)  # gives wrong result cos we are operating on item itself
