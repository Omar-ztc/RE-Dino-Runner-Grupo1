from dino_runner.components.extrasgame.extras import Extras
from dino_runner.utils.constants import HEART, HEART_TYPE

class Heart(Extras):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)