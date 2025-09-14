from Cryptodome.Util.number import *

base10_str = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

n = int(base10_str)

msg = long_to_bytes(n).decode("ascii")

print(msg)