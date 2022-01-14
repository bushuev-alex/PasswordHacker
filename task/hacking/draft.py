import itertools
from string import digits, ascii_lowercase
data = ascii_lowercase + digits

def numbers():
    for n_step in range(4):
        item = itertools.product(data, repeat=n_step)
        yield item

my_gen = numbers()
for b in my_gen:
    for t in b:
        print(''.join(t))
