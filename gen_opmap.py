#!/usr/bin/env pypy3

import sys

if __name__ == "__main__":
    opdict: dict[str, str] = {}
    if len(sys.argv) == 1:
        opcodes = "opcodes.txt"
    else:
        opcodes = sys.argv[1]

    with open(opcodes, 'r') as ops:
        for op in ops:
            opc = op.strip()
            if opc == '':
                continue
            opdict[f"'{opc}'"] = f'{opc}_impl'

    with open("opcodes.py", "w+") as output:
        for fun in opdict.values():
            output.write(f'def {fun}() -> None:\n')
            output.write('\t\n')
            output.write('\treturn\n\n\n')

        output.write("OPCODES = {\n")

        for opc in opdict:
            output.write(f'\t{opc}: {opdict[opc]},\n')

        output.write('}')
