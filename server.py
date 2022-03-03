import socket
import converter
import getpass

class Server:
    def __init__(self) -> None:
        self.socket = socket.socket()
        self.ip = ""
        self.port = "Your open port"
        self.conn = None
        self.adrr = None

    def start_server(self) -> None:
        self.socket.bind((self.ip, self.port))
        self.socket.listen(3)
        self.conn, self.adrr = self.socket.accept()

    def recv_file(self):
        name = self.conn.recv(3000).decode("utf-8")
        file = self.conn.recv(3000).decode("utf-8")
        if input("Do you want to accept the file? (yes/no)\n") == "yes":
            converter.decode_to_file(name, file)

    def send_file(self, path_to_file:str, name:str) -> None:
        file = converter.encode_to_base64(path_to_file)
        self.conn.send(name.encode("utf-8"))
        self.conn.send(file.encode("utf-8"))

    def main(self):
        self.start_server()
        while True:
            cmd = input(">>")
            if cmd == "send":
                path = input("Enter the file name: ")
                if "/" in path:
                    name = path.split("/")[-1]
                else:
                    s = path.split(".")
                    name = s[0] + f"(by {getpass.getuser()})" + "." + s[1]
                self.send_file(path, name)
            elif cmd == "accept":
                self.recv_file()

server = Server()
server.main()