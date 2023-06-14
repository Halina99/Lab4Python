def func(x):
    for i in range(1, len(x)+1):
        yield x[:i]


napis = "spam"
print(list(func(napis)))
