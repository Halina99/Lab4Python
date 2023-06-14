def newton(n, k):
    if k == 0 or k == n:
        return 1
    elif 0 < k < n:
        return newton(n-1, k-1) + newton(n-1, k)


print(newton(7, 2))
