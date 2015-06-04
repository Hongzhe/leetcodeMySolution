class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

#given a linked list, remove the nth node 
#from the end of list and return its head
def removeNthFromEnd(head, n):
	p1 = p2 = head
	for i in range(n):
		p1 = p1.next
	if not p1:
		head = head.next
	else:
		while p1.next:
			p1 = p1.next
			p2 = p2.next
		p2.next = p2.next.next
	return head



