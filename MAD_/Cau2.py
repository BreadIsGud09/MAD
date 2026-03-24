#Problem 2
def product(M,N):
    result =[[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += M[i][k] * N[k][j]
                
    return result

def compute_ABn(n):
    A = [[1, 3], [2, -1]]
    B = [[2, 1], [1, 4]]

    An = A
    Bn = B

    for _ in range(1, n):
        newA = product(An, A)
        temp = product(Bn, B)
        

        for i in range(2):
            for j in range(2):
                newA[i][j] += 7 * temp[i][j]


        part1 = product(An, B)
        part2 = product(Bn, A)
        
        newB = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                newB[i][j] = part1[i][j] + part2[i][j]

        An = newA
        Bn = newB

    return An, Bn

# Test case 2.1
print("2.1:")
M = [[1, 2], [3, 4]]
N = [[5, 6], [7, 8]]

print(product(M, N))

# Test Case 2.2
print("2.2")
An, Bn = compute_ABn(2)
print("An:", An)
print("Bn:", Bn)

