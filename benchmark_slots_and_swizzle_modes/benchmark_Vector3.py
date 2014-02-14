from __future__ import division, print_function
import timeit
import pprint
import sys

nruns = 7
repeats = 100000

def instantiation_v3(module_name):
    setup = 'from %s import Vector3' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='Vector3(1.0, 2.0, 3.0)',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def index_read_access_v3(module_name):
    setup = 'from %s import Vector3; v3 = Vector3(1.0, 2.0, 3.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a = v3[0]',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats
    
def single_swizzle_read_access_v3(module_name):
    setup = 'from %s import Vector3; v3 = Vector3(1.0, 2.0, 3.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a = v3.y',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mutate_by_index_access_v3(module_name):
    setup = 'from %s import Vector3; v3 = Vector3(1.0, 2.0, 3.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='v3[1] = 7.0',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mutate_by_member_access_v3(module_name):
    setup = 'from %s import Vector3; v3 = Vector3(1.0, 2.0, 3.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='v3.y = 7.0',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def add_v3(module_name):
    setup = 'from %s import Vector3; a=Vector3(1.0, 2.0, 3.0); b=Vector3(4.0, 5.0, 6.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a + b',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mul_v3(module_name):
    setup = 'from %s import Vector3; v3 = Vector3(1.0, 2.0, 3.0); r=1.3' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='r * v3',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats


variants = [ 'euclid_slots', 'euclid_no_slots', 'euclid_swizzle_set' ]
headers = [ 'testbed',
            'instantiation',
            'index_read_access',
            'single_swizzle_read_access',
            'mutate_by_index_access',
            'mutate_by_member_access',
            'add',
            'mul',
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
    row.append(repr_(instantiation_v3(module_name)))
    row.append(repr_(index_read_access_v3(module_name)))
    row.append(repr_(single_swizzle_read_access_v3(module_name)))
    row.append(repr_(mutate_by_index_access_v3(module_name)))
    row.append(repr_(mutate_by_member_access_v3(module_name)))
    row.append(repr_(add_v3(module_name)))
    row.append(repr_(mul_v3(module_name)))
    row_text = fseparator.join(row)
    table_rows.append(row_text)
text = '\n'.join(table_rows)

print(text)


#pprint.pprint(timmings)

