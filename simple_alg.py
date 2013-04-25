%cython


"""computes the probability of the binomial function in the specified range inclusive
min, max are the values for the range
n is the total population
p is the success probability """
def binom_range(min, max, n, p):
	if(min > max):
		raise Exception("Please pass a valid range")
	if(min < 0):
		raise Exception("The minimum must be positive")
	if(max >n):
		raise Exception("The maximum cannot exceed the total population")
	current = min
	total = 0
	while(current <= max): #go through and add up all the probabilities
		total+= binom(current, n,p)
		current = current+1
	return total

def binom(x, n, p):
	coeff = factorial(n) / (factorial(x)*factorial(n-x))
	return coeff*(p**x)*((1-p)**(n-x))


#make my own factorial so I can optimize more
def factorial(x):
	total = 1
	for i  in range(1,x):
		total = total*i
	return total   


#cython version
cdef binom_range2(int min, int max,int n,float p):
	if(min > max):
		raise Exception("Please pass a valid range")
	if(min < 0):
		raise Exception("The minimum must be positive")
	if(max >n):
		raise Exception("The maximum cannot exceed the total population")
	current = min
	total = 0
	while(current <= max): #go through and add up all the probabilities
		total+= binom2(current, n,p)
		current = current+1
	return total

cdef binom2(int x, int n,float p):
	coeff = factorial2(n) / (factorial2(x)*factorial2(n-x))
	return coeff*(p**x)*((1-p)**(n-x))


#make my own factorial so I can optimize more
cdef factorial2(int x):
	total = 1
	for i  in range(1,x):
		total = total*i
	return total

%timeit binom_range(0,15,50,.5)

%timeit binom_range2(0,15,50,.5)

												 
