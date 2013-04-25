%cython

#multiply 2 4x4 matrix

def multiply():
    a = [[1,2,3,4], [5,6,7,8],[3,5,8,6],[0,3,6,7]]
    b = [[6,3,7,3],[0,7,4,5],[7,7,5,4],[1,2,4,8]]
    c = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #b columns
    for k in range(4):
        print k
        #a rows
        for i in range(4):
            sum = 0
            #a columns
            for j in range(4):
                sum+= a[j][k]*b[i][j]
            c[i][k] = sum

    return c

cdef multiply2():
    cdef a = [[1,2,3,4], [5,6,7,8],[3,5,8,6],[0,3,6,7]]
    cdef b = [[6,3,7,3],[0,7,4,5],[7,7,5,4],[1,2,4,8]]
    cdef c = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #b columns
    for k in range(4):
        print k
        #a rows
        for i in range(4):
            sum = 0
            #a columns
            for j in range(4):
                sum+= a[j][k]*b[i][j]
            c[i][k] = sum

    return c


%timeit multiply()
%timeit multiply2()
