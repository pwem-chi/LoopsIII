row_nr = int(input("Enter the amount of rows : "))

for n in range(row_nr+1):
    for m in range(1,n+1):
        print(n*m, end = ' ')
    print()