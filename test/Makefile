clean:
	rm -rf inline __*

inline:
	gcc -O inline.c -o inline

disasm: inline
	otool -X -t -v inline > __text_clean.asm
	otool -t -v -V inline > __text_human.asm

text_tool: inline
	python3 osx_textool.py inline __text

run: clean inline disasm text_tool
