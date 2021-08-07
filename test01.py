import ctypes

ll = ctypes.cdll.LoadLibrary
lib = ll("./clib/utils.so")
print(lib.add(1, 2))
"""
1 hello.pyx
2 cython hello.pyx
3 gcc -shared -fPIC hello.c -o hello.so
4 import hello
5 hello.hello()
"""
from cylib import hello

hello.hello()
from cylib import example_cython
from cylib import example_python
import time

a = time.perf_counter()
example_cython.example_cython()
b = time.perf_counter()
example_python.example_python()
c = time.perf_counter()
lib.test()
d = time.perf_counter()
cython = b - a
python = c - b
clang = d - c
print(cython, python, clang)
print(python / cython, python / clang, cython / clang)
