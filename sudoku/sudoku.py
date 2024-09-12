

class Sudoku:
    def __init__(self, dimensions: int, difficulty: float) -> None:
        self.dimensions = dimensions
        self.difficulty = difficulty

    def _generate(self) -> None:
        ...

    def show(self) -> None:
        ...

    def solve(self) -> None:
        ...

    def solution(self) -> None:
        ...
