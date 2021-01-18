"""
Chess board module
"""
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import QMargins

RANKS = [1, 2, 3, 4, 5, 6, 7, 8]
FILES = ["A", "B", "C", "D", "E", "F", "G", "H"]


class Board(QWidget):
    """ The chess board """

    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.gen_board()
        self.grid_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.grid_layout.setSpacing(0)
        self.setLayout(self.grid_layout)

    def gen_board(self):
        """ Generates a board widget """
        for rank in range(len(RANKS)):
            for file in range(len(FILES)):
                tile = QPushButton(
                    f"{RANKS[len(RANKS) - rank - 1]}{FILES[file]}"
                )
                tile.setFixedSize(50, 50)
                if rank % 2 == 0:
                    if file % 2 == 0:
                        tile_color = "white"
                    else:
                        tile_color = "brown"
                else:
                    if file % 2 == 0:
                        tile_color = "brown"
                    else:
                        tile_color = "white"
                tile.setStyleSheet(f"background-color : {tile_color}")
                self.grid_layout.addWidget(tile, rank, file)
