from typing import List


class Sudoku:
    def __init__(self, dimensions: int, difficulty: float) -> None:
        self.dimensions = dimensions
        self.difficulty = difficulty

        self.sudoku: List[list] = []

    def _generate(self) -> None:
        ...

    def show(self) -> None:
        ...

    def solve(self) -> None:
        ...

    def solution(self) -> List[list]:
        ...
