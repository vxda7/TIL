# Python_190717_function

## 함수 기본 값(Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

**활용법**

```python
def func(p1=v1):
    return p1
```

![1563326459665](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563326459665.png)

- 단, 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.
- 항상 마지막 매개변수에 default를 넣을 것!



## 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.

```python
# 키워드 인자 예시
def greeting(age, name='john'):
    print(f'{name}은 {age}살입니다.)
```



- 단 아래와 같이 활용할 수는 없습니다. 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.

```python
greeting(age=24, '철수')
```

```result
 File "<ipython-input-11-d457a6f39e1c>", line 1
    greeting(age=24, '철수')
                    ^
SyntaxError: positional argument follows keyword argument
```





## 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다.

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다.

**활용법**

```python
def func(*args):
```

arguments : 인자들의 약자



## 정의되지 않은 키워드 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
```



우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다. 

![1563329371581](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563329371581.png)



