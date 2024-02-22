#!/usr/bin/env pypy3

import sys

import stack
import opcodes

MAIN_STACK: stack.Stack = opcodes.global_stack


#  return list of each instruction in the program
def read_script(filename: str) -> list[str]:
	with open(filename, 'r') as f:
		return f.read().split()


def dispatch(opc: str):
	opcodes.OPCODES[opc]()


def main(argv: list[str]) -> int:
	prog = read_script(argv[1])
	for instr in prog:
		if opcodes.is_opcode(instr):
			dispatch(instr)
		else:
			MAIN_STACK.push(instr)
		print(MAIN_STACK)

	return 0


if __name__ == "__main__":
	ret = main(sys.argv)
	sys.exit(ret)
