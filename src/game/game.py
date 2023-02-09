from src.game.specifications import Specification
from typing import Type


class Game:
    """
    High level API to work with backgammon specifications
    """
    def __init__(self, specification: Type[Specification], render_mode: bool = False): # noqa
        self.specification = specification
        self.render_mode = render_mode

    def start(self):
        pass
