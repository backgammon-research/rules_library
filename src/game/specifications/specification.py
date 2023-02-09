from ..game_entities.move import Move
from ..game_entities.dice import DiceRoll
from ..game_entities.board import Board
from ..agent.agent import Player

from copy import copy


class Specification:
    """
    Base class for all rules.
    """
    def get_available_moves(self, dice: DiceRoll, board: Board, current_agent: Player) -> list[list[Move]]: # noqa
        """
        High-level API to generate all available from board and dice.
        Some methods should be implemented by every Rules.
        """
        all_trees: list[list[Move]] = []
        permutations_dice: list[list[int]] = dice.get_permutations()
        base_board = copy(board)
        for dice_comb in permutations_dice:
            new_tree: list[Move] = self.get_moves_from_perm(dice_comb, board, current_agent, base_board) # noqa
            all_trees.append(new_tree)

        return all_trees

    def get_moves_from_perm(self,
                            dice_comb: list[int],
                            board: Board,
                            current_agent: Player,
                            base_board: Board) -> list[Move]: # noqa
        """
        Recursive method to generate available moves
        from each position with each dice.
        """
        all_moves: list[Move] = []

        for cell in board:
            for dice in dice_comb:
                if cell.player != current_agent.color:
                    continue

                from_pos = cell.pos
                to_pos = cell.pos + dice

                if not self.check_possible_move(from_pos, to_pos, board, current_agent, base_board): # noqa
                    continue
                new_move: Move = Move(from_pos, to_pos)
                self.implement_move(new_move, board)

                new_dice_comb: list[int] = list(dice_comb)
                new_dice_comb.remove(dice)
                new_move.next_moves = self.get_moves_from_perm(new_dice_comb, board, current_agent, base_board) # noqa

                self.cancel_move(new_move, board)
                all_moves.append(new_move)

        return all_moves

    def check_possible_move(self,
                            from_pos: int,
                            to_pos: int,
                            board: Board,
                            current_agent: Player,
                            base_board: Board) -> bool: # noqa
        """
        Answer on question, can I implement one atomic move or not.
        """
        raise NotImplementedError

    def implement_move(self, move: Move, board: Board) -> None:
        """
        Release move on a board.
        """
        raise NotImplementedError

    def cancel_move(self, move: Move, board: Board) -> None:
        """
        Cancel move on a board.
        """
        raise NotImplementedError

    @classmethod
    def get_flat_moves(cls, forest_moves) -> set[tuple[int]]:
        all_flat_moves = []
        max_move_size = 0

        for tree_moves in forest_moves:
            for move in tree_moves:
                current_flat_move = []
                max_move_size = cls.dfs_search(move, current_flat_move, all_flat_moves, max_move_size) # noqa

        all_flat_moves = [move for move in all_flat_moves if len(move) == max_move_size] # noqa

        return set(all_flat_moves)

    @classmethod
    def dfs_search(cls, actual_move: Move, full_move: list[tuple[int, int]], flat_moves_storage, max_size): # noqa
        full_move.append((actual_move.from_cell, actual_move.to_cell))

        if len(actual_move.next_moves) == 0:
            if len(full_move) >= max_size:
                flat_moves_storage.append(tuple(full_move))
                max_size = max(max_size, len(full_move))

            return max_size

        for move in actual_move.next_moves:
            max_size = max(max_size, cls.dfs_search(move, copy(full_move), flat_moves_storage, max_size)) # noqa

        return max_size
