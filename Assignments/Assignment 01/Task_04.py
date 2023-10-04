with open("input4.txt") as input_file, open("output4.txt","w") as output_file:
    n = int(input_file.readline())
    names = []
    dest = []
    times = []
    for i in range(n):
        x = input_file.readline().split(" ")
        names.append(x[0])
        dest.append(x[4])
        times.append(x[6][:-1])
    for i in range(n):
        max = i
        for j in range(i,n):
            if names[max]>names[j]:
                max = j
            elif names[max]==names[j]:
                if times[max]<times[j]:
                    max = j
        names[i],names[max] = names[max],names[i]
        dest[i], dest[max] = dest[max],dest[i]
        times[i], times[max] = times[max], times[i]

    for i in range(n):
        output_file.writelines(f"{names[i]} will departure for {dest[i]} at {times[i]}")
        if i<n:
            output_file.writelines("\n")