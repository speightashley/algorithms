#  This is wrong

c = 3
r = 4

# data = ([0] * c) * r

# print(data)

########################################################

# Also wrong
data = [[0] * c] * r

print(data)
print(f"ID for the entire struct {id(data)}")
print(id(data[0]))  # Same ID as below and below that
print(id(data[1]))
print(id(data[2]))

##########################################################

# The correct way

data2 = [[0] * c for _ in range(r)]
print(data2)
print(id(data2))
print(id(data2[0]))  # Different ID from every other list in the array
print(id(data2[1]))
print(id(data2[2]))
