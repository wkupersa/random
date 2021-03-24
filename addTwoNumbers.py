
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def mklist(self, integer):
        headNode = node = ListNode()
        intlen = len(str(integer))
        # pass in a node
        # therte will always be at least one digit
        # head node remains pointes at first node
        for i in str(integer)[::-1]:
            intlen -= 1
            node.val = i
            if intlen > 0:
                node.next = ListNode()
                node = node.next
        return headNode
            
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        multiplier = 1
        register = 0 
        while (l1 and l2):
            register += ((int(l1.val) * multiplier) + (int(l2.val) * multiplier))
            multiplier *= 10
            l1 = l1.next
            l2 = l2.next
        #remaining digits
        i = None
        if(l1):
            i = l1
        elif(l2):
            i = l2
        else:
            return self.mklist(register)
            
        while i:
            register += (int(i.val) *multiplier)
            multiplier *= 10
            i = i.next
            
        return self.mklist(register)  


test = Solution()


input1 = test.mklist(235)
input2 = test.mklist(1000)
answer = test.addTwoNumbers(l1=input1, l2=input2)
print(answer)


