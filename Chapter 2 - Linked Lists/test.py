import unittest

from linkedlist import LinkedList

class Test_LinkedList(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_1_insert(self):
        ll =LinkedList()
        for i in range(10):
            ll.insert(i)
        tn = ll.head
        for i in range(9,-1,-1):
            self.assertEqual(i,tn.data)
            tn = tn.next
        test_data = ["test",""]
        for d in test_data:
            ll.insert(d)
            self.assertEqual(d,ll.head.data)
        
    def test_1_append(self):
        ll =LinkedList()
        for i in range(10):
            ll.append(i)
        tn = ll.head
        for i in range(10):
            self.assertEqual(i,tn.data)
            tn = tn.next


unittest.main()