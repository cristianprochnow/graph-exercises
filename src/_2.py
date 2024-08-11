import csv
from typing import Dict, Any


class States:
    borders: dict[str, list[str]]

    def __init__(self):
        self.borders = {}

        self.__build()

    def __build(self):
        with open('../assets/states_brazil.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            row_index = 0
            for states in reader:
                row_index += 1

                if row_index == 1:
                    continue

                col_index = 0
                border_index = ''
                for border in states:
                    col_index += 1

                    if col_index == 1:
                        border_index = border
                        self.borders[border_index] = []

                        continue

                    self.borders[border_index].append(border.strip())

    def list(self) -> Dict[str, list[str]]:
        return self.borders

    def min(self) -> str:
        min_amount = 100
        min_state = ''

        for state, borders in self.borders.items():
            if len(borders) < min_amount:
                min_amount = len(borders)
                min_state = state

        return 'O estado %s é o estado com menos fronteiras, tendo apenas %s' % (min_state, min_amount)

    def max(self) -> str:
        max_amount = 0
        max_state = ''

        for state, borders in self.borders.items():
            if len(borders) > max_amount:
                max_amount = len(borders)
                max_state = state

        return 'O estado %s é o estado com mais fronteiras, tendo %s' % (max_state, max_amount)


states = States()

print(states.list())
print(states.min())
print(states.max())
