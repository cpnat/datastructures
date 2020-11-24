import ctypes


class DynamicArray:

    def __init__(self, size=1):

        if size < 1:
            raise ValueError('Array initialisation size must be >= 1')

        self.size = size
        self.items = 0
        self.arr = (self.size * ctypes.py_object)()

    def __len__(self):
        return self.items

    def __str__(self):
        return '[ ' + ', '.join(str(self.arr[x]) for x in range(self.items)) + ' ]'

    def __iter__(self):
        self.num = -1
        return self

    def __next__(self):
        if self.num >= self.items - 1:
            raise StopIteration

        self.num += 1
        return self.arr[self.num]

    def __getitem__(self, item):
        return self.arr[item]

    def __resize(self, new_size):

        temp = (new_size * ctypes.py_object)()

        for i in range(self.items):
            temp[i] = self.arr[i]

        self.arr = temp
        self.size = new_size

    def insert(self, num):

        if self.items + 1 > self.size:
            self.__resize(self.size * 2)

        self.arr[self.items] = num
        self.items += 1

    def index_of(self, num):

        for idx, el in enumerate(self.arr):
            if el == num:
                return idx

        return None

    def delete(self, num):

        position = self.index_of(num)

        if position is None:
            raise ValueError()

        for i in range(position, self.items - 1):
            self.arr[i] = self.arr[i + 1]

        self.items -= 1

        if self.size // 2 > self.items:
            self.__resize(self.size // 2)

    def pop(self):
        pop = self.arr[self.items - 1]
        self.delete(self.items - 1)
        return pop

    def max(self):
        curr_max = 0
        for i in range(self.items):
            curr_max = self.arr[i] if self.arr[i] > curr_max else curr_max

        return curr_max

    def reverse(self):
        for i in range(self.items // 2):
            self.arr[i], self.arr[self.items - 1] = self.arr[self.items - 1], self.arr[i]

    def insert_at(self, idx, num):

        self.insert(self.arr[self.items - 1])
        for i in range(idx, self.items - 2):
            self.arr[i+1] = self.arr[i]

        self.arr[idx] = num

    @staticmethod
    def intersect(arr1, arr2):

        arr1_set = set()
        arr2_set = set()

        intersect = DynamicArray(1)

        for el1 in arr1:
            arr1_set.add(el1)

        for el2 in arr2:
            if el2 in arr1_set and el2 not in arr2_set:
                intersect.insert(el2)
                arr2_set.add(el2)
        return intersect
