#Problem 3
def knight_moves(i, j, n, m):
    moves = [
        (i+2, j+1), (i+2, j-1),
        (i-2, j+1), (i-2, j-1),
        (i+1, j+2), (i+1, j-2),
        (i-1, j+2), (i-1, j-2)
    ]
    
    valid = []
    for x, y in moves:
        if 0 <= x < n and 0 <= y < m:
            valid.append((x, y))
    
    return valid

def min_knight_sum(A):
    n = len(A)
    m = len(A[0])
    
    min_sum = float('inf')
    pos = None
    
    for i in range(n):
        for j in range(m):
            for x, y in knight_moves(i, j, n, m):
                s = A[i][j] + A[x][y]
                if s < min_sum:
                    min_sum = s
                    pos = ((i, j), (x, y))
    
    return pos, min_sum

def value(i, j):
    return ((-1)**i) * (i*i - i) + ((-1)**j) * (j*j - j + 1)

def f(n):
    max_sum = -float('inf')
    
    for i in range(n):
        for j in range(n):
            for x, y in knight_moves(i, j, n, n):
                s = value(i, j) + value(x, y)
                if s > max_sum:
                    max_sum = s
    
    return max_sum % 7001

#Test Case 3.1
print("3.1:")
print(knight_moves(0, 0, 3, 3))

# Test Case 3.2
print("3.2:")
A = [
    [1, 5, 3],
    [2, 9, 4],
    [7, 6, 8]
]
print(min_knight_sum(A))

# Test Case 3.3
print("3.3:")
print(f(10))   # thử nhỏ trước
