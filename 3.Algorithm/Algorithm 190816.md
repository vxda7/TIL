# Algorithm 190816 

### ArraySum

```
for i : 0 - > 99
	s = 0 #행의 합. 행이 바뀔 때 초기화
	for j : 0 -> 99
		s = s + arr[i][j]
	if maxV  < s # 행의 합과 비교
		maxV = s
		
#열의 합
for i : 0 -> 99 #열
	s = 0 #열의 합. 열이 바뀔 때 초기화
	for j:0 -> 99 # 행
		s = s + arr[i][j]
	if maxV < s #열의 합과 비교
		maxV = s
		
#두 대각선의 합
s = 0 #오른쪽 아래 방향
for i : 0 -> 99
	s = s + arr[i][i]
if maxV < s
	maxV = s
s = 0 # 왼쪽 아래 방향
for i : 0 -> 99
	s = s + arr[i][99-i]	# NxN인 경우 arr[i][N-1-i]
	
```



### Selection Sort

```
#N개의 원소
#최소값을 찾는 구간의 시작인덱스
for i :0 -> N-2
	minidx = i # 각 구간의 시작인덱스
	for j : i+1 -> N-1 #최소값을 찾는 구간
		if arr[minidx] > arr[i]
			minidx = i
	arr[i], arr[minidx] = arr[minidx], arr[i]
```



```

```

