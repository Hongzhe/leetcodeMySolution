#check whether paranthess are closed propely
def isValid(s):
	prefix = {'{':0, '[':1, '(':2}
	postfix = ['}', ']', ')']
	index = 0
	l = len(s)
	stack = []
	first = True
	while index < l:
		c = s[index]
		i = prefix.get(c, -1)
		if i > -1:
			stack.append(postfix[i])
		else:
			 l = len(stack)
			 if l == 0 :
			 	return False
			 elif stack.pop() != c:
			 	return False
		index += 1
	if len(stack) != 0:
		return False
	return True



s = "()[]{}"
print(isValid(s))

s1 = "("
print(isValid(s1))