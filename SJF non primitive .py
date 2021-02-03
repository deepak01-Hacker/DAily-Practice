def SJFnonpremitive():
    arrival = [0,2,4,6,7]
    brust   = [5,3,2,4,1]
    n_ = len(arrival)

    cpu = []
    for i in range(5):
        cpu.append([arrival[i],brust[i],i])
    cpu.sort(key = lambda x : x[0])

    waiting = [0]*n_
    turned = [0]*n_

    queue = []
    

    index = cpu[0][0]
    while(len(cpu)):
        process_taken = [-1,9999999]
        for i in range(len(cpu)):
            if cpu[i][0] <= index:
                if process_taken[1] > cpu[i][1]:
                    process_taken[1] = cpu[i][1]
                    process_taken[0] = i
            else:
                break
        queue.append([index,cpu[process_taken[0]][2]])
        index += process_taken[1]
        cpu.pop(process_taken[0])

    for i in range(len(queue)):
        waiting[queue[i][1]] = queue[i][0]-arrival[queue[i][1]]
        turned[queue[i][1]] = waiting[queue[i][1]] + brust[queue[i][1]]

    print(waiting)
    print(turned)
