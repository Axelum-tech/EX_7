start  = 1
finish = 10

a_stat_1 = 1
a_stat_2 = 7

car      = 5

step = start
print ("\n")
while step<=finish:
    if step==finish:
        print(step)
    else:
        print(step,end="")
        print("---", end="")
    step += 1

step = start
print()

while step<=finish:   
    if step==a_stat_1 or step==a_stat_2:
        print("a", end="")
    else:
        print(" ", end="")
    print("---",end="")
    step+=1
       
step = start
print ("\n")
while step<=finish:   
    if step==car:
        print("c", end="")
    else:
        print(" ", end="")
    print("---",end="")
    step+=1
        
print ("\n")