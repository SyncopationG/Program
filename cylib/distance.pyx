from mathlib cimport max

cpdef inline int chebyshev(int x1, int y1, int x2, int y2):
    return max(abs(x1-x2),abs(y1-y2))
