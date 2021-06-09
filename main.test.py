# coding:utf-8
import unittest
from main import Main

from unittest.mock import patch


class TestMain(unittest.TestCase):
  def setUp(self):
    self.main = Main()

  @patch('builtins.print')
  def test_printHelloWord(self, mock_print):
    self.main.printHelloWord()
    mock_print.assert_called_with("Sou UFABC!\n")
  
  
if __name__ == '__main__':
  unittest.main()
