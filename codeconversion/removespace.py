str = input("Enter the string: ")
newstr = ""
i = 0
while i < len(str):
    while i < len(str) and str[i] == ' ':
        i += 1
    if i < len(str):
        newstr += str[i]
        i += 1
print("\nString after removal of blank spaces is:", newstr)
