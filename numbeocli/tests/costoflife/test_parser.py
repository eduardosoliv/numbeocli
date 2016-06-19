import os
from numbeocli.costoflife import parser

class TestParser:
    def test_indices_london_berlin_2016_06_19(self):
        input_path = os.path.dirname(os.path.abspath(__file__)) + "/inputs/london-berlin-2016-06-19.html"
        with open(input_path, 'r') as content_file:
            content = content_file.read()
        p = parser.Parser(content)
        assert p.indices_diff() == [
            {'category': 'Consumer Prices', 'percentage': 28.72, 'diff_type': 'lower'},
            {'category': 'Consumer Prices Including Rent', 'percentage': 46.17, 'diff_type': 'lower'},
            {'category': 'Rent Prices', 'percentage': 67.66, 'diff_type': 'lower'},
            {'category': 'Restaurant Prices', 'percentage': 42.33, 'diff_type': 'lower'},
            {'category': 'Groceries Prices', 'percentage': 23.08, 'diff_type': 'lower'},
            {'category': 'Local Purchasing Power', 'percentage': 40.53, 'diff_type': 'higher'}
        ]

    def test_indices_berlin_london_2016_06_19(self):
        input_path = os.path.dirname(os.path.abspath(__file__)) + "/inputs/berlin-london-2016-06-19.html"
        with open(input_path, 'r') as content_file:
            content = content_file.read()
        p = parser.Parser(content)
        assert p.indices_diff() == [
            {'category': 'Consumer Prices', 'percentage': 40.29, 'diff_type': 'higher'},
            {'category': 'Consumer Prices Including Rent', 'percentage': 85.77, 'diff_type': 'higher'},
            {'category': 'Rent Prices', 'percentage': 209.24, 'diff_type': 'higher'},
            {'category': 'Restaurant Prices', 'percentage': 73.39, 'diff_type': 'higher'},
            {'category': 'Groceries Prices', 'percentage': 30.00, 'diff_type': 'higher'},
            {'category': 'Local Purchasing Power', 'percentage': 28.84, 'diff_type': 'lower'}
        ]

    def test_indices_unrecognized_cities_2016_06_19(self):
        input_path = os.path.dirname(os.path.abspath(__file__)) + "/inputs/no-city-on-db-2016-06-19.html"
        with open(input_path, 'r') as content_file:
            content = content_file.read()
        p = parser.Parser(content)
        assert p.indices_diff() == []
