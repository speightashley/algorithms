import collections

D = collections.deque()

D.appendleft(1)
D.appendleft(0)
D.append(2)
D.count(1)

print(D)

for x in D:
    print(x)
