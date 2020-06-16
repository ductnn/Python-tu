def line_int():
    return [int(x) for x in input().split(' ')]

def main():
    (n, k, q) = line_int()
    arr = line_int()

    r = k%n
    for j in range(q):
        m = int(input())
        i = (m - r)
        print (arr[i if i >= 0 else i + n])

main()