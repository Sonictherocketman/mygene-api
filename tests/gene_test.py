""" Tests for the genes module. """

import unittest
import sys

sys.path.insert(0, '../')
from mygene.gene import Gene


class GeneTest(unittest.TestCase):

    def test_find_by(self):
        res = Gene.find_by(q='chr1:69000-70000')
        self.assertEqual(len(res), 1)
        for r in res:
            self.assertEqual(r.symbol, 'OR4F5')

    def test_find_multiple_by(self):
        ids = ','.join(['1017', '1018'])
        res = Gene.find_multiple_by(q=ids)
        for r in res:
            self.assertTrue(r._id in ids)

    def test_get(self):
        res = Gene.get('1017')
        self.assertTrue(res is not None)
        self.assertEqual(res.ec, '2.7.11.22')

    def test_get_multiple(self):
        ids = ','.join(['1017', '1018'])
        res = Gene.get_multiple(ids=ids)
        self.assertTrue(res is not None)
        for r in res:
            self.assertTrue(r._id in ids)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GeneTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
