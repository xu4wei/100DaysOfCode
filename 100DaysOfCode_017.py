def twonumbers(nums, target):
    # Create a dictionary to store the seen elements and their indices.
    seen = {}
    # Iterate through the list.
    for i, num in enumerate(nums):
        # Calculate the complement of the current element.
        complement = target - num
        # Check if the complement has been seen before.
        if complement in seen:
            # If yes, return the indices of the current element and the complement.
            return [seen[complement], i]
        # If not, add the current element and its index to the dictionary.
        seen[num] = i
        # If no solution is found, return an empty list.
    return []


print(twonumbers([1, 1, 2, 3, 5, 8, 13], 7))
