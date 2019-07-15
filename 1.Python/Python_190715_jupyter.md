# Python_190715_Jupyter

#### --자리이동--

## Jupyter

```bash
pip install jupyter		#주피터 설치!
jupyter notebook		#주피터 실행!
```

위아래 순서가 아니라 어떤 셀을 먼저 실행했는지 실행순서에 따라서 결정된다.

`Alt + Enter` 작동하고, 아래항목 수정

`Crtl + Enter` 작동

`Shift + Enter`  작동하고, 다음으로 넘어가기

## python

`PEP-8`

`type()` : 괄호안의 변수가 어떤 형인지 알려준다.

`id()` : 괄호안의 변수의 메모리 주소를 알려준다.

1) `%-formatting`

2) [`str.format()`](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

`.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

```
# name 변수에 이름을 입력해봅시다.
name="김승연"
```

```
김승연
```

```
# %-formatting을 활용해봅시다.
print("%s" %name)
```

```
김승연
```

```
# str.format()을 활용해봅시다.
print("{0}".format(name))
```

```
김승연
```

```
# f-string을 활용해봅시다.
print(f"{name}")
```

```
김승연
```

`datetime`

`//` : 몫

`%` : 나머지

3.0000000000000000000000001==3

True

적은 숫자는 영향을 안미침

`+` 는 숫자만 더해지는게 아니라 문자를 연결할 수도 있다.



#### 이스케이프 문자열

`\n` 줄바꿈

`\t` 탭

`\0` 널

`\\`	\

`\'` 단일인용부호(')

`\"` 이중인용부호(")



### is

파이썬에서 -5부터 256까지의 id는 동일합니다.



```python
a = 1000
b = 1000
print(a is b)
```

`False`



```python
a = 10
b = 10
print(a is b)
```

`True`



### Tuple

immutable! 수정 불가능!

의자 바꿀 때 주로 쓰는 형식

x, y = 1, 2

x, y = y, x

무려 temp가 필요없음!!

### SET

세트는 수학에서의 집합과 동일하게 처리됩니다.

세트는 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없습니다.

**활용법**

```python
{value1, value2, value3}
```



### Dictionary

**활용법**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

- 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다.
- `{}`를 통해 만들며, `dict()`로 만들 수도 있습니다.
- `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.
- 

### Join

list 를 문자열로 바꾸어주는 함수!

![1563175943618](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563175943618.png)

![1563175973235](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563175973235.png)



## Today's Coding

상승장? 하락장?

```python
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
print(data)
opening_price = data['opening_price']
closing_price = data['closing_price']
min_price = data['min_price']
max_price = data['max_price']

diff = float(max_price) - float(min_price)

if float(opening_price) + diff > float(max_price):
    print("상승장")
else:
    print("하락장")

```



모음제거하기 방법1

```python
# 내가 아는 함수들을 이용한 풀이 조건식이 너무 길어짐!!

my_str = "Life is too short, you need python"
howlong = len(my_str)

for i in range(howlong):
    if my_str[i] == 'a' or my_str[i] == 'e' or my_str[i] == 'i' or  my_str[i] == 'o' or my_str[i] == 'u':
        print("",end="")
    else:
        print(my_str[i],end="")
```



방법2 - 리스트추가! - join!

```python
my_str = "Life is too short, you need python"
collection=['a', 'e', 'i', 'o', 'u']
result=[]

for i in my_str:
    if i not in collection:
        result.append(i)

print(''.join(result))
```



방법3 정답 - 문자열덧셈!

```python
# 선생님의 정답! - 새로운 함수없이 깔끔!
my_str = "Life is too short, you need python"
result = ''

vowels = ['a', 'e', 'i', 'o', 'u']

for char in my_str:
    if char not in vowels:
        result+=char
print(result)
```



개인정보보호

```python
phone = input()
if len(phone) != 11 or phone[0:3] != '010':
    print("핸드폰번호를 입력하세요")
else:
    print(f"*******{phone[-4:]}")
```



정중앙

```python
text = input()
howlong=len(text)

if(howlong%2==1):
    solution=int(howlong/2-0.5)    # 5개의 글자 중 가운데는 3번째이지만 리스트내부에서는
    print(text[solution])          #2가 되기때문에 2를나누고 0.5를 빼면 원하는 값이나옴
    
elif(howlong%2==0):
    solve=int(howlong/2)
    print(text[solve-1:solve+1])
```

