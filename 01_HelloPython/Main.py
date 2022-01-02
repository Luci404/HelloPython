"""
Variables:
[cpp] Datatype name = value
[py] name: Datatype = value

Class:
[cpp] class ClassName : ParentClass {}
[py] class ClassName(ParentClass):

Function:
[cpp] ReturnType FunctionName(Parameters) {}
[py] def FunctionName(Parameters) -> ReturnType:
"""
import random

class Dice:
    _sides: int = 0

    def __init__(self, sides: int):
        self._sides = sides

    def Roll(self) -> int:
        return random.randint(1, self._sides)

d6: Dice = Dice(6)
d20: Dice = Dice(20)

print(d20.Roll())