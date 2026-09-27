def merge_ordered(a,b):
    result=[]
    ai = 0
    bi = 0

    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            result.append(a[ai])
            ai += 1
        else:
            result.append(b[bi])
            bi += 1

    while ai < len(a):
        result.append(a[ai])
        ai += 1

    while bi < len(b):
        result.append(b[bi])
        bi += 1

    return result

def merge_insert_ordered(a,b):
    ai = 0
    for value in b:
        while ( ai < len(a) and a[ai] <= value):
            ai += 1
        a.insert(ai, value)
        ai += 1
    return a

array1=sorted([1,9,3,24,5,10])
print(array1)
array2=sorted([5,9,49,32,98])
print(array2)
print(merge_ordered(array1, array2))
print(merge_insert_ordered(array1, array2))