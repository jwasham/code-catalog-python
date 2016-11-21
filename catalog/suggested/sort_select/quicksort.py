import random


class Quicksort(object):
    def __init__(self, data):
        self.__data = data

    def sort(self):
        self.quicksort(0, len(self.__data) - 1)

        return self.__data

    def quicksort(self, start, end):
        if end == start:
            return

        data = self.__data

        pivot = data[random.randint(start, end)]

        left = start
        right = end

        while left < right:
            while data[left] < pivot:
                left += 1

            while data[right] > pivot:
                right -= 1

            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        if start < right:
            self.quicksort(start, right)

        if left < end:
            self.quicksort(left, end)


def main():
    numbers = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
               597, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 42, 7506,
               184, 184, 2409, 45, 824, 4, -2650, 9, 662, 3928,
               -170, 45358, 395, 842, 7697, 110, 14, 99, 221]

    qs = Quicksort(numbers)
    output = qs.sort()

    print(output)


if __name__ == '__main__':
    main()
