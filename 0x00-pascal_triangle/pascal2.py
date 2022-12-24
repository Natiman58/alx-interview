n = int(input('please enter the number of rows: '))

list1 = []
"""
    row is i
    column is j
"""
for i in range(n):
    temp_list = []
    for j in range(i+1):
        """ For the begining the end values append 1"""
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            """For the inbetween values append append the sum of the immediate prev row """
            temp_list.append(list1[i-1][j-1] + list1[i-1][j])
    
    """Add the inner lists  into the bigger list"""
    list1.append(temp_list)
print(list1)

for i in range(n):
    """To print the spaces b/n each row"""
    for j in range(n-i-1):
        print(format(" ", "<2"), end="") 
    for j in range(i+1):
        """There is a space b/n each value"""
        print(format(list1[i][j], "<4"), end="")
    print()
