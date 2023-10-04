input_file = open("input1b.txt")
output_file = open("output1b.txt","w")

inputs = int(input_file.readline())

for i in range(inputs):
    x = input_file.readline()
    x = x[10:]
    if "+" in x:
        x = x.split("+")
        output_file.writelines(f"The result of {int(x[0])} + {int(x[1])} is {int(x[0])+int(x[1])}")

    elif "-" in x:
        x = x.split("-")
        output_file.writelines(f"The result of {int(x[0])} - {int(x[1])} is {int(x[0]) - int(x[1])}")

    elif "/" in x:
        x = x.split("/")
        output_file.writelines(f"The result of {int(x[0])} / {int(x[1])} is {int(x[0]) / int(x[1])}")

    elif "*" in x:
        x = x.split("*")
        output_file.writelines(f"The result of {int(x[0])} * {int(x[1])} is {int(x[0]) * int(x[1])}")
    if i<inputs-1:
        output_file.writelines("\n")

input_file.close()
output_file.close()