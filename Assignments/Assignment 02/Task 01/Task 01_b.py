input_file = open("input1.txt")
output_file = open("output1.txt","w")

n,s = input_file.readline().split(" ")
n,s = int(n),int(s)
arr = [0]*n
j = 0
for i in input_file.readline().split(" "):
    arr[j] = int(i)
    j+=1

sortedarry = sorted(arr)
i,j = 0, len(arr)-1
flag = False
while i<j:
    sum = sortedarry[i]+sortedarry[j]
    if sum<s:
        i += 1
    elif sum == s:
        flag = True
        break
    elif sum>s:
        j -= 1
if flag==False:
    print("IMPOSSIBLE")
else:
    x = ""
    for k in range(len(arr)):
        if sortedarry[i]==arr[k]:
            x += str(k+1)
            x+=" "
        elif sortedarry[j]==arr[k]:
            x += str(k + 1)
            x += " "

    output_file.writelines(x)


