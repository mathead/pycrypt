from ctypes import *

from ctypes.util import find_library

class dict_struct(Structure):
	_fields_ = [("sub", c_char_p), ("c", c_int)]

c_lib = CDLL(find_library("c"))
malloc = c_lib.malloc
malloc.argtypes = [c_long]
malloc.restype = c_void_p 

libtest = cdll.LoadLibrary('dll_test/test_dll.dll')

libtest.getngramfrequencies.restype = c_int

def getNgramFrequencies(text, length):
	arr_type = dict_struct * (len(text) + 1 - length)
	arr = arr_type()
	for j, i in enumerate(arr):
		address = malloc(length)
		i.sub = c_char_p(address)

	l = libtest.getngramfrequencies(arr, text, length, len(text))
	return dict([(i.sub, i.c) for i in arr[:l]])