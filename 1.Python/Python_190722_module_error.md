# Python_190722_module_error

# 모듈

모듈은 파이썬 정의와 문장들을 담고 있는 파일입니다. 파일의 이름은 모듈 이름에 확장자 `.py` 를 붙입니다.

## 패키지

- jupyter notebook 파일트리화면에서 New > Folder
- 다음과 같은 폴더구조 생성

```python
myPackage/
    __init__.py
    math/
        __init__.py
        formula.py
    web/
        __init__.py
        url.py
```

- 패키지는 '점으로 구분된 모듈 이름' 를 써서 파이썬의 모듈 이름 공간을 구조화하는 방법입니다. 예를 들어, 모듈 이름 `myPackage.math` 는 `myPackage` 라는 이름의 패키지에 있는 `math` 라는 이름의 서브 모듈을 가리킵니다.

- 단, 파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서 `__init__.py` 파일이 필요합니다. 이렇게 하는 이유는 string 처럼 흔히 쓰는 이름의 디렉터리가, 의도하지 않게 모듈 검색 경로의 뒤에 등장하는 올바른 모듈들을 가리는 일을 방지하기 위함입니다.

- `import`는 다양한 방법으로 할 수 있습니다.

## `from` *모듈명* `import` `*`

해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져옵니다.



## 수학 관련 함수(math)

다음의 기본 함수는 `import`없이 활용하였습니다.

```
sum`, `max`, `min`, `abs`, `pow`, `round`, `divmod
```



## 난수 발생관련 함수(random)

`random.random()` 0~1 사이의 랜덤한 수를 생성!

#### seed

#### 경우에 따라서(보통 디버깅 등을 위해 ) 동일한 순서로 난수를 발생시켜야 할 경우가 있다. 

#### 난수 발생을 위해서는 적절한 시드(seed)를 난수발생기에 주어야 한다. 

#### 만약 시드가 같다면 동일한 난수를 발생시키게 된다. 

#### 시드 설정을 하지 않으면 현재 시간을 기반으로 만든다.

random.seed(1)

같은 seed를 가지고 있다면 계속해서 같은 순서로 값들이 나온다.



# 날짜 관련 모듈

## datetime

```python
from datetime import datetime
today = datetime.now()
print(today)
```

```
2019-07-22 15:16:30.606220
```



```python
today = datetime.today()
print(today)
```

```
2019-07-22 15:16:47.979357
```



```python
print(datetime.utcnow())
```

해외의 서버와 연동하거나 할 때 필요한 utcnow()

| 형식 지시자(directive) |                   의미 |
| ---------------------: | ---------------------: |
|                     %y |        연도표기(00~99) |
|                     %Y |         연도표기(전체) |
|                     %b |          월 이름(축약) |
|                     %B |          월 이름(전체) |
|                     %m |         월 숫자(01~12) |
|                     %d |              일(01~31) |
|                     %H |     24시간 기준(00~23) |
|                     %I |     12시간 기준(01~12) |
|                     %M |              분(00~59) |
|                     %S |              초(00~61) |
|                     %p |              오전/오후 |
|                     %a |             요일(축약) |
|                     %A |             요일(전체) |
|                     %w | 요일(숫자 : 일요일(0)) |
|                     %j |  1월 1일부터 누적 날짜 |



| 속성/메소드 |                 내용 |
| ----------: | -------------------: |
|       .year |                   년 |
|      .month |                   월 |
|        .day |                   일 |
|       .hour |                   시 |
|     .minute |                   분 |
|     .second |                   초 |
|  .weekday() | 월요일을 0부터 6까지 |



- 특정한 날짜 만들기

```python
datetime(year, month, day, hour, minute, second, microsecond)
```



## timedelta - 시간 계산할 때 사용하는 모듈

```python
from datetime import timedelta
today + timedelta(days=100)
```

```result
datetime.datetime(2019, 10, 30, 15, 16, 47, 979357)
```





# Errors and Exceptions

- 발생할 수 있는 오류와 예외처리를 확인해봅시다.

가장 많이 만날 수 있는 에러로 발생한 `파일 이름`과 `줄`, `^`을 통해 파이썬이 읽어 들일 때(parser)의 문제 발생 위치를 표현한다.

반드시 표시되는 위치에 표시해주지는 않지만 python이 비교적 정확한 편이다.

EOL 오류(따옴표 오류) : SyntaxError: EOL while scanning string literal

EOF 에러(괄호 닫기 오류) : SyntaxError: unexpected EOF while parsing

문법 오류 : SyntaxError: invalid syntax





## 예외 (Exceptions)

- 문법이나 표현식이 바르게 되어있지만, 실행시 발생하는 에러입니다.
- 아래 제시된 모든 에러는 Exception을 상속받아 이뤄집니다.

0으로 나누는 오류  :  ZeroDivisionError: division by zero

변수 이름 오류 : NameError: name 'asdf' is not defined

타입에러 : TypeError: unsupported operand type(s) for +: 'int' and 'str'

함수호출 타입에러 : TypeError: type str doesn't define __round__ method

값 에러 : ValueError: invalid literal for int() with base 10: '3.5'

인덱스 에러 : IndexError: list index out of range     -> 리스트에서 특히 많이 발생!!



# 예외 처리

## 기본 - `try` `except`

`try` 구문을 이용하여 예외 처리를 할 수 있습니다.

기본은 다음과 같은 구조를 가지고 있습니다.

```python
try:
    codeblock1
except 예외:
    codeblock2
```

- `try`절이 실행됩니다.

- 예외가 발생되지 않으면, `except`없이 실행이 종료 됩니다.

- 예외가 중간에 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행됩니다.

  

## 에러 문구 처리

- 에러 문구를 함께 넘겨줄 수 있습니다.

```python
try:
    codeblock1
except 예외 as err:
    codeblock2
```



## `else` -> 에러가 발생 안하면 실행!

- 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용합니다.
- 모든 except 절 뒤에와야 합니다.
- try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절합니다.

```python
try:
    codeblock1
except 예외:
    codeblock2
else:
    codeblock3
```



## `finally` -> 에러발생여부와 관계없이 실행!

- 반드시 수행해야하는 문장은 `finally`를 활용합니다.
- 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용합니다.
- 예외의 발생 여부과 관계없이 try 문을 떠날 때 항상 실행됩니다.

```python
try:
    codeblock1
except 예외:
    codeblock2
finally:
    codeblock3
```



## Gitlab 사용

```gitbash
git remote -v  # 현재 원격으로 연결되어있는 변수와 주소를 연결시켜 보여줌
git remote add gitlab https:-----  # gitlab이라는 변수와 사이트서버를 연결시켜줌
git diff # 현재 master폴더와 서버에 저장된 파일이 다른부분이 있는지 확인시켜줌
```

