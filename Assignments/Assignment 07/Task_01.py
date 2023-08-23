with open("input1.txt") as input_file, open("output1.txt","w") as output_file:
    n = int(input_file.readline())
    tasks = []
    for i in range(n):
        j, k = map(int,input_file.readline().split(" "))
        tasks.append((j, k))

    for i in range(n - 1):
        for j in range(0, n-i-1):
            if tasks[j][1] > tasks[j+1][1]:
                tasks[j], tasks[j+1] = tasks[j+1], tasks[j]
        # print(tasks)
    task = []
    lastfinishtime = -1
    for j in tasks:
        if j[0] >= lastfinishtime:
            task.append(j)
            lastfinishtime = j[1]
        # print(task)
    output_file.writelines(f"{len(task)}\n")
    for i in task:
        output_file.writelines(f"{str(i[0])} {str(i[1])} \n")