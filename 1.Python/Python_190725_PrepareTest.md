# Python_190725_PrepareTest

#### complex(복소수)

복소수는 허수부를 `j`로 표현한다.

```python
a = 3 - 4j
type(a)
```

```result
complex
```



#### 여러줄 출력

```python
a = "안녕하세요"
print(f"""
{a}
반갑습니다.
""")
```

```result
안녕하세요
반갑습니다.
```



## `while` 문

`while`문은 조건식이 참(True)인 경우 반복적으로 코드를 실행합니다. 

**while 문은 종료조건을 반드시 설정해주어야 합니다.**

거짓이 나올때까지 반복!!



### enumerate()

```python
# enumerate()를 활용해서 출력해봅시다.
lunch = ['짜장면', '초밥']
for idx, menu in enumerate(lunch):
    print(idx, menu)
```

```result
0 짜장면
1 초밥
```





## 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.

```python
# 키워드 인자 예시
def greeting(age, name='john'):
    print(f'{name}은 {age}살입니다.')
    
greeting(20,'change')
greeting(name = 'change', age = 20)
```

```
change은 20살입니다.
change은 20살입니다.
```

- 단 아래와 같이 활용할 수는 없습니다. 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.

```python
greeting(age=24, '철수')
```

```python
File "<ipython-input-4-d457a6f39e1c>", line 1
    greeting(age=24, '철수')
                    ^
SyntaxError: positional argument follows keyword argument
```





## 정의되지 않은 키워드 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
```





### `.join(iterable)`

Iterable 을 해당 문자열을 separator 로 합쳐서 문자열로 반환합니다.

```python
# 아래에 코드를 작성하세요.
print('!'.join('배고파'))
print('-'.join(['1', '2', '3', '4']))
```

```
배!고!파
1-2-3-4
```



### `.find(x)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다

### `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.





### `.remove(x)` : 리스트에서 값이 x인 것을 삭제합니다. 없으면, 오류발생



- 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야합니다.
- 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경됩니다.

```python
# 깊은 복사를 사용해봅시다.
import copy
a = [1, 2, [9, 10]]
b = copy.deepcopy(a)
b[2][0] = 99999
print(a)
print(b)
```

```
[1, 2, [9, 10]]
[1, 2, [99999, 10]]
```

