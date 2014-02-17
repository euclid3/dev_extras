This repository supports the development of euclid3/euclid3.

Stores benchmarks and experiments with alternate implementations to not clutter
the core project and remain discoverable. 

Good to see see if some approach has been considered, or to recycle some benchmarks.

Each experiment is stored in a top dir, it has it's own readme with details, and a
short entry in this file with a description.

Experiments
===========

01_benchmark_slots_and_swizzle_modes
------------------------------------

The original code proposes three modes to run the library:
	- use python slots, don't support swizzle for set operations (default)
	- don't use python slots, don't support swizzle for set operations
	- use slots and enable swizzle for set operations, like v3.xy = 1.1, 2.2

This complicates the code with  __metaclass__  and conditionally injecting methods.
It is desired to simplify that by keeping only the best performant of the variants.
This experiment benchmarks the differences between the three variants, and is referenced in https://github.com/euclid3/euclid3/issues/3

02_benchmark_simpler_f06655d
----------------------------

Benchmarking before and after the refactor proposed in https://github.com/euclid3/euclid3/issues/3

	- get rid of modes
	- eliminate __metaclass__
	- implement swizzle (read only) using properties

Data colected in simpler_f06655d.ods.
All the operations exercised in the benchmark are faster after the refactor.

03_benchmark_determinant
------------------------

cocos.euclid has a different implementation for Matrix3 determinant and inverse.
Benchmarking shows that the cocos version is a bit faster.
As an aside, in those opers py3.3 is noticeably slower than py2.6, around a 40% slower
Linked to https://github.com/euclid3/euclid3/issues/5

 