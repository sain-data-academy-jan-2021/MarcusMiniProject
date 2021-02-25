import os
import unittest
from unittest.mock import patch, Mock
from modules.menus import MainMenuChoice
from modules.courier_functions import GetCourierID

class TestMenus(unittest.TestCase):
    @patch("modules.menus.DrawMainMenu")
    @patch("builtins.input")
    def test_main_menu_choice_correct_value(self, mock_input, mock_DrawMainMenu):
        mock_DrawMainMenu.return_value = None
        mock_input.return_value = "1"
        expected = "1"
        actual = MainMenuChoice()
        self.assertEqual(actual, expected)
    
    @patch("modules.menus.DrawMainMenu")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_main_menu_choice_incorect_menu_number(self, mock_print, mock_input, mock_DrawMainMenu):
        mock_DrawMainMenu.return_value = None
        mock_input.side_effect = ["5", "1"]
        mock_print.return_value = None
        expected = "1"
        actual = MainMenuChoice()
        self.assertEqual(actual, expected)

class TestCourier_functions(unittest.TestCase):
    @patch("modules.courier_functions.DBSelect")
    @patch("modules.courier_functions.PrintTable")
    @patch("builtins.input")
    def test_get_courier_id_correct_value(self, mock_input, mock_PrintTable, mock_DBSelect):
        mock_DBSelect.return_value = (((1,), (2,), (3,)), (('courier_id', 3, None, 11, 11, 0, False),))
        mock_PrintTable.return_value = None
        mock_input.return_value = 1
        expected = 1
        actual = GetCourierID(None)
        self.assertEqual(actual, expected)
        
    @patch("modules.courier_functions.DBSelect")
    @patch("modules.courier_functions.PrintTable")
    @patch("builtins.input")
    def test_get_courier_id_incorrect_value(self, mock_input, mock_PrintTable, mock_DBSelect):
        mock_DBSelect.return_value = (((1,), (2,), (3,)), (('courier_id', 3, None, 11, 11, 0, False),))
        mock_PrintTable.return_value = None
        mock_input.side_effect = ["5", "1"]
        expected = "1"
        actual = GetCourierID(None)
        self.assertEqual(actual, expected)
    
    @patch("builtins.input")
    def test_NewDBCourier_with_correct_value(self, mock_input):
    mock_input.side_effect = ["john", "trycycle"]
    
    
        
if __name__ == "__main__":
    unittest.main()
