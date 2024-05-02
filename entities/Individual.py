from typing import List, Dict, Tuple
from util.config import target_note
from util.config import target_dict


# one melody solution
class Individual:
    def __init__(self, notes: List[str]):
        self.notes = notes
        self.dict_notes: Dict[Tuple | str, int] = {}

        for note in notes:
            self.dict_notes[note] = self.dict_notes.get(note, 0) + 1  # increases number of occurrences of the given key

        self.dict_notes: Dict[str, int] = dict(sorted(self.dict_notes.items()))

    # str representation of object
    def __str__(self):
        return repr(self.notes)

    # hash value
    def __hash__(self):
        return hash(str(self.notes))

    # gets the number of the same key-value pairs in two dictionaries, used in fitness function
    def number_of_shared_items(self) -> int:
        num = 0
        for key, value in target_dict.items():
            if key in self.dict_notes and value == self.dict_notes[key]:
                num += 1

        return num

    # calculates fitness value for each individual based on two criteria:
    # if target melody and current melody have the same note at the same index then
    # it gives 10 points(max = number of notes * 10)

    # if current melody has the same number of occurrences of the given note as in target melody
    # then it gives 5 points(max = number of different notes in target melody * 5)
    def fitness(self) -> int:
        sum_value = 0
        for note, target in zip(self.notes, target_note):
            if note == target:
                sum_value += 10

        sum_value += self.number_of_shared_items() * 5
        return sum_value
