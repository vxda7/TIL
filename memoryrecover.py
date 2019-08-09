numbers = int(input())

def check(gets):
    pass

for number in range(numbers):
    gets = int(input().lstrip('0'))
    result=0
    if len(set(gets)) == 1:
        result=1
    result=check(gets)
    print("#{0} {1}".format(number+1, result))