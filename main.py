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
		if not opcodes.ctrl_flow_exec(instr):
			# ignore statements within a negative IF block
			print(f'[ignored] {instr}')
			continue
		print(instr)
		if opcodes.is_opcode(instr):
			dispatch(instr)
		else:
			MAIN_STACK.push(instr)
		print(MAIN_STACK)


	if MAIN_STACK.empty() or not opcodes.convert_to_bool(MAIN_STACK.pop()):
		print("Invalid Transaction!")
	else:
		print("Valid Transaction!")

	return 0


if __name__ == "__main__":
	ret = main(sys.argv)
	sys.exit(ret)
