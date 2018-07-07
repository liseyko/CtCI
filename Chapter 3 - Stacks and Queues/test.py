import unittest
import importlib
import random
#import string

sol = {}
for i in [3]:
    sol[300+i] = importlib.import_module('s030'+str(i), package=None)


class S0103TestCase(unittest.TestCase):
    """ Tests for: SetOfStacks class with methods: push, pop, popAt"""
    def setUp(self):
        self.ss = sol[303].SetOfStacks()
        for i in range(14):
            self.ss.push(i)
        for _ in range(10):
            self.ss.pop()
        for i in range(15):
            self.ss.push(i)

    def test_push_and_pop(self):
        self.assertEqual(str(self.ss.stacks[0]),'[3, 2, 1, 0, 3, 2, 1, 0]')
        for _ in range(7):
            self.ss.popAt(1)
        self.assertEqual(str(self.ss.stacks[1]),'[4]')            
        for _ in range(6):
            self.ss.pop()
        testdata = [1, 0, 3, 2, 1, 0]
        self.assertEqual(str(self.ss.stacks[0]),str(testdata))            
        for i in range(6):
            self.assertEqual(self.ss.pop(),testdata[i])
        self.assertFalse(self.ss.pop())
        self.assertEqual(str(self.ss.stacks[0]),'[]')
        self.ss.push(1)
        self.assertEqual(self.ss.pop(),1)

unittest.main()