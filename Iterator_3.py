class FlatIterator:

    def __init__(self, list_of_list):
        self.array = self.unpack(list_of_list)
        
    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor > len(self.array):
            raise StopIteration
        return self.array[self.cursor - 1]
    
    def unpack(self, list_of_list):
        new_array = list_of_list
        ind = 0
        while True:
            try:
                while isinstance(new_array[ind], list):
                    item = new_array.pop(ind)
                    for inner_item in reversed(item):
                        new_array.insert(ind, inner_item)
                ind += 1
            except IndexError:
                break
        return new_array

    
def test():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test()