length={1:1,2:4,3:5,4:8,5:8,7:10}
def	max_cost(price_list,length_of_brick):
	if length_of_brick==0:
		return 0
	c=-200	
	for x in range(1,length_of_brick+1):
		c=max(c,price_list[x]+max_cost(price_list,length_of_brick-x))
	return c
def max(a,b):
		if a>b:
			return a
		else:
			return b
			
max_cost(length,9)			