"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
	if x > 1:
		return foo(x-1) + foo(x-2)
	else:
		return x
	pass

def longest_run(mylist, key):
    ### TODO
	size = 0
	max_size = 0
	for i in range(len(mylist)):
		if (mylist[i] == key):
			size = size + 1
			if (size > max_size):
				max_size = size
		else:
			size = 0
	return max_size
	pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
	
def combine(left,right):

	if(left.is_entire_range==True and right.is_entire_range==True):
		is_total = left.left_size + right.left_size
		return Result(is_total,is_total,is_total,True)
		

	if(left.is_entire_range==True):
		total_le = left.left_size + right.left_size
		# return Result(total1,total1,total1,True)
	else:
		total_le= left.left_size
		

	if(right.is_entire_range==True):
		total_ri = left.right_size + right.left_size
		# return Result(total2,total2,total2,True)
	else:
		total_ri= right.right_size

	middle = left.right_size + right.left_size

	if middle> max(left.longest_size, right.longest_size):
		return Result(total_le, total_ri, middle, False)
	else:
		return Result(total_le, total_ri, max(left.longest_size, right.longest_size),False)

def longest_run_recursive(mylist, key):
	res = _longest_run_recursive(mylist, key)
	return res.longest_size
	
def _longest_run_recursive(mylist, key):
	### TODO
	print(mylist)
	size = len(mylist)
	if(size==1):
		if(mylist[0]==key):
			return Result(1,1,1,True)
		else:
			return Result(0,0,0,False)
	else:
		half_size = size//2
		left_part = _longest_run_recursive(mylist[:half_size],key)
		right_part = _longest_run_recursive(mylist[half_size:],key)
		return combine(left_part,right_part) 
		
	pass

	
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
	
def test_longest_run_recursive():
    assert longest_run([12,12,12,8,12,12,0,12,12,12,12], 12) == 4
    assert longest_run_recursive([2], 2) == 1
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3

