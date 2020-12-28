
n = 1

while n <= 64:
    if n>0 and n<=8 and n % 2 == 0 or n>16 and n<=24 and n % 2 == 0 or n>32 and n<=40 and n % 2 == 0 or n>48 and n<=56 and n % 2 ==0:
        print(" # ",end="")
        
    else:
        print(" * ", end="")
    if n%8==0:
        print()
    n+=1

    