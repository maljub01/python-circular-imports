from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from a import A


class B:
    def __init__(self, value: int):
        self.value = value

    def get_a(self) -> "A":
        from a import A

        return A(self.value)

    def __str__(self) -> str:
        return f"B({self.value})"
