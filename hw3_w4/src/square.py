def square(start,end):
    arr = [start]
    counts = start
    while(counts < end):
        counts = counts ** 2
        arr.append(counts)
        if (counts**2 > end):
            break
    return print(arr)


# square(2,20)