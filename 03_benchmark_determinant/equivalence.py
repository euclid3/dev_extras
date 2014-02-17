from __future__ import division, print_function
import timeit
import pprint
import sys

from euclid_cocos import Matrix3
m = Matrix3()
print('det:', m.determinant())

from euclid_cd2331 import Matrix3
m = Matrix3()
print('det:', m.determinant())
