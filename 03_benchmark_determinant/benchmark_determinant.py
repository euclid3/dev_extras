from __future__ import division, print_function
import timeit
import pprint
import sys

nruns = 3
repeats = 100000

def determinant_matrix3(module_name):
    setup = 'from %s import Matrix3; m = Matrix3()' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='m.determinant()',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def inverse_matrix3(module_name):
    setup = 'from %s import Matrix3; m = Matrix3()' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='m.inverse()',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats


variants = [ 'euclid_cd2331', 'euclid_cocos',]
headers = [ 'testbed',
            'determinant_matrix3',
            'inverse_matrix3',
          ]

fseparator = '\t'
decimal_point = ','
def repr_(v):
    if decimal_point == '.':
        return repr(v)
    else:
        s = repr(v)
        s = s.replace('.', decimal_point)
    return s
table_rows = [fseparator.join(headers),]

for module_name in variants:
    row = ['py_%s_%s'%(sys.version[:5], module_name), ]
    row.append(repr_(determinant_matrix3(module_name)))
    row.append(repr_(inverse_matrix3(module_name)))
    row_text = fseparator.join(row)
    table_rows.append(row_text)
text = '\n'.join(table_rows)

print(text)


#pprint.pprint(timmings)

