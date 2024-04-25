def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr

def is_triangular(arr):
    insertion_sort(arr)
    
    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 1] > arr[i + 2] and arr[i + 1] + arr[i+2] > arr[i] and arr[i] + arr[i+2] > arr [i+1]:
            return 1

    return 0

sides = list(map(int, input("Enter the lengths of the sides with a space between every side(ex:10 20 30)\n").split()))
print(is_triangular(sides))