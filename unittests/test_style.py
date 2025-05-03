from contextlib import redirect_stdout
from io import StringIO

from style import Style, BOLD, END


class TestStyle:
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
