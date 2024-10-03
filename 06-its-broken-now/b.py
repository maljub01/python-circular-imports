from typing import TYPE_CHECKING

from c import C

if TYPE_CHECKING:
    from a import A


class B:
    def __init__(self, value: int):
        self.value = value
        self.c = C(value)

    def get_a(self) -> "A":
        from a import A

        return A(self.value)

    def get_c(self) -> C:
        return self.c

    def __str__(self) -> str:
        return f"B({self.value})"
