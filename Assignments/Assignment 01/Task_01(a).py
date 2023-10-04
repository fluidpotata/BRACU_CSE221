input_file = open("input1a.txt")
output_file = open("output1a.txt","w")

inputs = int(input_file.readline())

for i in range(inputs):
    x = int(input_file.readline())
    if x%2==0:
        output_file.writelines(f"{x} is an even number")
    else:
        output_file.writelines(f"{x} is an odd number")
    if i<inputs-1:
        output_file.writelines("\n")

input_file.close()
output_file.close()
