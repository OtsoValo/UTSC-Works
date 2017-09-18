import unittest
import squeal
from database import Table


class TestCartesianProduct(unittest.TestCase):

    def test_01_blank_tables(self):
        # start with two tables that will be empty
        t1 = Table()
        t2 = Table()
        # the result of the cartesian product of two empty tables
        # should iteslf be an empty table
        result = squeal.cartesian_product(t1, t2)
        # we'll know it's an empty table if its dictionary is empty
        result_dict = result.get_dict()
        expected = {}
        self.assertEqual(result_dict, expected,
                         "product of two empty tables should be empty")

    def test_02_blank_table_first(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set table 1
        table_1.set_dict({'t1.title': ['CSCA', '08']})
        # the result should return 0 row, and titles of t1
        result = squeal.cartesian_product(table_1, table_2)
        # we'll know it's an empty table if its dictionary is empty
        # but t1 has title, so we should return its title
        result_dict = result.get_dict()
        expected = {'t1.title': []}
        self.assertEqual(result_dict, expected,
                         '''if one table is empty, result should be empty,
                         and return another tables' title''')

    def test_03_blank_table_second(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set table 2
        table_2.set_dict({'t2.title': ['CSCA', '08']})
        # the result should return 0 row, and titles of t2
        result = squeal.cartesian_product(table_1, table_2)
        # we'll know it's an empty table if its dictionary is empty
        # but t2 has title, so we should return its title
        result_dict = result.get_dict()
        expected = {'t2.title': []}
        self.assertEqual(result_dict, expected,
                         '''if one table is empty, result should be empty,
                         and return another tables' title''')

    def test_04_blank_row_first(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # table 2 has no row only titles, but table 1 has
        table_1.set_dict({'t1.title': ['CSCA', '08']})
        table_2.set_dict({'t2.title': []})
        # the result of the cartesian product of a table without any row
        # it should return no row
        result = squeal.cartesian_product(table_1, table_2)
        # if there is no row for one table, then result should be no row
        result_dict = result.get_dict()
        expected = {'t2.title': [], 't1.title': []}
        self.assertEqual(result_dict, expected,
                         '''if one table has no row, product should be empty,
                         but it has all the title names''')

    def test_04_blank_row_second(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # table 1 has no row only titles, but table 2 has
        table_1.set_dict({'t1.title': []})
        table_2.set_dict({'t2.title': ['CSCA', '08']})
        # the result of the cartesian product of a table without any row
        # it should return no row
        result = squeal.cartesian_product(table_1, table_2)
        # if there is no row for one table, then result should be no row
        result_dict = result.get_dict()
        expected = {'t2.title': [], 't1.title': []}
        self.assertEqual(result_dict, expected,
                         '''if one table has no row, product should be empty,
                         but it has all the title names''')

    def test_06_two_blank_rows(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # two tables both have no row
        table_1.set_dict({'t1.title': []})
        table_2.set_dict({'t2.title': []})
        # the result of the cartesian product of a table without any row
        # it should return no row
        result = squeal.cartesian_product(table_1, table_2)
        # if there is no row for one table, then result should be no row
        result_dict = result.get_dict()
        expected = {'t2.title': [], 't1.title': []}
        self.assertEqual(result_dict, expected,
                         '''if two tables has no row, then there is no row
                         to return but title names''')

    def test_07_normal_cases(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set two tables
        table_1.set_dict({'CSC': ['A08', 'A67'], 'MAT': ['A31', 'A23']})
        table_2.set_dict({'c.A08': ['term work', 'term tests', 'final']})
        result = squeal.cartesian_product(table_1, table_2)
        # get the result dict of cartesian product
        result_dict = result.get_dict()
        expected = {'MAT': ['A31', 'A31', 'A31', 'A23', 'A23', 'A23'],
                    'c.A08': ['term work', 'term tests', 'final', 'term work',
                              'term tests', 'final'],
                    'CSC': ['A08', 'A08', 'A08', 'A67', 'A67', 'A67']}
        self.assertEqual(result_dict, expected,
                         '''your cartesian product must get something
                         wrong''')

    def test_08_normal_test(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set two tables
        table_1.set_dict({'m.A31': ['homework', 'midterm', 'final']})
        table_2.set_dict({'c.A08': ['term work', 'term tests', 'final']})
        result = squeal.cartesian_product(table_1, table_2)
        # get the result dict of cartesian product
        result_dict = result.get_dict()
        expected = {'m.A31': ['homework', 'homework', 'homework', 'midterm',
                              'midterm', 'midterm', 'final', 'final', 'final'],
                    'c.A08': ['term work', 'term tests', 'final', 'term work',
                              'term tests', 'final', 'term work',
                              'term tests', 'final']}
        self.assertEqual(result_dict, expected,
                         '''your cartesian product must get something
                         wrong''')

    def test_09_normal_test(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set two tables
        table_1.set_dict({'m.A31': ['homework', 'midterm', 'final']})
        table_2.set_dict({'c.A08': ['term work', 'term tests', 'final']})
        result = squeal.cartesian_product(table_2, table_1)
        # get the result dict of cartesian product
        result_dict = result.get_dict()
        expected = {'m.A31': ['homework', 'midterm', 'final', 'homework',
                              'midterm', 'final', 'homework', 'midterm',
                              'final'],
                    'c.A08': ['term work', 'term work', 'term work',
                              'term tests', 'term tests', 'term tests',
                              'final', 'final', 'final']}
        self.assertEqual(result_dict, expected,
                         '''your cartesian product must get something
                         wrong''')

    def test_10_normal_test(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set two tables
        table_1.set_dict({'a': ['1', '2', '3', '4']})
        table_2.set_dict({'b': ['10', '11', '12'], 'c': ['99', '98', '97']})
        result = squeal.cartesian_product(table_1, table_2)
        # get the result dict of cartesian product
        result_dict = result.get_dict()
        expected = {'a': ['1', '1', '1', '2', '2', '2', '3', '3', '3', '4',
                          '4', '4'],
                    'b': ['10', '11', '12', '10', '11', '12', '10', '11',
                          '12', '10', '11', '12'],
                    'c': ['99', '98', '97', '99', '98', '97', '99', '98',
                          '97', '99', '98', '97']}
        self.assertEqual(result_dict, expected,
                         '''your cartesian product must get something
                         wrong''')

    def test_11_normal_test(self):
        # initialize two tables
        table_1 = Table()
        table_2 = Table()
        # set two tables
        table_1.set_dict({'a': ['1', '2', '3', '4']})
        table_2.set_dict({'b': ['10', '11', '12'], 'c': ['99', '98', '97']})
        result = squeal.cartesian_product(table_2, table_1)
        # get the result dict of cartesian product
        result_dict = result.get_dict()
        expected = {'a': ['1', '2', '3', '4', '1', '2', '3', '4', '1', '2',
                          '3', '4'],
                    'b': ['10', '10', '10', '10', '11', '11', '11', '11',
                          '12', '12', '12', '12'],
                    'c': ['99', '99', '99', '99', '98', '98', '98', '98',
                          '97', '97', '97', '97']}
        self.assertEqual(result_dict, expected,
                         '''your cartesian product must get something
                         wrong''')

if(__name__ == "__main__"):
    unittest.main(exit=False)
