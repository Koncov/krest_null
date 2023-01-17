import pygame
from enum import Enum



class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий его тип и иимя.
    """
    def __int__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameField:
    """

    """
    pass


class GameFieldView:
    """

    """
    pass


class GameRoundManager:
    """
    Менеджер игры запускающий все процессы
    """
    def __int__(self, player1: Player, player2: Player):
        self._plaers = [player1, player2]
        self._current_pLayer = 0
        self._field = GameField()

    def handle_click(self):
        plaer = self._plaers[self._current_pLayer]
        # Игрок делает клик на поле
        pass


class GameWindow:
    """
    Содержит виджет поля, а так же менеджера игрового раунда.
    """
    def __int__(self):
        # Инициализация pygame
        self._field_widget = GameFieldView()
        player1 = Player("Петья", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)

    def main_loop(self):
        finished = False
        while not finished:
            for event in pygame.get_events(...):
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)


