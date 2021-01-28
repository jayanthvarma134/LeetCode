# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_vals(self, object):
        if(object and object.val):
            return object.val
        else:
            return 0
    
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
        l3=None
        L1_tail = l1
        L2_tail = l2
        carry = 0
        while L1_tail or L2_tail or carry :
            val1 = self.get_vals(L1_tail)
            val2 = self.get_vals(L2_tail)
            node = ListNode()
            l3_tail = None
            val = val1 + val2 + carry
            carry,node.val = divmod(val, 10)
            if not l3:
                l3 = node
            else:
                l3_tail.next = node

            l3_tail = node
            if((L1_tail and L1_tail.next) or (L2_tail and L2_tail.next)):
                L1_tail= L1_tail.next
                L2_tail = L2_tail.next
            else:
                L1_tail= None
                L2_tail = None
                
        return l3