n = 10

if n >= 0:
    param = n
else:
    param = -n
result = foo(param)

param = n if n >= 0 else -n  # Can be written like this
result = foo(param)

# can also be written like this:

result = foo(n if n >= 0 else -n)
