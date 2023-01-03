import sys

data = []
temp = 0

for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    if b > temp:
        print(f"Length: {a:3d}; Size in bytes: {b:4d}")
    data.append(None)
    temp = b
