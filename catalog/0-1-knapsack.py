import numpy as np
import sys


def zero_one_knapsack(values, weights, capacity):
    n = len(values)
    # costs = [[0] * (capacity + 1) for _ in range(n)]
    c = np.zeros((n, capacity + 1))

    for i in range(0, n):
        for j in range(0, capacity + 1):
            if weights[i] > j:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = max(c[i - 1][j], values[i] + c[i - 1][j - weights[i]])

    return [c[n - 1][capacity], get_used_items(weights, c)]


# w = list of item weight or cost
# c = the cost matrix created by the dynamic programming solution
def get_used_items(weights, c):
    i = len(c) - 1
    current_w = len(c[0]) - 1

    # set everything to not marked
    marked = [0 for _ in range(i + 1)]

    while i >= 0 and current_w >= 0:
        if (i == 0 and c[i][current_w] > 0) or c[i][current_w] != c[i - 1][current_w]:
            marked[i] = 1
            current_w = current_w - weights[i]
        i -= 1

    return marked


def main():
    if len(sys.argv) != 3:
        print("Usage knapsack.py name1-weight1-val1,name2-weight2-val2,... max weight")
        print("Example:")
        print("knapsack.py iphone-1-500,clock-1-40,laptop-3-2000,guitar-2-1500 4")
        quit()

    items = sys.argv[1].split(',')
    w = []
    v = []
    names = []

    for item in items:
        nums = item.split('-')
        names.append(nums[0])
        w.append(int(nums[1]))
        v.append(int(nums[2]))

    max_cost = int(sys.argv[2])
    answer = zero_one_knapsack(v, w, max_cost)
    print("Knapsack can hold %d pounds, for $%d profit." % (max_cost, answer[0]))
    print("by taking item(s): ")

    for i in range(len(answer[1])):
        if answer[1][i] != 0:
            print(" - " + names[i])


if __name__ == '__main__':
    main()
