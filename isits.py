def isit(get):
    count=0
    howlong=get+1
    for i in range(1,howlong):
        if get%i == 0:
            count+=1
    if count==2:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")
        
get = int(input())

result = isit(get)