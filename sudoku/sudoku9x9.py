from typing import List

import random

from objects.sudoku import Sudoku


class Sudoku9x9(Sudoku):
    def __init__(self, difficulty: float) -> None:
        self.difficulty = difficulty
        self.sudoku: List[list] = []

    def generate(self) -> None:
        for x in range(0, 9):
            for y in range(0, 9):
                ...

    def is_valid(self) -> bool:
        for x in range(0, 9):
            for y in range(0, 9):
                ...

    def show(self) -> None:
        ...

    def solve(self) -> None:
        ...

    def solution(self) -> List[list]:
        ...
