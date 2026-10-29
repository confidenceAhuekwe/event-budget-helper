from enum import Enum
# Enum is a way to create a constant in python, so that nobody can reassign the values.
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(list(State))
print(len(State))