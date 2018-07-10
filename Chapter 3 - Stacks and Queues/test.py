import unittest
import importlib
import random
#import string

sol = {}
for i in [3,4,5]:
    sol[300+i] = importlib.import_module('s030'+str(i), package=None)


class S0103TestCase(unittest.TestCase):
    """ Tests for: SetOfStacks class with methods: push, pop, popAt"""
    def setUp(self):
        pass
  
    def test_push_and_pop(self):
        ss = sol[303].SetOfStacks()
        for i in range(14):
            ss.push(i)
        for _ in range(10):
            ss.pop()
        for i in range(15):
            ss.push(i)
        self.assertEqual(str(ss.stacks[0]),'[3, 2, 1, 0, 3, 2, 1, 0]')
        for _ in range(7):
            ss.popAt(1)
        self.assertEqual(str(ss.stacks[1]),'[4]')            
        for _ in range(6):
            ss.pop()
        testdata = [1, 0, 3, 2, 1, 0]
        self.assertEqual(str(ss.stacks[0]),str(testdata))            
        for i in range(6):
            self.assertEqual(ss.pop(),testdata[i])
        self.assertFalse(ss.pop())
        self.assertEqual(str(ss.stacks[0]),'[]')
        ss.push(1)
        self.assertEqual(ss.pop(),1)

    def test_shrinking(self):
        ss = sol[303].SetOfStacks()
        expected_results = [[9, 8, 5, 4, 3, 2, 1, 0], \
                    [19, 18, 17, 16, 13, 12, 11, 10], \
                    [29, 28, 27, 26, 25, 24, 21, 20], \
                    [41, 40, 37, 36, 35, 34, 33, 32], \
                    [51, 50, 49, 48, 45, 44, 43, 42], \
                    [61, 60, 59, 58, 57, 56, 53, 52]]
        for i in range(64):
            ss.push(i)
        for i in range(8):
            ss.popAt(i)
            ss.popAt(i)
        ss.shrink()
        for i in range(len(ss.stacks)):
            self.assertEqual(str(ss.stacks[i]),str(expected_results[i]))

    def test_auto_shrinking(self):
        ss = sol[303].SetOfStacks()
        for i in range(64):
            ss.push(i)
        for i in range(8):
            ss.popAt(i)
            ss.popAt(i)
            ss.popAt(i)
        for i in range(len(ss.stacks)):
            self.assertEqual(str(ss.stacks[5]),"[63, 62, 61, 60, 59, 58]")

class S0304TestCase(unittest.TestCase):
    "Tests for: hanoi.move, hanoi.iterSol"
    def test_0_init(self):
        for i in range(1,8):
            ht = sol[304].Hanoi(i)
            self.assertEqual("['" + str([j for j in range(1,i+1)]) +"', '[]', '[]']",str(ht))

    def test_1_recursive_solution(self): 
        for i in range(1,8):
            ht = sol[304].Hanoi(i)
            ht.move(0,2)
            self.assertEqual("['[]', '[]', '" + str([j for j in range(1,i+1)]) + "']",str(ht))

    def test_1_iterative_solution(self): 
        for i in range(1,8):
            ht = sol[304].Hanoi(i)
            ht.iterSol(0,2)
            self.assertEqual("['[]', '[]', '" + str([j for j in range(1,i+1)]) + "']",str(ht))

class S0305TestCase(unittest.TestCase):
    """Tests for: push, pop, peek"""
    def test_all_in_one(self):
        rq = sol[305].Queue()
        q = sol[305].MyQueue()
        
        for i in range(100):
            if random.random() < 0.6:
                rq.enqueue(i)
                q.enqueue(i)
            else:
                self.assertEqual(q.dequeue(),rq.dequeue())


unittest.main()