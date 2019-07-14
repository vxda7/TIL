
get = int(input())
result = [1,1]
a=0
for i in range(2, get):
    temp = result[a]+result[a+1]
    result.append(temp)
    a+=1 

print(result)