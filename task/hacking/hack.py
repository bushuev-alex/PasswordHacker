import socket
import argparse


class Hacktool:

    def __init__(self, data):
        self.hostname = data[0]
        self.port = int(data[1])
        self.password = data[2]
        self.address = (self.hostname, self.port)
        self.my_socket = None
        self.recv_data = None

    def connect_to_socket(self):
        self.my_socket = socket.socket()
        self.my_socket.connect(self.address)
        
    def send_data(self):
        pasw = str.encode(self.password)
        self.my_socket.send(pasw)

    def receive(self):
        self.recv_data = self.my_socket.recv(1024).decode()

    def close(self):
        self.my_socket.close()


parser = argparse.ArgumentParser()
parser.add_argument("hostname", default='localhost')
parser.add_argument("port", default=9090)
parser.add_argument("password", default=111111)
args = parser.parse_args()
params = [args.hostname, args.port, args.password]


my_hacktool = Hacktool(params)
my_hacktool.connect_to_socket()
my_hacktool.send_data()
my_hacktool.receive()
print(my_hacktool.recv_data)
my_hacktool.close()

