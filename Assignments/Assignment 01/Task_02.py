def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag==False:
            break

with open("input2.txt") as input_file, open("output2.txt","w") as output_file:
    size = int(input_file.readline())
    arr = [0]*size
    i = 0
    for j in input_file.readline().split(" "):
        arr[i] = int(j)
        i+=1

    bubbleSort(arr)
    out = ""
    for k in arr:
        out+= f"{k} "

    output_file.writelines(out)

