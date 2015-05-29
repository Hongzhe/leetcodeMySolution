#merge two sorted singlly 	linked list
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


def mergeTwoLists(l1, l2):
	p1 = l1
	p2 = l2
	merge = temp = None
	while p1 != None and p2 != None:
		cur = None
		if p1.val < p2.val:
			cur = p1
			p1 = p1.next
		else:
			cur = p2
			p2 = p2.next
		if merge == None:
			merge = temp = ListNode(cur.val)
		else:
			temp.next = ListNode(cur.val)
			temp = temp.next
	
	while p1 != None:
		temp.next = ListNode(p1.val)
		p1 = p1.next
		temp = temp.next
	while p2 != None:
		temp.next = ListNode(p2.val)
		p2 = p2.next
		temp = temp.next
	return merge

