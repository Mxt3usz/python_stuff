from dataclasses import dataclass
from typing import Optional
import pytest

@dataclass
class Chip:
    points: int

@dataclass
class GameState:
    stack: list[Chip]
    total: int

@dataclass
class ColoredChip(Chip):
    def add_chip(self, state: GameState) -> Optional[GameState]:
        state.total += self.points
        state.stack.append(self)

@dataclass
class White(ColoredChip):
    def add_chip(self, state: GameState) -> Optional[GameState]:
        super().add_chip(state)
        white_points = 0
        for chip in state.stack:
            if isinstance(chip, White):
                white_points += chip.points
        return state if white_points <= 7 else None

@dataclass
class Orange(ColoredChip):
    def add_chip(self, state: GameState) -> Optional[GameState]:
        super().add_chip(state)
        return state

@dataclass
class Red(ColoredChip):
    def add_chip(self, state: GameState) -> Optional[GameState]:
        super().add_chip(state)
        orange_count = 0
        for chip in state.stack:
            if isinstance(chip, Orange):
                orange_count += 1
        if orange_count > 0:
            state.total += 1
            if orange_count > 2:
                state.total += 1
        return state

def add_chip(state: GameState, chip: ColoredChip)-> Optional[GameState]:
    return chip.add_chip(state)


state = GameState([], 0)
state = add_chip(state, White(3))
state = add_chip(state, Red(1))
state = add_chip(state, Red(2))
print(state.total)

print(state.stack)
