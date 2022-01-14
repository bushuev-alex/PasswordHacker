import itertools
from string import digits, ascii_lowercase
data = ascii_lowercase + digits
import os

my_gen = itertools.product([['g', 'G'], ['o', 'O'], ['l', 'L'], ['f', 'F']])

for let in my_gen:
    print(next(let))




"""def numbers():
    for n_step in range(4):
        item = itertools.product(data, repeat=n_step)
        yield item

my_gen = numbers()
for b in my_gen:
    for t in b:
        print(''.join(t))"""

"""def gen_line(line):
    new_words = [line]
    new_word = [b for b in line]
    for i in range(len(line)):

        new_words.append(''.join(new_word))
    print(new_words)    
    
gen_line('word')"""


"""with open("passwords.txt", "r") as file:
    text = file.readlines()"""
        
"""for i in 'word':
    item = itertools.combinations(i + i.capitalize(), 2)
    for j in item:
        print(j)
"""
