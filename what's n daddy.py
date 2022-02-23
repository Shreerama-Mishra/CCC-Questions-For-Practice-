n = int(input())

#POSSIBLE COMBINATIONS
# 1 - (1,0)
# 2 - (2,0) , (1,1)
# 3 - (3,0) , (2,1)
# 4 - (4, 0) , (3, 1) , (2,2)
# 5 - (5, 0) , (3, 2,) ,(4,1)
# 6 - (6, 1) , (4, 2), (3,3)
# 7 - (5,2) , (4,3)
# 8 - (3,5), (4, 4)
# 9 - (5,4)
# 10 - (5,5)

if n==10:
    print(1)

elif n==9:
    print(1)

elif n==8:
    print(2)

elif n==7:
    print(2)

elif n==6:
    print(3)

elif n==5:
    print(3)

elif n==4:
    print(3)

elif n==3:
    print(2)

elif n==2:
    print(2)

elif n==1:
    print(1)
