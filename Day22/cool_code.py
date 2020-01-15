print('\033c')

print("\t\033[35;1;6;4;5mTuesday Time!\033[0m\n")


from dis import dis
import opcode


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers[:]

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return f"{id(self)}: {self.passengers}"

import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

a = [10, 20]
b = [a, 30]
a.append(b)

from copy import deepcopy
c1 = deepcopy(a)
print(c1)
import pdb; pdb.set_trace()

print(c1[2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2][0][2])



print("Done")