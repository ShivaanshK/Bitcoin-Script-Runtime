#!/usr/bin/env pypy3

import sys
import stack, opcodes

MAIN_STACK = stack.Stack()


#  return list of each instruction in the program
def read_script(filename: str) -> list[tuple[str]]:
    with open(filename, 'r') as f:
        return [instr for instr in f]


def dispatch(opc: str):
    opcodes.OPCODES[opc]()


def main(argv: list[str]) -> int:
    prog = read_script(argv[1])
    print(prog)

    for instr in prog:
        if opcodes.is_opcode(instr):
            dispatch(instr)
        else:
            MAIN_STACK.push_val(instr)
        print(MAIN_STACK)

    return 0


if __name__ == "__main__":
    ret = main(sys.argv)
    sys.exit(ret)
