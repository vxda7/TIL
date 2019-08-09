def mul(a, b):
    if b==1:
        return a
    else:
        b-=1
        a*=mul(a,b)
    


result=[]
for i in range(10):
    numbers = int(input())

    gets = list(map(int,input().split()))
    result.append(mul(gets[0], gets[1]))

#출력
cnt=1
for res in result:
    print(f"#{cnt} {res}")
    cnt+=1