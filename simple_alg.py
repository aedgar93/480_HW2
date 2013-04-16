print "Hello"

import math

#computes the probability of the binomial function in the specified range inclusive
#min, max are the values for the range
#n is the total population
#p is the success probability
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
	coeff = math.factorial(n) / (math.factorial(x)*math.factorial(n-x))
	return coeff*(p**x)*((1-p)**(n-x))


#examples
# We want the probability that a binomial with population of 2 and success probability of .5
#for 0<= x <= 1
x = binom_range(0,1,2,.5)
print x # should print .75


x = binom_range(10,15,20, .7)
print x


                                                                                                 
