# Python_190718_recursive

# 재귀 함수(recursive function)

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻한다.



## 팩토리얼 계산

> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성해봅시다.
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.



​			`𝑛!=∏𝑘=1𝑛𝑘n!=∏k=1nk`

​			`𝑛!=1∗2∗3∗...∗(𝑛−1)∗𝑛`



```python
# 아래에 코드를 작성해주세요.
def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n-1) * n
factorial(5)
```



## 피보나치 수열

> 피보나치 수열은 다음과 같은 점화식이 있다.
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해보자.

𝐹0=𝐹1=1F0=F1=1



𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2(𝑛∈{2,3,4,…})Fn=Fn−1+Fn−2(n∈{2,3,4,…})



1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

------

```
예시 입력)
fib(10)

예시 호출)
89
```



# 메소드 활용하기

## 변형

### `.capitalize()`, `title()`, `.upper()`

### `.capitalize()` : 앞글자만 대문자로 만들어 반환합니다.

### `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환합니다.

### `.upper()` : 모두 대문자로 만들어 반환합니다.

### `.lower()`: 모두 소문자로 만들어 반환합니다.

### `.swapcase()` : 대 ↔ 소문자로 변경하여 반환합니다.

위에 모든 것들은 원본을 훼손하지 않는다! 반환! Return!

### `.join(iterable)`

Iterable 을 해당 문자열을 separator 로 합쳐서 문자열로 반환합니다.

```python
print('!'.join('배고파'))
print('-'.join(['1', '2', '3', '4']))
```

```result
배!고!파
1-2-3-4
```

### `.replace(old, new[, count])` 글씨 변환

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다.

### `strip([chars])` 글씨제거

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip) 오른쪽을 제거합니다(rstrip)

지정하지 않으면 공백을 제거합니다.



## 탐색 및 검증

### `.find(x)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

```python
'applpe'.find('p',3)
```

```result
4
```

### `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.

### `.split()`:문자열을 특정한 단위로 나누어 리스트로 반환합니다.



## 다양한 확인 메소드 : 참/거짓 반환

```
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
dir('string')
```





# 리스트 메소드 활용하기

## 값 추가 및 삭제

### `.append(x)` 리스트에 값 추가!

리스트에 값을 추가할 수 있습니다.

### `.extend(iterable)` 리스트끼리 합체!

리스트에 iterable(list, range, tuple, string*유의*) 값을 붙일 수가 있습니다.

### `insert(i, x)`

정해진 위치 `i`에 값을 추가합니다.

### `remove(x)`

리스트에서 값이 x인 것을 삭제합니다.

### `.pop(i)`

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.



## 탐색 및 정렬

### `.index(x)`

x 값을 찾아 해당 index 값을 반환합니다.

### `.count(x)`

원하는 값의 갯수를 확인할 수 있습니다.

### `.sort()`

정렬을 합니다.

`sorted()`와는 다르게 원본 list를 변형시키고, None을 리턴합니다.

### `reverse()`

반대로 뒤집습니다. (정렬 아님)



## 복사

### copy[¶](http://localhost:8888/notebooks/notes/04.data_structure.ipynb#copy)

> [pythontutor](http://pythontutor.com/visualize.html#code=lunch %3D {'김밥천국'%3A '치즈라면', '김가네'%3A '제육볶음'} print(lunch) dinner %3D lunch dinner['김밥천국'] %3D '참치김밥' print(lunch)&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=[]&textReferences=false)를 활용하여 자세하게 알아봅시다.

- 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다.

```
num = [1, 2, 3]
```

- 위와 같이 변수를 생성하면 hong이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.
- 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

따라서, 복사를 하고 싶을 때에는 다음과 같이 해야한다.

```python
# 리스트를 복사해봅시다.
a = [1, 2, 3]
b = a[:]
b[0] = 123
print(a)
```

```
[1, 2, 3]
[123, 2, 3]
```

- 하지만, 이렇게 하는 것도 일부 상황에만 서로 다른 얕은 복사(shallow copy)입니다.

  

```python
# 2차원 배열을 복사해봅시다.
a = [1, 2, [9, 10]]
b = list(a)
b[2][0] = 9999
print(a)
```

```
[1, 2, [9999, 10]]
```

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



## `.clear()`

리스트의 모든 항목을 삭제합니다.



# List Comprehension

List를 만들 수 있는 간단한 방법이 있습니다.



### 세제곱리스트

> 다음의 리스트를 만들어보세요.

- 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`









































