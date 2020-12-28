

start_n = int(input("insert start_n"))
end_n   = int(input ("insert end_n"))

n=start_n
if n>=end_n:
    while n >= end_n:
        print(n)
        n -=1
else:
    while n <= end_n:
        print(n)
        n +=1