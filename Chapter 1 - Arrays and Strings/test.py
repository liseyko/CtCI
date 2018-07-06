import unittest
import importlib
from random import randint

sol = {}
for i in range(1,7):
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
    def setUp(self):
        self.strings_perm = ["abcd", "cbda","dabc"]
        self.strings_notperm = ["abkd" ,"abdce", "", "a"]

    def test_1_perm(self):
        for s1 in self.strings_perm:
            for s2 in self.strings_perm:
                self.assertTrue(sol[103].check_permutation1(s1,s2))
    def test_1_notperm(self):
        for s1 in self.strings_notperm + self.strings_perm:
            for s2 in self.strings_notperm:
                if s1 == s2:
                    continue
                self.assertFalse(sol[103].check_permutation1(s1,s2))

class S0104TestCase(unittest.TestCase):
    """Tests for: replace"""
    def test_1_check_converted_strings(self):
        input_strings=["Mr John Smith"," ","a ","   ","abc"]
        expected_results=["Mr%20John%20Smith","%20","a%20","%20%20%20","abc"]
        for i in range(len(input_strings)):
            result = sol[104].replace(input_strings[i])
            self.assertEqual(result,expected_results[i])

class S0105TestCase(unittest.TestCase):
    """Test for: s_compress"""
    def setUp(self):
        self.in_strings = ["aabcccccaaa","abbc","abbccc","xxxxxxxXyyyyyYzzzzzzZ","aaaaaaaaffffffffffffffffffdffffffffffffffffffffggggggggggggggggrttttttttttttttttttttttttttttgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggssssssssssssdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"]
        self.expected_results = ["a2b1c5a3","abbc","abbccc","x7X1y5Y1z6Z1","a8f18d1f20g16r1t28g77s12d7f111d261"]

    def test_1(self):
        for i in range(len(self.in_strings)):
            result = sol[105].s_compress(self.in_strings[i])
            self.assertEqual(result,self.expected_results[i])

class S0106TestCase(unittest.TestCase):
    """Test for: init_matrix, rotate_naive, rotate"""
    def setUp(self):
        self.testdata = [ \
[['00', '01', '02', '03', '04'], ['10', '11', '12', '13', '14'], ['20', '21', '22', '23', '24'], ['30', '31', '32', '33', '34'], ['40', '41', '42', '43', '44'], ['50', '51', '52', '53', '54'], ['60', '61', '62', '63', '64'], ['70', '71', '72', '73', '74']],\
[['70', '60', '50', '40', '30', '20', '10', '00'], ['71', '61', '51', '41', '31', '21', '11', '01'], ['72', '62', '52', '42', '32', '22', '12', '02'], ['73', '63', '53', '43', '33', '23', '13', '03'], ['74', '64', '54', '44', '34', '24', '14', '04']],\
[['74', '73', '72', '71', '70'], ['64', '63', '62', '61', '60'], ['54', '53', '52', '51', '50'], ['44', '43', '42', '41', '40'], ['34', '33', '32', '31', '30'], ['24', '23', '22', '21', '20'], ['14', '13', '12', '11', '10'], ['04', '03', '02', '01', '00']],\
[['04', '14', '24', '34', '44', '54', '64', '74'], ['03', '13', '23', '33', '43', '53', '63', '73'], ['02', '12', '22', '32', '42', '52', '62', '72'], ['01', '11', '21', '31', '41', '51', '61', '71'], ['00', '10', '20', '30', '40', '50', '60', '70']]]
        self.img = sol[106].init_matrix(5,8)

    def test_1_init_matrix(self):
        self.assertEqual(self.img,self.testdata[0])
        self.assertFalse(sol[106].init_matrix(0,1))
        self.assertFalse(sol[106].init_matrix(2,0))

    def test_2_rotate_naive(self):
        self.assertEqual(sol[106].rotate_naive(self.img),self.testdata[1])

    def test_3_rotate(self):
        for i in range(1,4):
            self.assertEqual(sol[106].rotate(self.img),self.testdata[i])

    def test_4_init_random_and_rotate(self):
        for _ in range(100):
            img = sol[106].init_matrix(randint(2,64),randint(2,64))
            self.assertEqual(sol[106].rotate_naive(img),sol[106].rotate(img))
            self.assertEqual(sol[106].rotate_naive(img),sol[106].rotate(img))


unittest.main()