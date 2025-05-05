from contextlib import redirect_stdout
from io import StringIO

import pytest

from style import Style, BOLD, END


class TestStyle:
    def test_correct_ansi_code(self):
        s = Style("\033[23;1;3m")

    def test_incorrect_ansi_code_1(self):
        with pytest.raises(TypeError):
            s = Style("\033[;23;23m")

    def test_incorrect_ansi_code_2(self):
        with pytest.raises(TypeError):
            s = Style("\033[23;23;m")

    def test_incorrect_ansi_code_3(self):
        with pytest.raises(TypeError):
            s = Style("\033[-jav3m")

    def test_incorrect_ansi_code_4(self):
        with pytest.raises(TypeError):
            s = Style("not an ansi code")

    def test_string_representation(self):
        s = Style("\033[1;2;3m")

        assert "\033[1;2;3m" == str(s)

    def test_left_addition(self):
        s = Style("\033[1;2;3m")

        assert "\033[1;2;3m test" == s + " test"

    def test_right_addition(self):
        s = Style("\033[1;2;3m")

        assert "test \033[1;2;3m" == "test " + s

    def test_repr(self):
        s = Style("\033[1;2;3m")

        assert "Style(\033[1;2;3m)" == repr(s)

    def test_from_rgb_1(self):
        s = Style.from_rgb(0, 0, 0)

        assert isinstance(s, Style)
        assert str(s) == "\033[38;2;0;0;0m"

    def test_from_rgb_2(self):
        s = Style.from_rgb(255, 127, 0)

        assert isinstance(s, Style)
        assert str(s) == "\033[38;2;255;127;0m"

    def test_from_rgb_t_1(self):
        s = Style.from_rgb_t((255, 127, 0))

        assert isinstance(s, Style)
        assert str(s) == "\033[38;2;255;127;0m"

    def test_from_rgb_t_2(self):
        s = Style.from_rgb_t((0, 0, 0))

        assert isinstance(s, Style)
        assert str(s) == "\033[38;2;0;0;0m"

    def test_from_hex(self):
        s = Style.from_hex("#FFFFFF")

        assert isinstance(s, Style)
        assert str(s) == "\033[38;2;255;255;255m"

    def test_hex_to_rgb_1(self):
        assert Style.hex_to_rgb("#FFFFFF") == (255, 255, 255)

    def test_hex_to_rgb_2(self):
        assert Style.hex_to_rgb("#FFD1DC") == (255, 209, 220)

    def test_st_print_default(self):
        with redirect_stdout(StringIO()) as buf:
            Style.st_print("123")

        assert buf.getvalue() == "123\033[0m\n"

    def test_st_print_bold(self):
        with redirect_stdout(StringIO()) as buf:
            Style.st_print("123", bold=True)

        assert buf.getvalue() == BOLD + "123" + END + "\n"
