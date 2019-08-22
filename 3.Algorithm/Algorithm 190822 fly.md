# Algorithm 190822 fly

### X - fly

```python
# 파리채가 X자 모양이라면(크기는 K)
# 부분 배열의 왼쪽 모서리 좌표가 i, j 일 때,
s = 0
for m in range(K):
    s += fly[i+m][j+m]  # 오른쪽 아래 방향
    s += fly[i+m][j+K-1-m]
# K가 홀수인 경우 가운데 원소가 두번 더해지므로
if K%2 == 1:
    s -= fly[i + K//2][j + K//2]    # 한개를 빼줌
```

