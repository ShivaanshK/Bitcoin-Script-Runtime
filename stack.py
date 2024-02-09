class Stack:
    contents: list[str]

    def __init__(self) -> None:
        self.contents: list[str] = []

    def push(self, val: str) -> None:
        self.contents.append(val)

    def pop(self) -> str:
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.contents.pop()

    def empty(self) -> bool:
        return len(self.contents) == 0

    def __repr__(self) -> str:
        return f"Stack(contents={self.contents})"
