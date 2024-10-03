from b import B


class A:
    def __init__(self, value: int):
        self.value = value

    def get_b(self) -> B:
        return B(self.value)

    def __str__(self) -> str:
        return f"A({self.value})"
