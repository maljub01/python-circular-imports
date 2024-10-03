from a import A


class B:
    def __init__(self, value: int):
        self.value = value

    def get_a(self) -> A:
        return A(self.value)

    def __str__(self) -> str:
        return f"B({self.value})"
