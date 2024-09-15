from typing import List

from abc import ABC


class Sudoku(ABC):
    @classmethod
    def generate(self) -> None:
        raise NotImplementedError()

    @classmethod
    def is_valid(self) -> bool:
        raise NotImplementedError()

    @classmethod
    def show(self) -> None:
        raise NotImplementedError()

    @classmethod
    def solve(self) -> None:
        raise NotImplementedError()

    @classmethod
    def solution(self) -> List[list]:
        raise NotImplementedError()
