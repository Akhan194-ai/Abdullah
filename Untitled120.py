#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Initial population represented as a list of lists
S = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
]

print("Initial Population S:", S)

# Function to calculate fitness
def calfitness(S):
    fit = []  # List to store fitness of each individual
    total = 0  # Total fitness
    print("Fitness Calculation:")
    for i in S:
        fitness = i.count(1)  # Fitness of an individual is the count of 1s
        fit.append(fitness)
        total += fitness
    print("Fitness of individuals:", fit)
    print("Total fitness:", total)
    return fit

# Calculate fitness for the initial population
fit = calfitness(S)

# Arrange the population in descending order of fitness
print("Arranging in Descending order based on fitness")
desc = S.copy()  # Create a copy of S for sorting
# Sort individuals based on their fitness in descending order
for i in range(len(desc)):
    for j in range(i + 1, len(desc)):
        if desc[i].count(1) < desc[j].count(1):
            desc[i], desc[j] = desc[j], desc[i]  # Swap if fitness of desc[j] is greater than desc[i]

print("Sorted population (desc):", desc)

# Cross over after 2 points (single-point crossover example for simplicity)
print("Crossover after 2 points:")
for i in range(3):  # Perform crossover on the first 3 elements
    desc[0][i], desc[3][i] = desc[3][i], desc[0][i]  # Swap first 3 bits between individual 0 and 3
    desc[4][i], desc[5][i] = desc[5][i], desc[4][i]  # Swap first 3 bits between individual 4 and 5

# Swap the entire individuals (0 and 3, 4 and 5)
desc[0], desc[3] = desc[3], desc[0]
desc[4], desc[5] = desc[5], desc[4]

print("s1 and s4 after crossover")
print("s1 =", desc[0], "s4 =", desc[3])
print("s5 =", desc[4], "s6 =", desc[5])

# Crossover between S2 and S3 after the 4th point
print("Crossover between S2 and S3 after the 4th point:")
for i in range(4, 10):  # Perform crossover from the 4th point onwards (index 4 to 9)
    desc[1][i], desc[2][i] = desc[2][i], desc[1][i]  # Swap bits between individual 1 (S2) and individual 2 (S3)

print("s2 and s3 after crossover")
print("s2 =", desc[1], "s3 =", desc[2])

# Mutation
print("Mutation:")
for i in range(6):  # Iterate over 6 individuals
    for j in range(2):  # Iterate over the first two elements (to mutate first two bits)
        if desc[i][j] == 0:
            desc[i][j] = 1  # Change 0 to 1
        else:
            desc[i][j] = 0  # Change 1 to 0

print("Population after mutation:", desc)

# Calculate fitness after applying crossover and mutation
fit2 = calfitness(desc)

# Compare fitness before and after applying Genetic Algorithm
if sum(fit) < sum(fit2):
    print("Fitness is greater after applying Genetic Algorithm")
else:
    print("Fitness is greater before applying Genetic Algorithm")



# In[ ]:




