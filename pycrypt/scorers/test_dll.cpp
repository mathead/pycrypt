#include "stdafx.h"
#include <stdexcept>
#include <map>

using namespace std;
#define EXPORT extern "C" __declspec(dllexport)

struct structure_test {
	char *sub;
	int c;
};
//struct structure_test2 {
//	int c;
//	int i;
//};


EXPORT int myprint(int a) {
	return a;
}

EXPORT void str_ptr_test(char* a)
{
	a[0] = 'b';
}

EXPORT void arr_alloc_test(structure_test* a)
{

//	strcpy(a[9].sub, "ahoj");
}


struct cmp_str
{
	static int length;
	bool operator()(char const *a, char const *b)
	{
		return std::strncmp(a, b, cmp_str::length) < 0;
	}
};
int cmp_str::length;

EXPORT int getngramfrequencies(structure_test* a, char* text, int length, int text_len)
{
	map<char*, int, cmp_str> d;
	cmp_str::length = length;
	char *sub;
	int j = 0;
	for (int i = 0; i < text_len + 1 - length; i++) {
		sub = text + i;
		if ( d.find(sub) != d.end() ) {
			a[d[sub]].c++;
		} else {
			a[j].c = 1;
			strncpy(a[j].sub, sub, length);
			a[j].sub[length] = 0;
			d[sub] = j;
			j++;
		}
	}

	return j;
}


//
//def getNgramFrequencies(self, text, length):
//	"""Get dictionary of frequencies of N-grams (of given length)"""
//	d = {}
//	for i in range(len(text) - 1 - length):
//		sub = text[i:i+length]
//		if (d.has_key(sub)):
//			d[sub] += 1.0
//		else:
//			d[sub] = 1.0
//
//	for i in d:
//		d[i] /= len(text)
//
//	return d
//
