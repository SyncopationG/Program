import numpy as np
cpdef do():
    cdef int[:] arr
    arr_np = np.zeros(10,dtype="int32")
    arr=arr_np
    arr[1]=1
    print("arr",arr)
    print("arr_np",arr_np)
