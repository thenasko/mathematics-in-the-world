def find_summands(A, n):
    ## Convert A to a set
    Aset = { a for a in A }
    
    ## For each a in A, check if b = n - a is also in it
    for a in Aset:
        if (n - a) in Aset:
            return (a, n - a)

    return None

A = [1, 2, 3, 4, 5]
print(find_summands(A, 8))
