class SinglyLinkedList[T]:
    length:int

    def prepend(self, item: T) -> None: 
        ...

    def insertAt(self, item: T, idx: int) -> None: 
        ...

    def append(self, item: T) -> None: 
        ...

    def remove(self, item: T) -> T | None:
        ...

    def get(self, idx: int) -> T | None: 
        ...

    def removeAt(self, idx: int) -> T | None:
        ...
