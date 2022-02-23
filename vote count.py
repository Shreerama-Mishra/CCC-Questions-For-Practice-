a=int(input())
b=str(input())

# step 1: move across the string from left to right
# step 2: count each and every character
# step 3: get the total for each character and compare


# of a in the string
# of b in the string
aCount=0
bCount=0
      
for i in range (a):
    if b[i] == 'A':
      aCount = aCount + 1

    elif b[i] == 'B':
        bCount = bCount + 1

if aCount>bCount:
    print("A")
            
elif bCount>aCount:
    print("B")

else:
    print("Tie")
                  
