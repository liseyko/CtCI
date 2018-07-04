""" is linked list a palindrome """

from linkedlist import LinkedList

def isLLaPalindrome_naive(ll):
    ll2 = LinkedList()
    for n in ll:
        ll2.insert(n.data)
    n1 = ll.head
    n2 = ll2.head
    while n1.data == n2.data:
        if not n1.next:
            return True
        n1 = n1.next
        n2 = n2.next
    return False

def isLLaPalindrome_rec(ll):
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
    rabbit = ll.head
    if rabbit:
        turtle = rabbit
    while rabbit:
        stack.insert(turtle.data)
        rabbit = rabbit.next
        if rabbit:
            rabbit = rabbit.next
            turtle = turtle.next
    #print(ll,stack,turtle.data)
    n = stack.head
    while turtle:
        if turtle.data != n.data:
            return False
        n = n.next
        turtle = turtle.next
    return True


test1 = LinkedList([c for c in "never odd or even".replace(" ", "")])
test2 = LinkedList([c for c in "mr owl ate my metal worm".replace(" ", "")])
print(isLLaPalindrome_naive(test1))
isLLaPalindrome_rec(test1)
print(isLLaPalindrome_naive(test2))
isLLaPalindrome_rec(test2)
print("iterative:")
print(isLLaPalindrome(test1))
print(isLLaPalindrome(test2))
