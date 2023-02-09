class Move:
    def __init__(self, from_cell, to_cell):
        self.from_cell = from_cell
        self.to_cell = to_cell
        self.next_moves = {}

    def __repr__(self):
        return f"pos: {self.from_cell}, dice: {self.to_cell}, next_moves: {self.next_moves}"

    def __str__(self):
        return f"from_pos: {self.from_cell}, dice: {self.to_cell}, next_moves: {self.next_moves}"
