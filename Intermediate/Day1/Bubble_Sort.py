def bubble_sort(nums):
    """
    Implement the Bubble Sort algorithm to sort a list of numbers in ascending order.

    Parameters:
    - nums (list): List of numbers to be sorted (in-place).

    Returns:
    None
    """
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# Example usage:
numbers = [64, 25, 12, 22, 11]
bubble_sort(numbers)
print("Sorted list:", numbers)
