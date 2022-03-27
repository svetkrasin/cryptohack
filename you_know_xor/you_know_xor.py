from pwn import *

def parital_brutefroce(string, knownkey):
	return xor(bytes_string, knownkey)

string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
partial_result = 'crypto{'

bytes_string = bytes.fromhex(string)
partial_key = parital_brutefroce(bytes_string, partial_result)
print(partial_key)
partial_key = partial_key[:len(partial_result)] + 'y'.encode()
print(partial_key)
partial_result = parital_brutefroce(bytes_string, partial_key)
print(partial_result)
