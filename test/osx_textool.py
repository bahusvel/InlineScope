import os
import sys

if (len(sys.argv) != 3):
	print("Usage: python3 osx_textool.py input_file_macho output_file")
	exit(1)

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

output_file = open(sys.argv[2], 'wb')
output_file.write(text_bytes)
output_file.close()
