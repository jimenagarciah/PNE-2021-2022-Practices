n1 = 0
n2 = 1
for i in range(2, 11):
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
