#Given an array of integers, find two numbers such that they add up to a specific target number.
def twoSum(nums, target):
    visited = {}
    for j, val in enumerate(nums, 1):
	    i = visited.get(target - val, -1)
	    if i > 0:
	        return [i, j]
	    visited[val] = j