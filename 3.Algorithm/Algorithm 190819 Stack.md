# Algorithm 190819 Stack



stack은 뒤에서 부터 꺼내기 때문에 거꾸로 무언가를 만들거나 불러들일 때 사용하기 좋다.

##### push 알고리즘

```python
def push(item):
	s.append(item)
```

##### pop 알고리즘

```python
def pop():
	if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1);
```



#### 비트연산자

##### <<연산자

`1<<n` : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.

##### &연산자 and

`i&(1<<j)`: i의 j번째 비트가 1인지 아닌지를 리턴한다.



##### |연산자 or

`i|(1<<j)` : i의 j번째 비트를 1로 만들어준다.