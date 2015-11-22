#!/usr/bin/env python

def main():
	idx = 1
	while (1):
		idx+=1
		s = "".join(sorted(str(idx)))
		allMatch = 1
		for i in range(1,7):
			x = "".join(sorted(str(idx*i)))
			if ( "".join(sorted(str(idx*i))) != s):
				allMatch = 0 
		if (allMatch == 1):
			print idx
			for i in range(1,7):
				print (idx*i)
			break

if __name__ == "__main__":
	main()
		
