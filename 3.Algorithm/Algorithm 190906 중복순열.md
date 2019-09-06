# Algorithm 190906 중복순열

```python
def npr(n,k,m):

    # n이 하나씩 증가하다가 k와 같아 지면 다 뽑히는 것이므로...
    if n == k:
        print(p)
    else:
        for i in range(m):
            if used[i] == 0:  # 사용하지 않은 숫자이면
                used[i] = 1   # 그 부분을 사용하면서 사용했다는 1을 준다.
                p[n] = i      # n번째에 i 값을 저장한다.
                npr(n+1,k,m)  # 다음 자리 수를 본다.
                used[i] = 0   # 재귀로 다시 돌아왔을 때 그 자리 수를 사용할 수 있게 해준다.

TC = int(input())
for t in range(TC):
    N = int(input()) # 1 ~ N의 숫자
    k = int(input()) # 몇 개를 뽑을 것인가
    used = [0]*N    # 1 ~ N의 숫자의 각각을 1 또는 0으로 카운트 해준다.(0은 사용가능, 1은 이미 사용했다.)
    p = [0]*k       # k개를 뽑아 저장할 리스트

   #npr = (0에서 부터 시작한다, k 개를 뽑는다, N까지의 정수 중에서)
    npr = (0, k, N)
```

