#!/usr/bin/env pypy3

import sys

import stack
import opcodes
import time

MAIN_STACK: stack.Stack = opcodes.global_stack
TIME_FLAG: int = sys.argv[2] if len(sys.argv) > 2 else 0

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
	return 0


if __name__ == "__main__":
	if TIME_FLAG:
		num_runs: int = sys.argv[3] if len(sys.argv) > 3 else 1000
		start_time: float = time.time()
		for i in range(num_runs):
			main(sys.argv)
		end_time: float = time.time()
		# Average time to run script in seconds
		avg_time: float = (end_time - start_time) / num_runs
		print(f"Average time per run for {num_runs} runs: {avg_time} seconds")
	else:
		main(sys.argv)
	
	if MAIN_STACK.empty() or not opcodes.convert_to_bool(MAIN_STACK.pop()):
		print("Invalid Transaction!")
	else:
		print("Valid Transaction!")
		
	sys.exit(0)
