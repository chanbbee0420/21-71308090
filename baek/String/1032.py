n = int(input())
arr1 = list(input())

for i in range(n - 1):
    arr2 = list(input())
    for j in range(len(arr1)):
        if arr1[j] != arr2[j]:
            arr1[j] = '?'
print(''.join(arr1))