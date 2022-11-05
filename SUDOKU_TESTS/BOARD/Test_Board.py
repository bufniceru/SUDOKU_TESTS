from SUDOKU.BOARD.Board import Board
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.BOARD.LOADERS.StringBoard import StringBoard
from SUDOKU.BOARD.LOADERS.StringBoardLoader import StringBoardCreator
from SUDOKU.BOARD.OUTPUT.BoardLogOutput import BoardLogOutput
from SUDOKU.CONFIG.Constants import BOARD_DIMENSION, ALL_POSSIBILITIES_SET, EMPTY_SET


class TestBoard:
    def test_board_constructor(self):

        sut = Board()

        assert sut.validity is True
        assert sut.blanks == 81
        assert sut.givens == 0

        assert sut.board.shape == (9,9)
        assert sut.board.ndim == 2

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                assert sut.board[line][column]() == 0
                assert sut.board[line][column].markup.value == ALL_POSSIBILITIES_SET
                assert sut.board[line][column].coordinates.line == line + 1
                assert sut.board[line][column].coordinates.column == column + 1

    def test_board_string_board_creator(self):

        string_board = StringBoard('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        sut = StringBoardCreator.create_board(string_board.string)

        assert sut.validity is True
        assert sut.blanks == 55
        assert sut.givens == 26
        assert sut.how_many(1) == 3
        assert sut.how_many(2) == 1
        assert sut.how_many(3) == 3
        assert sut.how_many(4) == 1
        assert sut.how_many(5) == 2
        assert sut.how_many(6) == 4
        assert sut.how_many(7) == 4
        assert sut.how_many(8) == 4
        assert sut.how_many(9) == 4

        assert sut.board.shape == (9,9)
        assert sut.board.ndim == 2

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                if sut.board[line][column]() == 0:
                    assert sut.board[line][column].markup.value == ALL_POSSIBILITIES_SET
                else:
                    assert sut.board[line][column].markup.value == EMPTY_SET
                assert sut.board[line][column].coordinates.line == line + 1
                assert sut.board[line][column].coordinates.column == column + 1
                assert sut.board[line][column] == string_board.cell(line + 1, column + 1)

    def test_board_cells(self):

        string_board = StringBoard('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        sut = StringBoardCreator.create_board(string_board.string)

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                assert sut.cell(Coordinates((line + 1, column + 1))) == string_board.cell(line + 1, column + 1)

    def test_board_validity(self):

        string_board = StringBoard('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        sut = StringBoardCreator.create_board(string_board.string)

        assert sut.validity is True

    def test_board_string_board_print_bare(self):

        string_board = StringBoard('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        sut = StringBoardCreator.create_board(string_board.string)

        prnt = BoardLogOutput(sut)

        print('\n')
        prnt.bare()

    def test_board_string_board_print_full_at_first(self):

        sut = StringBoardCreator.create_board('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        prnt = BoardLogOutput(sut)

        print('\n')
        prnt.full()

    def test_board_string_board_line(self):

        sut = StringBoardCreator.create_board('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        assert sut.line == '000600000874000000000030097067900050900106008080003160720080000000000935000001000'
