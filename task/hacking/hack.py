import socket
import argparse
from string import digits, ascii_lowercase
import itertools


class Hacktool:

    def __init__(self, data):
        self.hostname = data[0]
        self.port = int(data[1])
        self.password = None
        self.address = (self.hostname, self.port)
        self.my_socket = None
        self.recv_data = None
        self.psw_base = []

    def connect_to_socket(self):
        self.my_socket = socket.socket()
        self.my_socket.connect(self.address)

    def send_data(self, pasw):
        mes = pasw.strip().encode()
        self.my_socket.send(mes)

    def receive(self):
        response = self.my_socket.recv(1024)
        self.recv_data = response.decode()

    def close(self):
        self.my_socket.close()

    def gen_password(self):
        data = ascii_lowercase + digits
        for n in range(1, 4):
            n_step = itertools.product(data, repeat=n)
            yield n_step

    def lower_upper_words(self):
        with open("passwords.txt", "r") as file:
            for line in file:
                lower_upper = [[letter.lower(), letter.upper()] for letter in line.strip()]
                my_gen = itertools.product(*lower_upper)
                for item in my_gen:
                    yield ''.join(item)


parser = argparse.ArgumentParser()
parser.add_argument("hostname", default='localhost')
parser.add_argument("port", default=9090)
# parser.add_argument("password", default=None)
args = parser.parse_args()
params = [args.hostname, args.port]


my_hacktool = Hacktool(params)
my_hacktool.connect_to_socket()
words = my_hacktool.lower_upper_words()
while True:
    word = next(words)
    my_hacktool.send_data(word)
    my_hacktool.receive()
    if my_hacktool.recv_data == "Connection success!":
        print(word)
        break
my_hacktool.close()
