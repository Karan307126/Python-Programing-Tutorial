def topten():
    n = 1
    while(n <= 10):
        sq = n * n
        yield sq    # yield is make a method to generator.and it's give us iterator.
        n += 1

a = topten()

for i in a:
    print(i)