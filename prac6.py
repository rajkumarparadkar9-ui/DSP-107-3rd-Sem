# ============================================
# PYTHON PRACTICAL
# Array Creation, Initialization, Indexing,
# Slicing, Reshaping and Array Operations
# Using Normal Python Library
# ============================================


# --------------------------------------------
# Program 1: Array Creation
# --------------------------------------------

arr = [1, 2, 3, 4, 5]

print("----- Program 1: Array Creation -----")
print("Array:", arr)


# --------------------------------------------
# Program 2: Special Initialization
# --------------------------------------------

print("\n----- Program 2: Special Initialization -----")

# Zeros
zeros = [[0, 0], [0, 0]]
print("Zeros:")
for row in zeros:
    print(row)

# Ones
ones = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

print("Ones:")
for row in ones:
    print(row)

# Full with 7
full = [[7, 7], [7, 7]]

print("Full:")
for row in full:
    print(row)


# --------------------------------------------
# Program 3: Indexing, Slicing and Reshaping
# --------------------------------------------

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print("\n----- Program 3: Indexing, Slicing and Reshaping -----")

# Indexing
print("Element:", arr[1][2])

# Slicing
slice_arr = [row[1:3] for row in arr[0:2]]

print("Slice:")
for row in slice_arr:
    print(row)

# Reshaping 3x3 into 1x9
new_arr = [element for row in arr for element in row]

print("Reshaped:", [new_arr])


# --------------------------------------------
# Program 4: Array Operations
# --------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]

print("\n----- Program 4: Array Operations -----")

# Addition
addition = [a[i] + b[i] for i in range(len(a))]
print("Addition:", addition)

# Multiplication
multiplication = [a[i] * b[i] for i in range(len(a))]
print("Multiplication:", multiplication)

# Mean
mean = sum(a) / len(a)
print("Mean:", mean)

# Sum
total = sum(b)
print("Sum:", total)