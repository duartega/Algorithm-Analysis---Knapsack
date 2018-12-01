'''
Authors: Gabriel Duarte and Jorge Bautista
Date: 11/29/2018
Class: cs415 - Algorithm Analysis
Program: We will be coding the Knapsack problem
        using dynamic programing
'''

import time # Used for time measurement of program

# Open the files and create put the data into lists
def readFile(f1, f2, f3, weight, values, V):
    with open(f1,"r") as c: #c = capacity
        for line in c:
            capacity = int(line)
    with open(f2,"r") as w: #w = weights
        for line in w:
            line = int(line) # Conversion from string to int
            weight.append(line)
    with open(f3,"r") as v: #v = values
        for line in v:
            line = int(line) # Conversion from string to int
            values.append(line)

    print("\nKnapsack capacity =", capacity, "Total number of items =", len(weight),'\n')
    return capacity

def KS(capacity, weight, values, n):
    # Initialize 2d list
    V = [[ 0 for x in range(capacity+1)] for y in range(n+1)]

    # Create the values for the table (2d list)
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i==0 or j==0: # Create the outter 0's in the next line
                V[i][j] = 0
            elif weight[i-1] <= j:
                V[i][j] = max(V[i-1][j], values[i-1] + V[i-1][j-weight[i-1]])
            else:
                V[i][j] = V[i-1][j]

    print("Dynamic Programming Optimal Value:", V[n][capacity])
    print("Dynamic Programming Optimal subset:", optimalSubset(V, capacity, weight, values, n))


def optimalSubset(V, capacity, weight, values, n):
    optSS = []
    i = n
    j = capacity

    while i > 0 and j > 0:
        if V[i][j] > V[i-1][j]:
            # This will append to the beginning since we
            # are backtracking. Sorting takes more time with larger sets.
            optSS = [i] + optSS
            i -= 1
            j -= weight[i]
        else:
            i -= 1

    return optSS

def main():
    # Have user enter file names
    file1 = input("Please enter file containing the capacity:")
    file2 = input("Please enter file containing the weights:")
    file3 = input("Please enter file containing the values:")

    # Initialize lists on one line
    weight, values, V = ([] for i in range(3))

    # Call function to read files and return the capacity
    capacity = readFile(file1, file2, file3, weight, values, V)

    # Start the timer to calculate cpu time taken for KnapSack
    # and optimal subset (backtracking)
    start = time.time()
    KS(capacity, weight, values, len(values))
    print("Dynamic Programming Time Taken:", time.time() - start,  "seconds")

main()
