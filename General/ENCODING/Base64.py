import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"



bytes_str = bytes.fromhex(hex_str)

base64_bytes = base64.b64encode(bytes_str)

print(base64_bytes)