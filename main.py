import pygame
from enum import Enum


CELL_SIZE = 50


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
    def __int__(self):
        self.height = 3
        self.wigth = 3
        self.cells = [[Cell.VOID]*self.wigth for i in range(3)]


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а так же выясняет место клика
    """
    def __int__(self, field):
        # Загрузить картинки значков клеток и тд.
        # Отобразить первичное сосотояние поля
        self._field = field
        self._height = field.heiht * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True # TODO: self._height учесть

    def get_coords(self, x, y):
        return (0, 0)  # TODO: реально вычислить клетку клика


class GameRoundManager:
    """
    Менеджер игры запускающий все процессы
    """
    def __int__(self, player1: Player, player2: Player):
        self._plaers = [player1, player2]
        self._current_pLayer = 0
        self._field = GameField()

    def handle_click(self, i, j):
        plaer = self._plaers[self._current_pLayer]
        # Игрок делает клик на поле
        print("handle_click, i, j")


class GameWindow:
    """
    Содержит виджет поля, а так же менеджера игрового раунда.
    """
    def __int__(self):
        # Инициализация pygame
        pygame.init()

        self._width = 800
        self._height = 600
        self._title = "Crosses & Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        player1 = Player("Петья", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager._field)

    def main_loop(self):
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)


