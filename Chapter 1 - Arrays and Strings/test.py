import unittest
import importlib

sol = {}
for i in range(1,4):
    sol[100+i] = importlib.import_module('s010'+str(i), package=None)


class S0101TestCase(unittest.TestCase):
    """ Tests for: isUniqueA, isUniqueB """
    def test_1_uniq(self):
        """Check unique string."""
        strings = ['Abc123,./=-0jkf','']
        for s in strings:
            result = sol[101].isUniqueA(s)
            self.assertTrue(result)
            result = sol[101].isUniqueB(s)
            self.assertTrue(result)

    def test_2_nonuniq(self):
        """Check non-unique string."""
        strings = ['Abc123,./=-03jkf','  ']
        for s in strings:
            result = sol[101].isUniqueA(s)
            self.assertFalse(result)
            result = sol[101].isUniqueB(s)
            self.assertFalse(result)


class S0102TestCase(unittest.TestCase):
    """Tests for: reverse"""
    def test_1_reverse(self):
        input_str = "Implement a function in C/C++ to reverse a null terminated string."
        result = sol[102].reverse(input_str)
        expected_result = ".gnirts detanimret llun a esreve rot ++C/C ni noitcnuf a tnemelpmI"
        self.assertEqual(result, expected_result)

    def test_1_not_reverse(self):
        input_str = "Implement a function in C/C++ to reverse a null terminated string."
        result = sol[102].reverse(input_str)
        expected_result = ".gnirts detanimret llun a esreve rot ++C/C ni noitcnuf a tnemelpmI "
        self.assertNotEqual(result, expected_result)


class S0103TestCase(unittest.TestCase):
    """Tests for: check_permutation0, check_permutation1"""
    def test_1_perm(self):
        strings_perm = ["abcd", "cbda","dabc"]
        for s1 in strings_perm:
            for s2 in strings_perm:
                self.assertTrue(sol[103].check_permutation1(s1,s2))
    def test_1_notperm(self):
        strings_notperm = ["abcd","abkd" ,"abdce", "", "a"]
        for s1 in strings_notperm:
            for s2 in strings_notperm:
                if s1 == s2:
                    continue
                self.assertFalse(sol[103].check_permutation1(s1,s2))


unittest.main()