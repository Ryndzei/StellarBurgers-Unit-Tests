from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_successfully(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun

    def test_add_ingredient_successfully(self):
        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100

        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_successfully(self):
        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_successfully(self):
        burger = Burger()

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_first_ingredient.get_name.return_value = "hot sauce"
        mock_first_ingredient.get_price.return_value = 100

        mock_second_ingredient = Mock()
        mock_second_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_second_ingredient.get_name.return_value = "dinosaur"
        mock_second_ingredient.get_price.return_value = 200

        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_second_ingredient, mock_first_ingredient]

    def test_get_burger_price_successfully(self):
        burger = Burger()

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_first_ingredient.get_name.return_value = "hot sauce"
        mock_first_ingredient.get_price.return_value = 100

        mock_second_ingredient = Mock()
        mock_second_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_second_ingredient.get_name.return_value = "dinosaur"
        mock_second_ingredient.get_price.return_value = 200

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        burger.bun = mock_bun
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert burger.get_price() == 500

    def test_get_burger_receipt_successfully(self):
        burger = Burger()

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_first_ingredient.get_name.return_value = "hot sauce"
        mock_first_ingredient.get_price.return_value = 100

        mock_second_ingredient = Mock()
        mock_second_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_second_ingredient.get_name.return_value = "dinosaur"
        mock_second_ingredient.get_price.return_value = 200

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        burger.bun = mock_bun
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        expected_receipt = (
            '(==== black bun ====)\n'
            f'= sauce hot sauce =\n'
            f'= filling dinosaur =\n'
            '(==== black bun ====)\n\n'

            'Price: 500'
        )

        assert burger.get_receipt() == expected_receipt
