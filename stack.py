class StackItem:
    is_opcode: bool
    value: str

    def __init__(self, value: str, is_opcode=False):
        self.is_opcode = is_opcode
        self.value = value


class Stack:
    contents: list[StackItem]

    def __init__(self):
        self.contents = []

    # pushes instruction as a tuple (opcode, args...)
    def push_instr(self, ins: tuple[str]):
        self.push_opcode(ins[0])
        for val in ins[1:]:
            self.push_val(val)

    # pushes value
    def push_val(self, val: str):
        self.contents.append(StackItem(val, is_opcode=False))

    # pushes opcode
    def push_opcode(self, val: str):
        self.contents.append(StackItem(val, is_opcode=True))

    def pop(self) -> StackItem:
        return self.contents.pop()

    def empty(self) -> bool:
        return len(self.contents) == 0
