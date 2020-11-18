import sys
print("Numeric Matrix Processor")
print("Here are your mathematical operations")
print('1. Add matrices.')
print('2. Subtract Matrices.')
print('3. Element - wise multiplication')
print('4. Multiply matrix with a constant.')
print('5. Transpose matrix.')
print('6. Exit')
choice_ = int(input("Your Choice: "))
# addition of matrices
if choice_ == 1:
    n = int(input("Enter the number of rows:"))
    m = int(input("Enter the number of columns:"))
    a_ = []
    for i in range(0, n):
        a_.append([int(j) for j in input().split()])
    n1_ = int(input("Enter the number of rows: "))
    m1_ = int(input("Enter no. of columns: "))
    b_ = []
    for i in range(0, n):
        b_.append([int(j) for j in input().split()])
    if n1_ == n and m1_ == m:
        res = []
        for i in range(0, n):
            val = []
            for j in range(0, m):
                val.append(a_[i][j] + b_[i][j])
            res.append(val)
        print("Result:")
        print(res)
    else:
        print("ERROR")
# subtraction of matrices
elif choice_ == 2:
    n = int(input("Enter the number of rows:"))
    m = int(input("Enter the number of columns:"))
    a_ = []
    for i in range(0, n):
        a_.append([int(j) for j in input().split()])
    n1_ = int(input("Enter the number of rows: "))
    m1_ = int(input("Enter no. of columns: "))
    b_ = []
    for i in range(0, n):
        b_.append([int(j) for j in input().split()])
    if n1_ == n and m1_ == m:
        res = []
        for i in range(0, n):
            val = []
            for j in range(0, m):
                val.append(a_[i][j] - b_[i][j])
            res.append(val)
        print("Result:")
        print(res)
    else:
        print("ERROR")
# multiplication of matrices
elif choice_ == 3:
    n = int(input("Enter the number of rows:"))
    m = int(input("Enter the number of columns:"))
    a_ = []
    for i in range(0, n):
        a_.append([int(j) for j in input().split()])
    n1_ = int(input("Enter the number of rows: "))
    m1_ = int(input("Enter no. of columns: "))
    b_ = []
    for i in range(0, n):
        b_.append([int(j) for j in input().split()])
    if n1_ == n and m1_ == m:
        res = []
        for i in range(0, n):
            val = []
            for j in range(0, m):
                val.append(a_[i][j] * b_[i][j])
            res.append(val)
        print(res)
    else:
        print("ERROR")
    # Multiply matrix with a constant
elif choice_ == 4:
    n = int(input("Enter the number of rows:"))
    m = int(input("Enter the number of columns:"))
    print("Enter Matrix")
    a_ = []
    for i in range(0, n):
        a_.append([int(j) for j in input().split()])
    print("Enter the constant: ", end="")
    c = int(input())
    out = []
    for i in a_:
        row = [j * c for j in i]
        out.append(row)
    print("The matrix is: \n")
    for f in out:
        for g in f:
            print(g, end="  ")
        print()
# transpose matrix
elif choice_ == 5:
    n = int(input("Enter the number of rows:"))
    m = int(input("Enter the number of columns:"))
    print("Enter Matrix")
    a_ = []
    for i in range(0, n):
        a_.append([int(j) for j in input().split()])
    rez = [[a_[j][i] for j in range(len(a_))] for i in range(len(a_[0]))]
    print("\n")
    for row in rez:
        print(row)
elif choice_ == 6:
    sys.exit()
else:
    print("Oops! Please pick a valid choice.")
