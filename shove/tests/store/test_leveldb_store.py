## -*- coding: utf-8 -*-
#
#from stuf.six import unittest
#
#
#@unittest.skipIf(PY3, 'Python 3')
#class TestLevelDBStore(unittest.TestCase):
#
#    def setUp(self):
#        from shove import Shove
#        self.store = Shove('leveldb://test', compress=True)
#
#    def tearDown(self):
#        import shutil
#        shutil.rmtree('test')
#
#    def test__getitem__(self):
#        self.store['max'] = 3
#        self.assertEqual(self.store['max'], 3)
#
#    def test__setitem__(self):
#        self.store['max'] = 3
#        self.assertEqual(self.store['max'], 3)
#
#    def test__delitem__(self):
#        self.store['max'] = 3
#        del self.store['max']
#        self.assertEqual('max' in self.store, False)
#
#    def test_get(self):
#        self.store['max'] = 3
#        self.assertEqual(self.store.get('min'), None)
#
#    def test__cmp__(self):
#        from shove import Shove
#        tstore = Shove()
#        self.store['max'] = 3
#        tstore['max'] = 3
#        self.assertEqual(self.store, tstore)
#
#    def test__len__(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.assertEqual(len(self.store), 2)
#
#    def test_close(self):
#        self.store.close()
#        self.assertEqual(self.store, None)
#
#    def test_clear(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        self.store.clear()
#        self.assertEqual(len(self.store), 0)
#
#    def test_items(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        slist = list(self.store.items())
#        self.assertEqual(('min', 6) in slist, True)
#
#    def test_keys(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        slist = list(self.store.keys())
#        self.assertEqual('min' in slist, True)
#
#    def test_values(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        slist = list(self.store.values())
#        self.assertEqual(6 in slist, True)
#
#    def test_pop(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        item = self.store.pop('min')
#        self.assertEqual(item, 6)
#
#    def test_popitem(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        item = self.store.popitem()
#        self.assertEqual(len(item) + len(self.store), 4)
#
#    def test_setdefault(self):
#        self.store['max'] = 3
#        self.store['min'] = 6
#        self.store['pow'] = 7
#        self.store.setdefault('bow', 8)
#        self.assertEqual(self.store['bow'], 8)
#
#    def test_update(self):
#        from shove import Shove
#        tstore = Shove()
#        tstore['max'] = 3
#        tstore['min'] = 6
#        tstore['pow'] = 7
#        self.store['max'] = 2
#        self.store['min'] = 3
#        self.store['pow'] = 7
#        self.store.update(tstore)
#        self.assertEqual(self.store['min'], 6)
#
#
#if __name__ == '__main__':
#    unittest.main()
