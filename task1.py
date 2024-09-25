class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter_one = -1
        self.length_list = len(self.list_of_list)

    def __iter__(self):
        self.counter_one += 1
        self.counter_two = 0
        return self

    def __next__(self):
        if self.counter_two == len(self.list_of_list[self.counter_one]):
            iter(self)
        if self.counter_one == self.length_list:
            raise StopIteration
        self.counter_two += 1
        return self.list_of_list[self.counter_one][self.counter_two - 1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()