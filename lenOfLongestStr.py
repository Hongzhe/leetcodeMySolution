def lengthOfLongestSubstring(s):
	p1 = p2 = 0
	length = 0
	l = len(s)
	visisted = {}
	while(p1 != l):
		if visisted.get(s[p1]) == None:
			visisted[s[p1]] = -1
		if visisted.get(s[p1]) > -1:
			lh = p1 - p2
			if lh > length:
				length = lh
			if p2 <= visisted[s[p1]]:
				p2 = visisted[s[p1]] + 1

		visisted[s[p1]] = p1;
		p1+=1
	if p1 - p2 > length:
		length = p1 - p2
	return length


s = 'aa'
r = lengthOfLongestSubstring(s)
print(r)