from pwn import * # pip install pwntools
import json, codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()
    print("Received:", received)

    if "flag" in received:
        print("Flag:", received["flag"])
        break

    typ = received["type"]
    data = received["encoded"]

    # Giải mã theo từng loại
    if typ == "hex":
        decoded = bytes.fromhex(data).decode()
    elif typ == "base64":
        decoded = base64.b64decode(data).decode()
    elif typ == "rot13":
        decoded = codecs.decode(data, "rot_13")
    elif typ == "bigint":
        n = int(data, 16)
        decoded = n.to_bytes((n.bit_length() + 7) // 8, "big").decode()
    elif typ == "utf-8":
        decoded = bytes(data).decode("utf-8")
    else:
        print("Chưa xử lý type:", typ)
        break

    # Gửi đáp án
    to_send = {"decoded": decoded}
    json_send(to_send)

