#!/usr/bin/env python

import pdb

f = open("primes.txt", "r")
nums = []
for l in f:
	l = l.replace("\n", "")
	p = l.split(" ")
	p = [x for x in p if x != '']
	p = [x for x in p if x != '\n']
	nums.extend(p)
f.close()

primes = []
for t in nums:
	primes.append(int(t))

sum = 0
for p in primes:
	sum += p
	if (sum in primes):
		print sum
	if (sum > 1000000):
		break
