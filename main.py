#!/usr/bin/env pypy3

import sys
import stack, opcodes

MAIN_STACK = stack.Stack()


#  return list of each instruction in the program
def read_script(filename: str) -> list[tuple[str]]:
    with open(filename, 'r') as f:
        return [tuple(instr.split()) for instr in f]


def dispatch():
    opc = MAIN_STACK.pop()
    assert opc.is_opcode, "attempted to dispatch non-opcode!"
    opcodes.OPCODES[opc]()


def main(argv: list[str]) -> int:
    prog = read_script(argv[1])

    for instr in prog:
        MAIN_STACK.push_instr(instr)
        dispatch()

    return 0


if __name__ == "__main__":
    ret = main(sys.argv)
    sys.exit(ret)
