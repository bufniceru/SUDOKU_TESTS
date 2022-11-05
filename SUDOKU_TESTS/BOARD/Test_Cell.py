from SUDOKU.BOARD.Cell import Cell
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET, EMPTY_SET


class TestCell:
    def test_cell_constructor_void(self):

        sut = Cell()

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None

    def test_cell_constructor(self):

        sut = Cell(5, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value == 5
        assert sut.markup.value == EMPTY_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_constructor_none_value(self):

        sut = Cell(None, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_constructor_zero_value(self):

        sut = Cell(0, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_constructor_ten_value(self):

        sut = Cell(0, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_clear_cell(self):

        sut = Cell(7, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        sut.clear_cell()

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_markup_discard(self):

        sut = Cell(0, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        sut.markup.discard(7)

        assert sut.value.value is None
        set_to_compare = set(ALL_POSSIBILITIES_SET)
        set_to_compare.remove(7)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(3)

        assert sut.value.value is None
        set_to_compare.remove(3)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(9)

        assert sut.value.value is None
        set_to_compare.remove(9)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(5)

        assert sut.value.value is None
        set_to_compare.remove(5)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(2)

        assert sut.value.value is None
        set_to_compare.remove(2)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(8)

        assert sut.value.value is None
        set_to_compare.remove(8)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(1)

        assert sut.value.value is None
        set_to_compare.remove(1)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(4)

        assert sut.value.value is None
        set_to_compare.remove(4)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

        sut.markup.discard(6)

        assert sut.value.value is None
        set_to_compare.remove(6)
        assert sut.markup.value == set()
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6

    def test_cell_fill_value_7(self):

        sut = Cell()

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None

        sut.fill_value(7)

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value == 7
        assert sut.markup.value == EMPTY_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None
