def maximum_activities(tasks, M):
    tasks.sort(key=lambda x: x[1])  # Sort tasks based on end times
    assigned = [False] * M
    count = 0

    for task in tasks:
        for i in range(M):
            if not assigned[i] and task[0] >= task[1]:  # Ensure the task is valid
                assigned[i] = True
                count += 1
                break

    return count

with open("input2.txt") as input_file, open("output2.txt","w") as output_file:



    # Read input
    N, M = map(int, input_file.readline().split())
    tasks = []
    for _ in range(N):
        start, end = map(int, input_file.readline().split())
        tasks.append((start, end))

    # Call the function and print the result
    result = maximum_activities(tasks, M)
    print(result)

