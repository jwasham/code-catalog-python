class Tower:
    def __init__(self, name):
        self.stack = []
        self.name = name

    def add(self, n):
        self.stack.append(n)

    def move_disk(self, dest):
        dest.add(self.stack.pop())

    def __str__(self):
        return self.name + str(self.stack)


def move_disks(n, origin, dest, buffer):
    if n > 0:
        move_disks(n - 1, origin, buffer, dest)
        origin.move_disk(dest)
        print(origin, buffer, dest)
        move_disks(n - 1, buffer, dest, origin)


def main():
    origin = Tower('o')
    dest = Tower('d')
    buffer = Tower('b')

    n = 3

    for disk in range(n, 0, -1):
        origin.add(disk)

    print(origin, buffer, dest)
    move_disks(n, origin, dest, buffer)


if __name__ == '__main__':
    main()
