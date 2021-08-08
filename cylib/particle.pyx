cdef class Point:
    cdef public double x
    cdef public double y
    def __init__(self, double x, double y):
        self.x = x
        self.y = y

cpdef inline double norm(Point p):
    return (p.x**2+p.y**2)**0.5

