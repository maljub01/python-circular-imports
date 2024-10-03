from __future__ import annotations

import a
import c


class B:
    def __init__(self, value: int):
        self.value = value
        self.c = c.C(value)

    def get_a(self) -> a.A:
        return a.A(self.value)

    def get_c(self) -> c.C:
        return self.c

    def __str__(self) -> str:
        return f"B({self.value})"
