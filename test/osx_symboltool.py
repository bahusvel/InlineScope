import os
import sys
import re

def get_text_bytes_and_offset():
	os.system("otool -X -t {} > __text_tmp".format(sys.argv[1]))
	tmp_text = open("__text_tmp", "r")
	text_dump = tmp_text.readlines()
	tmp_text.close()
	os.unlink("__text_tmp")

	hexstring = ""
	for line in text_dump:
		line = line[17:-1] # strip off address and new lines
		hexstring += line.replace(" ", "")

	text_bytes = bytearray.fromhex(hexstring)
	return (int(text_dump[0][:16], base=16), text_bytes)

class Symbol:

	@staticmethod
	def symbol_from_buffer(symbol_name, buffer):
		symbol = Symbol()
		symbol.name = symbol_name
		symbol.start_addr = int(buffer[0][:16], base=16)
		symbol.end_addr = int(buffer[-1][:16], base=16)
		symbol.assembly = "".join(buffer)
		return symbol

	def find_raw_bytes(self, section_offset, section_bytes):
		self.raw_bytes = section_bytes[self.start_addr - section_offset: self.end_addr - section_offset]

	def dump_symbol(self, directory):
		symbol_file = open("{}/{}".format(directory, self.name), 'wb')
		symbol_file.write(self.raw_bytes)
		symbol_file.close()

	def __repr__(self):
		return "{} ({}-{}):\n{}".format(self.name, self.start_addr, self.end_addr, self.raw_bytes)

	def __init__(self):
		self.name = ""
		self.assembly = ""
		self.raw_bytes = []
		self.start_addr = 0
		self.end_addr = 0

if (len(sys.argv) != 3):
	print("Usage: python3 osx_symboltool.py input_file_macho symbols_output_dir")
	exit(1)

os.system("otool -t -v {} > __text_tmp_asm".format(sys.argv[1]))

tmp_text = open("__text_tmp_asm", "r")
text_dump = tmp_text.readlines()
tmp_text.close()
os.unlink("__text_tmp_asm")

symbol_buffer = []
symbol_name = ""
symbols = []

section_offset, section_bytes = get_text_bytes_and_offset()

for line in text_dump:
	if re.match(".+\:$", line):
		if symbol_name != "" and len(symbol_buffer) >= 2:
			symbol = Symbol.symbol_from_buffer(symbol_name, symbol_buffer)
			symbol.find_raw_bytes(section_offset, section_bytes)
			symbol.dump_symbol(sys.argv[2])
			symbols.append(symbol)
		symbol_name = line[:-2]
		symbol_buffer = []
	else:
		symbol_buffer.append(line)

#print(symbols)
