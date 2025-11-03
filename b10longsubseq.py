'''
Problem: Longest Contiguous Increasing Subsequence (Length)


COMPLEXITY
Time Complexity:  O(n)   # one linear pass through the list
Space Complexity: O(1)   # constant auxiliary variables
'''

def longest_increasing_run(nums):
  
    if not nums:
        return 0

    best_run = 1
    current_run = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_run += 1
        else:
            current_run = 1
        best_run = max(best_run, current_run)

    return best_run


#Test cases
assert longest_increasing_run([5, 3, 4, 8, 6, 7, 9, 1]) == 3   # [6,7,9]
assert longest_increasing_run([5, 1, 2, 3, 2, 5, 6]) == 3      # [2,5,6]
assert longest_increasing_run([]) == 0                         # empty list
assert longest_increasing_run([9]) == 1                        # single element
assert longest_increasing_run([1, 2, 3, 4, 5]) == 5            # all increasing
assert longest_increasing_run([5, 4, 3, 2, 1]) == 1            # strictly decreasing


