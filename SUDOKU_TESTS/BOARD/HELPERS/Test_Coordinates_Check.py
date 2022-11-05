import pytest

from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates


class TestCoordinates_Check:
    def test_coordinates_constructor_check_inside(self):

        print('\n')
        assert Coordinates.check(5) is True

    def test_coordinates_constructor_check_outside_low(self):

        print('\n')
        with pytest.raises(Exception):
            Coordinates.check(0)

    def test_coordinates_constructor_check_outside_high(self):

        print('\n')
        with pytest.raises(Exception):
            Coordinates.check(10)
