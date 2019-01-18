def surfaceArea(A):
     # The surface area from the bottom and the top
	ans = 2 * len(A) * len(A[0])

    # Now get the surface area of the external sides

    # Left side sum first ones
	ans+=sum(A[0])

    # Right side sum last elements
	ans+=sum(A[-1])
    # Front (first element from each tuple)
	ans+=sum([item[0] for item in A])
    # Back (last element from each tuple)
	ans+=sum([item[-1] for item in A])
	# Now for the internal edges

    # Get the columns, if there are potential internal edges
	for i in range(len(A) - 1):
		for j in range(len(A[0])):
            # Add the abs differences between columns
			ans += abs(A[i][j] - A[i + 1][j])

    # And now add the differences between rows
	for j in range(len(A[0]) - 1):
		for i in range(len(A)):
            # Add the abs differences between rows
			ans += abs(A[i][j] - A[i][j + 1])
	
	print ans


a=[[1, 3, 4],[2, 2, 3],[1, 2, 4]]

surfaceArea(a)