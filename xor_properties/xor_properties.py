from matplotlib.pyplot import flag
from pwn import *

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2XORkey1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2XORkey3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flagXORkey1XORkey3XORkey2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key2 = xor(bytes.fromhex(key1), bytes.fromhex(key2XORkey1))
key3 = xor(key2, bytes.fromhex(key2XORkey3))
flag = xor(bytes.fromhex(flagXORkey1XORkey3XORkey2), key2, key3, bytes.fromhex(key1))
print(flag)