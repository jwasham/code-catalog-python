def multiply(a, b):
    val = 0

    while b > 0:
        val += a
        b -= 1

    return val


def add(a, b):
    sum = 0

    while sum < b:
        sum += 1
        a += 1

    return a


def divide(a, d):
    if d == 0:
        raise ValueError('Cannot divide by 0.')

    q = 0
    r = a

    while r >= d:
        r -= d
        q += 1

    print("{} div by {} = {} remainder {}".format(a, d, q, r))


def power(base, exp):
    val = 1

    for _ in range(exp):
        val *= base

    return val


def power2(base, exp):
    if exp == 0:
        return 1
    else:
        partial = power(x, exp // 2)  # rely on truncated division
        result = partial * partial
        if exp % 2 == 1:  # if n odd, include extra factor of x
            result *= base

        return result


def factorial(n):
    val = 1

    for num in range(n, 0, -1):
        val *= num

    return val


def fib(n):
    a, b = 1, 1

    for _ in range(1, n):
        a, b = b, a + b

    return a


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def gcd(a, b):
    while a:
        b, a = a, b % a

    return b


def lcm(a, b):
    return (a * b) / gcd(a, b)
