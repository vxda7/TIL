def mul(a, b):
    if b==1:
        return a
    else:
        b-=1
        a*=mul(a,b)
        return a
    
for i in range(10):
    numbers = int(input())
    gets = list(map(int,input().split()))
    print("#{0} {1}".format(i+1,mul(gets[0], gets[1])))