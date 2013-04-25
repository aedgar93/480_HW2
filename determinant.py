%cython

#determinant of the matrix using diagonals.
#lots of typing, but very straight forward
# instead we could break the matrix down to 3x3 and again to 2x2, but because the matrix is a fixed size we can just use this method
def find_deter():
    """ I could make a list of lists, but I will keep them seperate
    so it is easy to see what is going on """
    r1 = [1.1, 2.2, 1.5, 6.7]
    r2 = [5.6, 4.8, 9, 10.5]
    r3 = [92.1, 35,1,0]
    r4 = [8.4, 5.5, 7.8, 9.4]
    total = 0

    first = r1[0]*(r2[1]*r3[2]*r4[3]+r3[1]*r4[2]*r2[3]+r4[1]*r2[2]*r3[3]-r2[3]*r3[2]*r4[1]
                   -r3[3]*r4[2]*r2[1]-r3[1]*r2[2]*r4[3])
    second = r1[1]*(r2[2]*r3[3]*r4[2]+r3[2]*r4[3]*r2[0]+r4[2]*r2[3]*r3[0]-r2[0]*r3[3]*r4[2]
                   -r3[0]*r4[3]*r2[2]-r3[2]*r2[3]*r4[0])

    third = r1[2]*(r2[3]*r3[0]*r4[1]+r3[3]*r4[0]*r2[1]+r4[3]*r2[0]*r3[1]-r2[1]*r3[0]*r4[3]
                   -r3[1]*r4[0]*r2[3]-r3[3]*r2[3]*r4[1])
    fourth = r1[3]*(r2[3]*r3[1]*r4[2]+r3[0]*r4[1]*r2[2]+r4[0]*r2[1]*r3[2]-r2[2]*r3[1]*r4[0]
                   -r3[2]*r4[1]*r2[0]-r3[0]*r2[1]*r4[2])

    return first-second+third-fourth


#cython version
#there is not much to do here
"""I could have made this function somewhat recursive. In that case I could use cdef on all of the functions
and also use type declarations"""
cdef find_deter2():
    r1 = [1.1, 2.2, 1.5, 6.7]
    r2 = [5.6, 4.8, 9, 10.5]
    r3 = [92.1, 35,1,0]
    r4 = [8.4, 5.5, 7.8, 9.4]
    total = 0

    first = r1[0]*(r2[1]*r3[2]*r4[3]+r3[1]*r4[2]*r2[3]+r4[1]*r2[2]*r3[3]-r2[3]*r3[2]*r4[1]
                   -r3[3]*r4[2]*r2[1]-r3[1]*r2[2]*r4[3])
    second = r1[1]*(r2[2]*r3[3]*r4[2]+r3[2]*r4[3]*r2[0]+r4[2]*r2[3]*r3[0]-r2[0]*r3[3]*r4[2]
                   -r3[0]*r4[3]*r2[2]-r3[2]*r2[3]*r4[0])

    third = r1[2]*(r2[3]*r3[0]*r4[1]+r3[3]*r4[0]*r2[1]+r4[3]*r2[0]*r3[1]-r2[1]*r3[0]*r4[3]
                   -r3[1]*r4[0]*r2[3]-r3[3]*r2[3]*r4[1])
    fourth = r1[3]*(r2[3]*r3[1]*r4[2]+r3[0]*r4[1]*r2[2]+r4[0]*r2[1]*r3[2]-r2[2]*r3[1]*r4[0]
                   -r3[2]*r4[1]*r2[0]-r3[0]*r2[1]*r4[2])

    return first-second+third-fourth

%timeit find_deter()

%time find_deter2()
