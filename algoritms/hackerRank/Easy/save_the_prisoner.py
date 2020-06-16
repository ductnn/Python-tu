test_cases = int(input())

for _ in range(test_cases):
    n, m, s = map(int, input().split())

    while m > 0:
        m -= 1
        s = n if s > n else s + 1

    s = n if s < 1 else s - 1
    print(s)