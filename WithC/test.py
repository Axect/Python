import ctypes
from ctypes import CDLL

lib = CDLL("libtest.so")
lib.f.argtypes = [ctypes.c_double, ctypes.c_double]
lib.f.restype = ctypes.c_double

print(lib.f(1.0, 2.0))

lib2 = CDLL("libtest2.so")
lib2.g_double.argtypes = [ctypes.c_double, ctypes.c_double]
lib2.g_double.restype = ctypes.c_double
lib2.g_int.argtypes = [ctypes.c_int, ctypes.c_int]
lib2.g_int.restype = ctypes.c_int

print(lib2.g_double(1.0, 2.0))
print(lib2.g_int(1, 2))

