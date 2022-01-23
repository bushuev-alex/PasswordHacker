import json


def get_login():
    with open("logins.txt", "r") as login_file:
        for line in login_file:
            js_data = json.dumps({"login": f"{line.strip()}", "password": f"{''}"})
            yield js_data


my_gen = get_login()
print(json.loads(next(my_gen))['login'])
print(next(my_gen))
print(next(my_gen))



"""import itertools
from string import digits, ascii_lowercase
data = ascii_lowercase + digits
import os"""

"""a = itertools.product([1,2], [3,4], [5,6])
for i in a:
    print(i)"""

"""my_gen = itertools.product([['g', 'G'], ['o', 'O'], ['l', 'L'], ['f', 'F']])
for let in my_gen:
    print(next(let))"""

"""def itet():
    word = 'word'
    upper_lower_list = []
    if not word.strip().isdigit():
        for letter in word.strip():
            upper_lower_list.append([letter.upper(), letter.lower()])
        res = itertools.product(*upper_lower_list)
        for item in res:
            yield ''.join(item)

my_itet = itet()
print(next(my_itet))
print(next(my_itet))
print(next(my_itet))
print(next(my_itet))"""

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
