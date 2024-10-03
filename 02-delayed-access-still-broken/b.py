import a


class B:
    def __init__(self, value: int):
        self.value = value

    def get_a(self) -> a.A:
        return a.A(self.value)

    def __str__(self) -> str:
        return f"B({self.value})"
