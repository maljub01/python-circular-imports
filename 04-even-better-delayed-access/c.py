from a import A


class C:
    def __init__(self, value: int):
        self.value = value
        self.a = A(value)

    def get_a(self) -> A:
        return self.a

    def __str__(self) -> str:
        return f"C({self.value})"
