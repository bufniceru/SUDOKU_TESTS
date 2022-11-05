from SUDOKU.BOARD.HELPERS.Value import Value


class TestValue:
    def test_value_constructor_none(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_constructor_int(self):

        sut = Value(5)

        assert hasattr(sut, 'value') is True
        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_constructor_str(self):

        sut = Value('5')

        assert hasattr(sut, 'value') is True
        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_constructor_1(self):

        sut = Value(1)

        assert hasattr(sut, 'value') is True
        assert sut.value == 1
        assert f'{sut}' == '1'

    def test_value_constructor_9(self):

        sut = Value(9)

        assert hasattr(sut, 'value') is True
        assert sut.value == 9
        assert f'{sut}' == '9'

    def test_value_constructor_int_0(self):

        sut = Value(0)

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_constructor_str_0(self):

        sut = Value('0')

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_constructor_int_10(self):

        sut = Value(10)

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_constructor_str_10(self):

        sut = Value('10')

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_from_int(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None

        sut.from_int(5)

        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_from_str(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None

        sut.from_str('5')

        assert sut.value == 5
        assert f'{sut}' == '5'
