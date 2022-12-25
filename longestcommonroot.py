def longestCommonPrefix(strs: list[str]) -> str:
    number_of_words = len(strs)
    shortest_string = min(strs, key=len)

    for i in range(len(strs)):
        for j in range(len(shortest_string)):
            print(strs[i][j])










strings = ["flower", "flow", "flight"]

print(longestCommonPrefix(strings))
