# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# pat  -> pattern
# txt  -> text
# q    -> A prime number


def search(pat, txt, q):
    m = len(pat)
    n = len(txt)
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # d is the number of characters in input alphabet
    d = 256

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(m):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            # if p == t and pat[0...m-1] = txt[i, i+1, ...i+m-1]
            if j == m:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q


# Driver program to test the above function
txt = "a hello there to you all! hello all!"
pat = "hello"
q = 101  # A prime number
search(pat, txt, q)
