# Python program for implementation of heap Sort extracted from GeeksForGeeks
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]:
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

# Python Program for recursive binary search extracted from GeeksForGeeks
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
	# Check base case 
	if r >= l: 

		mid = l + (r - l)//2

		# If element is present at the middle itself 
		if arr[mid] == x: 
			return mid 
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 

		# Else the element can only be present 
		# in right subarray 
		else: 
			return binarySearch(arr, mid + 1, r, x) 

	else: 
		# Element is not present in the array 
		return -1

