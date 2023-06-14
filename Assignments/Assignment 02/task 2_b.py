input_file = open("input2.txt")
output_file = open("output2.txt","w")

n1= input_file.readline()
# print(n1)
n1= int(n1)
l1 = [0]*n1
j = 0
for i in input_file.readline().split(" "):
    l1[j] = int(i)
    j+=1

n2= input_file.readline()
n2= int(n2)
l2 = [0]*n2
j = 0
for i in input_file.readline().split(" "):
    l2[j] = int(i)
    j+=1

print(l1)
print(l2)

