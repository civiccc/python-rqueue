import unittest2 as unittest
from basic import QueueTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QueueTestCase))
    return suite