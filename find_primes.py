%cython

#accepts a positive integer value greater than 2 and returns all primes <= the input

def find_primes(n):
    primes = []
    for i in range(2,n):
        check = True
        for num in primes:
            if(num*num > i):
                break
            if(i % num == 0):
                check = False
                break

        if(check):
            primes.append(i)
    return primes

#cython implementations

cdef cy_primes(int n)
    cdef primes = []
    for i in range(2,n):
        cdef bool check = True
        for num in primes:
            if(num*num > i):
                break
            if(i % num == 0):
                check = False
                break

        if(check):
            primes.append(i)
    return primes

%timeit find_primes(9000)

%timeit cy_primes(9000)
