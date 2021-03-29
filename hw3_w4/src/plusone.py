def plus_one(start,end):
    arr = [start]
    counts = start
    while(counts < end):
        counts += 1
        arr.append(counts)
    return print(arr)


# plus_one(2,10)