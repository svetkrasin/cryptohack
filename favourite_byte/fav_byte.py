import imp
from pwn import *

string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytes_string = bytes.fromhex(string)
for byte in range(256):
	if 'crypto' in xor(bytes_string, byte).decode('utf-8'):
		print(xor(bytes_string, byte))
		break