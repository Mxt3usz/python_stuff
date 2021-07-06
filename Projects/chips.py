from dataclasses import dataclass
from typing import Union

#jeder spieler sammelt chips bekommt punkte
#pro zug bekommt spieler zufälligen chips
#punktewert des neuen chips wird zu Punktestand addiert
#mehr als 7 punkte nach weißem chip verloren
#bei orange passiert nichts
#bei rot und einem oder zwei orangenem extra punkte
#bei 3 oder mehr 2 extra
@dataclass
class White:
    points : int

@dataclass
class Orange:
    points : int


@dataclass
class Red:
    points : int

@dataclass
class GameState:
    stack : [White,Red,Orange]
    total : int

def add_chip(state : GameState, chips:Union[White,Orange,Red]):
    if isinstance(chips,Red):
        for chip in state.stack:
            if chip == Orange:
                chip = Orange
                if chip.points > 2:
                    stack.total += 2
                else:
                    stack.total += 1
    if isinstance(chips,White):
        old = state.total
        state.total +=  chips.points
        state.stack.append(chips)
        return state if old <= 7 and state.total < 8 else None

    if isinstance(chips,Orange):
        state.total += chips.points
        state.stack.append(chips)
        return state
    if isinstance(chips,Red):
        state.total += chips.points
        state.stack.append(chips)
        return state
state = GameState([], 0)
state = add_chip(state, White(3))
state = add_chip(state, Orange(3))
state = add_chip(state, Red(1))
stack = add_chip(state, White(1))
print(state.total)
print(state.stack)
