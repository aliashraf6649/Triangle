def my_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count
def is_triangular(arr):
    n = my_len(arr)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[j] + arr[k] > arr[i]:
                    return 1
    
    return 0

sides = list(map(int, input("Enter the lengths of the sides with a space between every side(ex:10 20 30)\n").split()))
print(is_triangular(sides))
