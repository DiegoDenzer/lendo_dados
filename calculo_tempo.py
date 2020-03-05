from timeit import timeit

v1 = timeit('f1()', 'from main import f1', number=10)

print(v1)