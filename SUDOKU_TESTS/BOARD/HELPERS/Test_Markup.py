from SUDOKU.BOARD.HELPERS.Markup import Markup
from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class TestMarkup:
    def test_markup_constructor_void(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

    def test_markup_constructor_discard(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.discard(5)

        assert sut.value == {1, 2, 3, 4, 6, 7, 8, 9}

        sut.discard(2)

        assert sut.value == {1, 3, 4, 6, 7, 8, 9}

        sut.discard(8)

        assert sut.value == {1, 3, 4, 6, 7, 9}

        sut.discard(4)

        assert sut.value == {1, 3, 6, 7, 9}

        sut.discard(7)

        assert sut.value == {1, 3, 6, 9}

        sut.discard(1)

        assert sut.value == {3, 6, 9}

        sut.discard(9)

        assert sut.value == {3, 6}

        sut.discard(3)

        assert sut.value == {6}

        sut.discard(6)

        assert sut.value == set()

    def test_markup_constructor_reset(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.discard(5)
        sut.discard(2)
        sut.discard(8)
        sut.discard(4)
        sut.discard(7)
        sut.discard(1)
        sut.discard(9)
        sut.discard(3)
        sut.discard(6)

        assert sut.value == set()

        sut.reset()

        assert sut.value == ALL_POSSIBILITIES_SET

    def test_markup_fill(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.fill({2, 5, 7})

        assert sut.value == {2, 5, 7}
