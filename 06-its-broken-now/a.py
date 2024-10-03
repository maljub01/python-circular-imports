from __future__ import annotations

import b


class A:
    def __init__(self, value: int):
        self.value = value

    def get_b(self) -> b.B:
        return b.B(self.value)

    def __str__(self) -> str:
        return f"A({self.value})"
