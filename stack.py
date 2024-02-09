from typing import Generator, Any, Sequence


class Stack:
    contents: list[str]

    def __init__(self) -> None:
        self.contents: list[str] = []

    def push(self, val: str) -> None:
        self.contents.append(val)

    def push_multi(self, *items: str) -> None:
        for item in items:
            self.push(item)

    def top(self) -> str:
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.contents[-1]

    def pop(self) -> str:
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.contents.pop()

    def pop_multi(self, count: int) -> Generator[Any, str, None]:
        return (self.pop() for _ in range(count))

    def depth(self) -> int:
        return len(self.contents)

    def empty(self) -> bool:
        return len(self.contents) == 0

    def __repr__(self) -> str:
        return f"Stack(contents={self.contents})"
