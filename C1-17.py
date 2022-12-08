"""Had we implemented the scale function (page 25) as follows, does it work
properly?"""


def scale(data, factor):
    for val in data:
        val *= factor


my_list = [1, 3, 6, 7]

print(scale(my_list, 5))

# No it doesn't work because it doens't return anything and val is only within the scope of the function
