import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun"])
    def test_buns_get_name_successfully(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_buns_get_price_successfully(self, price):
        bun = Bun("black bun", price)

        assert bun.get_price() == price