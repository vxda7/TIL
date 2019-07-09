# StartCamp-Day1

## 4차산업혁명
> 바뀌어가는 단어와 기술
### 소프트웨어의 발전

- 그딴거 없다 열심히 코딩하자
- 비교적 문법이 단순화 되어가고 있음

## 파이썬 기본문법
### 저장

```python
a=10 #숫자 저장 a라는 상자에 10이라는 숫자를 담아둔다
```



###  if문(조건문)

```python
if(True):
	print("if문 안쪽입니다.")
elif(True):
    print("추가 if문은 이렇게")
else
	print("남은 것들을 한번에 처리하는건 이렇게")
```



###  내장함수

`print()`는 파이썬이 가지고 있는 내장함수이다.

`for i in range(5)` 는 4번 반복! 5는 포함 안함! 

`enumerate()`반복문 사용 시 몇번째 인지 확인하는 반복문!

`for p in enumerate(t):`	`t=[1, 5, 7, 33,  39 , 52]`

​	`print(p)`

와 같으면

(0, 1)

(1, 5)

(2, 7) 

.

.

.	처럼 나온다



###  반복

`for i in range(5)` 

range는 0이 Default 5를 넣으면 5보다 작은 값까지 반복한다.

`while` 은 거짓일 될때까지 계속 반복한다

```python
i=0
while i<5
	i++
print i

# 5
```

i 는 0에서 4까지 반복

### 리스트

```python
list_number=[1,2,3,4,5]
list_number.append(6)
print(list_number)

# [1, 2, 3, 4, 5, 6]
```

### 랜덤

 `choice=random.choice(menu)` menu라는 리스트에서 무작위로 한가지를 추출하는 함수

`result=random.sample(lotto,6)` lotto라는 리스트에서 6가지 숫자를 **중복**없이 나열해줌



### 순서

`list_number.sort()`

list_number라는 리스트를 숫자가 작은순에서 큰순대로 나열해줌. 오름차순



### 새로운 키워드

- Beautiful Soup : 손쉽게 워하는 영역을 찾고, 특정 값을 추출할 수 있도록 한다.

  `from bs4 import BeautilfulSoup` 하단의 requests와 같이 씀

- parsing 파싱 : 추출을 원하는 페이지를 필요한 부분만 가져오는 것

- F - string 포멧 : 파이썬 3.6 이상에서 지원하는 최신 포멧방법

  ```python
  name='Bob'
  test=f'Hello {name}'
  print(test)
  
  # Hello Bob
  ```

- `import requests`  : 웹페이지에 원하는 정보를 요구할때 쓰는 라이브러리
- `import random` : 무작위적인 것을 추가할 때 필요한 라이브러리



### 참고코드

로또

```python
import random

numbers = range(1,46)
list_number=[]
lotto=random.choice(numbers)
for i in range(6):    #random.sample(range(1,46),6 이면 해결!)
    while lotto in list_number:
      lotto=random.choice(numbers)
    list_number.append(lotto)

list_number.sort()
print(f"추천 로또 당첨 번호는 {list_number} 입니다!")
```

미세먼지

```python
import requests
from bs4 import BeautifulSoup

url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.6'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print(f"{time} 기준 {location}의 미세먼지 농도는 {dust}입니다.")

# 아래에 코드를 작성해주세요
if dust>150:  #괄호를 써도되고 안써도된다.
    print("매우나쁨")  #띄어쓰기 4칸 탭 2번을 기본으로!
elif dust>80 and dust<=150:
    print("나쁨")
elif dust>30 and dust<=80:
    print("보통")
else:
    print("좋음")
  
print(url)
```

배달

```python
import random

# 원하는 식당과 전화번호를 {}안에 넣어주세요
# Dictionary 작성법↓
phonebook = {
  "모토이시":"062-571-7436",
  "수진초밥참치":"062-571-2228",
  "카페더테라스":"062-574-4040",
  "꽃담샤브":"062-531-4848",  #나중에 추가할 것을 생각해서 쉼표추가! training comma 에러가없네!
}

choice = random.choice(list(phonebook.keys()))
print(f"{choice} : {phonebook[choice]}")


phonebook = {
  '영암매력한우수완점':'062-383-8118',
  '신전떡볶이 광주수완점':'062-956-2334',
  '양동통닭':'062-471-9277',
  '광주식당':'062-962-8284 ',
  '회마켓':'062-952-2026',
  '원조나주곰탕50년':'062-951-3255'
}
```

실시간검색

```python
import requests
from bs4 import BeautifulSoup

html=requests.get('https://www.naver.com/').text
soup=BeautifulSoup(html,'html.parser')

result=soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for idx, title in enumerate(result, 1):
    print(idx,title.text)
```

