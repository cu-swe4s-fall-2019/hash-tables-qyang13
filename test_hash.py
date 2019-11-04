import unittest
import os
import hash_tables as ht
import hash_functions as hf


class TestHashFunction(unittest.TestCase):
    '''
    Unit test for hash_functions
    '''
    def test_h_ascii(self):
        self.assertEqual(hf.h_ascii('test', 500), 448)

    def test_h_rolling(self):
        self.assertEqual(hf.h_rolling('test', 500), 236)

    def test_h_sedgwicks(self):
        self.assertEqual(hf.h_sedgwicks('test', 500), 76)


class TestHashTables(unittest.TestCase):
    '''
    Unit test for hash_tables, using newly implemented sedgwicks hash algorithm
    '''
    def test_linear_probing(self):
        test_case = ht.LinearProbe(500, hf.h_sedgwicks)
        # Testing add
        self.assertEqual(test_case.add('key', 'value'), True)
        # Testing search
        self.assertEqual(test_case.search('key'), 'value')
        # Testing search not exist
        self.assertEqual(test_case.search('wrong_key'), None)

    def test_chained_hash(self):
        test_case = ht.ChainHashTable(500, hf.h_sedgwicks)
        # Testing add
        self.assertEqual(test_case.add('key', 'value'), True)
        # Testing search
        self.assertEqual(test_case.search('key')[0], 'value')
        # Testing search not exist
        self.assertEqual(test_case.search('wrong_key'), None)

    def test_quadratic_probing(self):
        test_case = ht.QuadraticProbing(500, hf.h_sedgwicks)
        # Testing add
        self.assertEqual(test_case.add('key', 'value'), True)
        # Testing search
        self.assertEqual(test_case.search('key'), 'value')
        # Testing search not exist
        self.assertEqual(test_case.search('wrong_key'), None)


if __name__ == '__main__':
    unittest.main()
