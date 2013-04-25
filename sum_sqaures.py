%cython

#sum of the natural numbers squared from 1 to n
def sum_sqaures(n):
    return (n*(n+1)*(2n+1))/6


"""assuming n only goes to 10,000 we can use an int. If it was larger
we would want to use a long.
There is not much to change here except for adding in the type declaration
"""
def sum_sqaures_cy(int n):
    return (n*(n+1)*(2n+1))/6

#lets see how they do for a small number

%timeit sum_squares(2)

%timeit sum_squares_cy(2)


#now a larger number

%timeit sum_squares(8000)

%timeit sum_squares_cy(8000)
