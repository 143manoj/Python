def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Get the number of rows for the pattern from the user
n = int(input("Enter the number of rows: "))
print_pattern(n)
print("puneeth")
