clean:
	rm -rf inline __*
	rm -rf text_symbols

inline:
	gcc -O inline.c -o inline

disasm: inline
	otool -X -t -v inline > __text_clean.asm
	otool -t -v -V inline > __text_human.asm

text_tool: inline
	otool -t inline > __text.hex
	python3 osx_textool.py inline __text

symbol_tool:
	mkdir text_symbols
	python3 osx_symboltool.py inline text_symbols/

run: clean inline disasm text_tool symbol_tool
