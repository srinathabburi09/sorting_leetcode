# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:      #if not head or only one node present we will be return head
            return head

        slow = head          # 2 - pointer approach slow will be at head and to get first middle for even length LL and to get for od length LL
        fast = head.next        #so we are setting fast at a pointer ahead slow during intialization

        while fast and fast.next:      #until the fast becomes None and Fast.next becomes none
            slow = slow.next            #slow will be moving 1 step forward
            fast = fast.next.next        #fast will be moving 2 steps a head

        middle = slow                    #by that middle will be at the slow pointer
        slow.next = None        #this breaks the list and immediately we point the middle.next points to None

        left = self.sortList(head)        #This is a recursive call so left will be starts from head to middle
        right = self.sortList(middle)      #and this also a recurive call it will be starts at middle to last node 
        return self.merge(left,right)

    def merge(self,left, right):
        dummy = ListNode()      #to track tail and to set all the node sorted and dummy will be at None
        tail = dummy            #tail will be set as dummy
        while left and right:        
            if left.val < right.val:    #if left.val < right.val  tail.next that is tail pointer will be at left and left will be updated to left .next
                tail.next = left       #and as well as tail will be updated as well,that is basically tail.next will be at left and left.next will be at pointing to next node    
                left = left.next
            else:
                tail.next = right        #same as the above iteration but vice versa
                right = right.next
            tail = tail.next

        tail.next = left if left else right     #for single node basically the first step in a recurive call
        return dummy.next                    #we return dummy.next
    
