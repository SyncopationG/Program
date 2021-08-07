def example_cython():
    cdef int i,j=0
    for i in range(100):
        j += 1
    return j
