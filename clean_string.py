def clean_string(s):
    clean_list = []
    for char in s:
        if char == "#":
            if clean_list:
                clean_list.pop()
            continue
        clean_list.append(char)
    return "".join(clean_list)


s1 = "abc#d##c"
s2 = "abc##d######"
s3 = "#######"
s4 = ""

print(clean_string(s1))
print(clean_string(s2))
print(clean_string(s3))
print(clean_string(s4))

