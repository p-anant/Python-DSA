# Given an array “A” of N integers and you have also defined the new array “B” as a concatenation of array “A” for an infinite number of times.
# For example, if the given array “A” is [1,2,3] then, infinite array “B” is [1,2,3,1,2,3,1,2,3,.......].
# Now you are given Q queries, each query consists of two integers “L“ and “R”. Your task is to find the sum of the subarray from index “L” to “R” (both inclusive) in the infinite array “B” for each query.
# Note : # The value of the sum can be very large, return the answer as modulus 10^9+7.
'''
    Time Complexity:O(Q*(R-L))
    Space Complexity:O(1).
    Where Q is the number of given queries, and L and R are the give
'''


def sumOfInfinityArray(arr, n, queries, q):
    
    mod = 10**9 + 7
    
    #  It stores answer for each query.
    ans = []

    # Traversing the given queries
    for ranges in queries:
        # Substract 1 from both L and R to use it as 0-based indexing
        l = ranges[0] - 1
        r = ranges[1] - 1

        # It stores the sum
        sume = 0

        for i in range(l, r + 1):
            index = (i % n)
            sume = (sume + arr[index]) % mod

        sume %= mod
        # Add answer to each query
        ans.append(sume)

    return ans

sumOfInfinityArray([1,2,3], 3, [[1,3],[1,5]], 2)

