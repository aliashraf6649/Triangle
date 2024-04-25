def max_heap(arr,n,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr [left]:
        largest = left
    if right < n and arr[largest] < arr [right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr,n,largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        max_heap(arr, n, i)

def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0 , -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr,i, 0)
        
def is_triangular(nums):
    heap_sort(nums)

    for i in range(len(nums) - 2):
        if nums[i] + nums[i + 1] > nums[i + 2] and nums[i + 1] + nums[i+2] > nums[i] and nums[i] + nums[i+2] > nums [i+1]:
            return 1

    return 0

sides = list(map(int, input("Enter the lengths of the sides with a space between every side(ex:10 20 30)\n").split()))
print(is_triangular(sides))