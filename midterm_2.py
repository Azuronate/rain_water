#
# "Linear Bucketeer," developed by Nathan Parker, for CSCI-H 200
#	Time Complexity: O(n)
#

import numpy as np

def calculate_water(height_map):
	'''
	Given a list of length n, with positive integers (heights),
	this function calculates how much rain water can be captured
	between these heights (a/k/a buckets). A bucket is only counted
	if it abides by the shape of a local minima parabola (as water
	would leak out the sides).

	Formal Parameters:
		- height_map: length n, with positive integers (heights)
	'''
	water = 0
	local_minima = []
	left_wall = height_map[0] # Set the first wall, saves us time
	bucket = [left_wall]

	for height in height_map[1:]: # Save us time (we already know the first value)
		if height < left_wall: # Left side of parabola (water is getting trapped)
			bucket.append(height)
		elif height >= left_wall: # Right side of parabola (concavity changed)! 
			right_wall = height
			bucket.append(right_wall)

			if len(bucket) >= 3: # We cannot fill buckets/parabolas without two sides
				local_minima.append(bucket)
				threshold = np.partition(bucket, -2)[-2] # a/k/a second highest value

				#
				# Avoid using another for loop, I utilize the power of Numpy,
				# to "floor" values above a threshold (as values above would
				# give us bigger areas).
				#

				numpy_bucket = np.array(bucket)
				capped_bucket = np.where(numpy_bucket > threshold, threshold, numpy_bucket)

				area = len(numpy_bucket) * threshold
				needed_water = area - np.sum(capped_bucket)
				water += int(needed_water)
				# print(f"Area ({threshold} * {len(numpy_bucket)}) = {area}\nNeeded Water ({area} - {np.sum(capped_bucket)}) = {int(needed_water)}")

				# Reset the bucket, and find more!
				left_wall = height
				bucket = [left_wall]
			else: # Invalid buckets
				bucket = []
				left_wall = height
				bucket.append(left_wall)

	return water

print(calculate_water([1,1,2,0,2,1,3])) # 3
print(calculate_water([5,1,3,1,5])) # 10
print(calculate_water([5,1,1,1,1,5])) # 16 
print(calculate_water([1,1,2,0,2,1,3,1])) # 3
print(calculate_water([4,3,2,1,2,3,4])) # 9 
print(calculate_water([5,0,0,5])) # 10
print(calculate_water([5,0,0,0,0,0,5])) # 25
print(calculate_water([5,0,0,0,0,0,0,0,0,5])) # 40
print(calculate_water([0,5,5,0])) # 0
print(calculate_water([1,0,1])) # 1
print(calculate_water([0,0,1])) # 0
print(calculate_water([2,1])) # 0