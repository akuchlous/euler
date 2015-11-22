#!/usr/bin/env python


def fb(previous,present):
	return (present,previous+present)

def main():
	idx = 3
	previous = 1
	present = 2
	while (1):
		idx+=1
		previous, present = fb(previous, present)
		print idx, present
		if (len(str(present)) >= 1000):
			break

if __name__ == "__main__":
	main()
		
		
