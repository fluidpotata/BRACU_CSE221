input_file = open("input1.txt")
output_file = open("output1.txt","w")

n,s = input_file.readline().split(" ")
n,s = int(n),int(s)
arr = [0]*n
j = 0
for i in input_file.readline().split(" "):
    arr[j] = int(i)
    j+=1

sum = 0
flag = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == s:
            # print(i+1, j+1)
            output_file.writelines(f"{i+1} {j+1}")
            flag = True
            break
    if flag==True:
        break
if flag==False:
    print("IMPOSSIBLE")
input_file.close()
output_file.close()




