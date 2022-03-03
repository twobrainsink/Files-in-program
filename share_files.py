import socket
import converter
import getpass
class Share:
    def __init__(self) -> None:
        self.socket = socket.socket()
        self.port = "Your open port"
        self.ip = "Local or global IP servers"

    def connect_to_server(self):
        self.socket.connect((self.ip, self.port))
            

    def send_file(self, path_to_file:str, name:str) -> None:
        file = converter.encode_to_base64(path_to_file)
        self.socket.send(name.encode("utf-8"))
        self.socket.send(file.encode("utf-8"))

    def recv_file(self):
        name = self.socket.recv(3000).decode("utf-8")
        file = self.socket.recv(3000).decode("utf-8")
        if input("Do you want to accept the file? (yes/no)\n") == "yes":
            converter.decode_to_file(name, file)

    def main(self):
        while True:
            try:
                print("Waiting for connection...")
                self.connect_to_server()
                print("Successfully connected!")
                break
            except:
                pass
        while True:
            cmd = input(">>")
            if cmd == "send":
                path = input("Enter the file name: ")
                if "/" in path:
                    s = path.split("/")[-1].split(".")
                    name = s[0] + f"(by {getpass.getuser()})" + "." + s[1]
                else:
                    s = path.split(".")
                    name = s[0] + f"(by {getpass.getuser()})" + "." + s[1]
                self.send_file(path, name)
            elif cmd == "accept":
                self.recv_file()


share = Share()
share.main()