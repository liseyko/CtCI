""" is linked list a palindrome """

from linkedlist import LinkedList

def isLLaPalindrome_naive(ll):
    """reverse and compare 1/2"""
    ll2 = LinkedList()
    q = 0
    for n in ll:
        ll2.insert(n.data)
        q += 1
    q = q // 2
    n1 = ll.head
    n2 = ll2.head
    while n1.data == n2.data:
        if not n1.next or q == 1:
            return True
        n1 = n1.next
        n2 = n2.next
        q -= 1
    return False

def isLLaPalindrome_rec(ll):
    """ TODO: check only half of the list """
    rw_n = ll.head
    fw_n = rw_n
    l = ll.len

    def rec(rw_n,fw_n,l):
        if rw_n.next:
            fw_n = rec(rw_n.next,fw_n,l-2)
            if not fw_n or not rw_n.data == fw_n.data:
                return False
            #print(rw_n.data,fw_n.data)
        else:
            if not rw_n.data == fw_n.data:
                return False
            #print(rw_n.data,fw_n.data)
        if not fw_n.next:
            return True
        return fw_n.next

    print(rec(rw_n,fw_n,l))
    return False

def isLLaPalindrome(ll):
    stack = LinkedList()
    fast = ll.head
    slow = fast

    while fast and fast.next:
        stack.insert(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    if fast is not None: # skip middle element if odd len
        slow = slow.next

    fast = stack.head
    while slow:
        if slow.data != fast.data:
            return False
        slow = slow.next
        fast = fast.next
    return True


test1 = LinkedList([c for c in "never odd or even".replace(" ", "")])
test2 = LinkedList([c for c in "mr owl ate my metal worm".replace(" ", "")])
print(isLLaPalindrome_naive(test1))
print(isLLaPalindrome_naive(test2))
print("recursive:")
isLLaPalindrome_rec(test1)
isLLaPalindrome_rec(test2)
print("iterative:")
print(isLLaPalindrome(test1))
print(isLLaPalindrome(test2))
