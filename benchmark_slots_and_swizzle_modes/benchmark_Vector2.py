from __future__ import division, print_function
import timeit
import pprint
import sys

nruns = 7
repeats = 1000000

def instantiation_v2(module_name):
    setup = 'from %s import Vector2' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='Vector2(1.0, 2.0)',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def index_read_access_v2(module_name):
    setup = 'from %s import Vector2; v2 = Vector2(1.0, 2.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a = v2[0]',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats
    
def single_swizzle_read_access_v2(module_name):
    setup = 'from %s import Vector2; v2 = Vector2(1.0, 2.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a = v2.y',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mutate_by_index_access_v2(module_name):
    setup = 'from %s import Vector2; v2 = Vector2(1.0, 2.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='v2[1] = 7.0',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mutate_by_member_access_v2(module_name):
    setup = 'from %s import Vector2; v2 = Vector2(1.0, 2.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='v2.y = 7.0',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def add_v2(module_name):
    setup = 'from %s import Vector2; a=Vector2(1.0, 2.0); b=Vector2(3.0, 4.0)' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='a + b',
                              setup=setup,
                              number=repeats)
    return min(times) / repeats

def mul_v2(module_name):
    setup = 'from %s import Vector2; v2 = Vector2(1.0, 2.0); r=1.3' % module_name 
    for i in range(nruns):
        times = timeit.repeat(stmt='r * v2',
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
    row.append(repr_(instantiation_v2(module_name)))
    row.append(repr_(index_read_access_v2(module_name)))
    row.append(repr_(single_swizzle_read_access_v2(module_name)))
    row.append(repr_(mutate_by_index_access_v2(module_name)))
    row.append(repr_(mutate_by_member_access_v2(module_name)))
    row.append(repr_(add_v2(module_name)))
    row.append(repr_(mul_v2(module_name)))
    row_text = fseparator.join(row)
    table_rows.append(row_text)
text = '\n'.join(table_rows)

print(text)


#pprint.pprint(timmings)

