def my_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def Insertion_Sort(arr):
    n = my_len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
    return arr

def is_triangular(nums):
    Insertion_Sort(nums)

    for i in range(my_len(nums) - 2):
        if nums[i] + nums[i + 1] > nums[i + 2]:
            return 1

    return 0

sides = list(map(int, input("Enter the lengths of the sides with a space between every side(ex:10 20 30)\n").split()))
print(is_triangular(sides))