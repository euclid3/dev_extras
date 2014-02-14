Branch to benchmark some opers when with the different mode flags ( _use_slots and _enable_swizzle_set ) - issue #3

The euclid.py from euclid3\euclid3 , 2014 04 12, sha=0e5ffd is copied and edited to:
    euclid_slots.py : no change, _use_slots = True and _enable_swizzle_set = False
	euclid_no_slots.py : _use_slots = False , _enable_swizzle_set = False
	euclid_swizzle_set : _use_slots = True , _enable_swizzle_set = True
	
Then added
	benchmark_Vector2.py
	benchmark_Vector3.py
	
They exercise the vector classes on a few common operations and output to stdout a text with results in CSV format.

The benchmarks are run with python 2.6.6 and 3.3.1, redirecting the output to appropriate files, then that is pasted into an open-office spreadsheet.
The spreadsheet is included as mode_stats.ods

Results:
	with _swizzle_set = True performance is the worst: mutate_by_member_access is 14 times slower, and add two vectors or scale a vector is three times slower
	
	results switching only _use_slots shows less differences, still in py2.6 add and scale are four times slower with _use_slots = False

Decision:
	Keep the _use_slots codepath, nuke the others
