with open("input3.txt") as input_file, open("output3.txt","w") as output_file:
    n = int(input_file.readline())
    ids = []
    marks = []
    for i in input_file.readline().split(" "):
        ids.append(int(i))
    for i in input_file.readline().split(" "):
        marks.append(int(i))

    for i in range(0,n):
        max = i
        for j in range(i,n):
            if marks[j] == marks[max]:
                if ids[j] < ids[max]:
                    max = j
            elif marks[j]>marks[max]:
                max = j
        marks[i],marks[max] = marks[max], marks[i]
        ids[i],ids[max] = ids[max],ids[i]

    for i in range(n):
        x = f"ID: {ids[i]} Mark: {marks[i]}"
        output_file.writelines(x)
        if i!=n-1:
            output_file.writelines("\n")
