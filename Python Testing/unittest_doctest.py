# unittest_doctest.py
import unittest
import doctest
import doctest_fibonacci


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(doctest_fibonacci))
    return tests
