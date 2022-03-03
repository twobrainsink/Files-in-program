import base64

def encode_to_base64(file:str) -> str:
    with open(file, "rb") as file:
        bytes_f = file.read()
        output = base64.b64encode(bytes_f)
    return output.decode()

def decode_to_file(file_name:str, file:str) -> None:
    with open(file_name, "wb") as f:
        f.write(base64.b64decode(file))