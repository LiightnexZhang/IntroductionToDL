
import torch as d2l
#定义u = 3x^2 - 4x
def f(x):
    return 3 * x ** 2 - 4 * x

#导数定义法
def numerial_lim(f, x, h):
    return (f(x + h) - f(x)) / h

h = 0.1
for i in range(5):
    print(f'h={h:.5f}, numerial limit={numerial_lim(f, 1, h):.5f}')
    h *= 0.1