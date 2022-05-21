import numpy

A = numpy.array([
    [17, 65, -13, 50, 84], 
    [12, 16, 37, 18, 25], 
    [56, 23, 11, -19, 38],
    [3, -5, 47, 10, 18]])
print("SPL yang ada diubah ke bentuk matriks :")
print(A,"\n")
n = len(A)
x = numpy.zeros(n)

for k in range(n):
    pivot = A[k][k] 
    A[k] = A[k]/pivot
    # print(A)
    for i in range(n): 
        if i == k: continue 
        factor = A[i][k]
        for j in range(k,n+1):
            A[i][j] = A[i][j] - factor * A[k][j]
    print(A)

x = A[:, n]
print("\nHasilnya adalah : \n",x)