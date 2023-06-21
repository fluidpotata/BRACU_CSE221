def quicksort(arr, low, high):
    if low<high:
        q = partition(arr, low, high)
        quicksort(arr, low, q - 1)
        quicksort(arr, q + 1, high)

def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j]<=x:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i+1


inp_file = open("input3.txt")
out_file = open("output3.txt","w")
n = int(inp_file.readline())
x = inp_file.readline().split(" ")
a = []
for i in range(n):
    a.append(int(x[i]))

quicksort(a,0,n-1)
out=""
for j in range(n):
    out+=str(a[j])
    if j<n-1:
        out+=" "
out_file.writelines(out) #for read and write use join and map
