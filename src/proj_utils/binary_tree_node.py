from typing import Self

class BinaryNode[T]:
    value: T
    left: Self | None
    right: Self | None

    def __init__(self, value: T, left, right) -> None:
        self.value=value
        self.left=left
        self.right=right
