class Solution:
    def pairSum(self, head):
        # Step 1: Find middle of linked list
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Find maximum twin sum
        max_sum = 0
        first = head
        second = prev
        
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum
