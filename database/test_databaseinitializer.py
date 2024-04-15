from unittest import TestCase
from unittest.mock import MagicMock
import os
from database.databaseinitializer import Databaseinitializer


class TestDatabaseinitializer(TestCase):

    def setUp(self):
        mock_app = MagicMock()
        mock_app.__getitem__.side_effect = lambda x: x  # Mock the dictionary get item behavior
        self.db = Databaseinitializer(mock_app)
    def test_initialize_table(self):
        self.fail()

    def test_write_data_to_table(self):
        print(os.getcwd())
        self.db.write_data_to_table("static/problemRating.json", "problemRating" )


    def test_create_table(self):
        self.fail()
