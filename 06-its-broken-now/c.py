from __future__ import annotations

import a


class C:
    def __init__(self, value: int):
        self.value = value
        self.a = a.A(value)

    def get_a(self) -> a.A:
        return self.a

    def __str__(self) -> str:
        return f"C({self.value})"
