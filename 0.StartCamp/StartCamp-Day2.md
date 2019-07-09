# StartCamp-Day2

## Session4 : Python 심화

### CLI - Command Line Interface - Git Bash

#### 명령어

`ls` : list 보여주기

`cd` : change directory 폴더이동

`mkdir` : 디렉토리 생성

`echo` : 문자열 나열

`rm` : 지우기	# rm -r	: 폴더지우기 recursive 재귀

`exit` : 터미널 종료

`clear` : 터미널 청소

`pwd` : present working directory

`touch` 파일을 만드는 명령어 ex) `touch exchange.py`

`code` 컴파일러 열기



### 정보 스크랩

```web-idl
queary=	#뒤에 나오는 단어에서 원하는 검색어의 결과물을 보여준다.
```



```bash
pip  install requests	#원하는 것을 사오는 코드 여기서는 requests를 사옴
```

`import requests` 웹에 무언가를 요구하는 코드 웹에서 응답(response)을 준다.

`from bs4 import BeautifulSoup` bs4라는 큰 툴안에 있는 `BeautifulSoup`라는 도구를 꺼내옴.

`soup=BeautilfulSoup(response,'html.parser')` html을 나눠서 python이 읽기쉽게 만들어 soup에 저장.

`soup.select('')` 웹브라우저에서 원하는 부분을 `selector`를 통해서 가져옴.

`soup.select_one('')` Select는 배열로 가져오면 `select_one`은 한개로만 가져온다.

`soup.status_code('')` 내부에 가장 큰 객체의 html 문이 들어가고 200이 정상적인 상태이다. #.text조심할것

`.text` 원하는 html 가져온 부분에서 <>와 <>사이에 있는 것을 가져옴

인터넷 페이지에서 F12 이용해서 Crtl+Shift+C (왼쪽위 마우스) 를 활용 원하는 페이지에 더 자세하게 접속하고 문제에 주어져 있는 클래스 등에 접근해서 긁어온다.



## Gitub 사용하기

```bash
git init #지금 부터 이 폴더를 git으로 관리할 거야
git add . 	# 현재 폴더 추가!

git commit -m "add README.md"	# commit로 코멘트

#github들어가서 가장긴 줄 을 git bash 에 옮기고 치기	ex↓
git remote add origin https://github.com/vxda7/TIL.git

git push origin master


# git허브에서 다운로드한 주소를 복사해서
git clone https://github.com/vxda7/TIL.git
#위 코드를 적으면 복사됨
git pull origin master # 다른사람이 수정한 파일을 당겨오기!
```



## Git의 목적

- 버전관리

- Git을 통한 협업

  

## 새로운 키워드 및 사이트 및 프로그램

환경변수

CLI  :  Command Line Interface 명령 줄 인터페이스

Git Bash : cmd창 같이 생겨서 유닉스체계를 띄고 있음

Visual Studio Code : Python으로 코딩할 때 사용 하게 될 컴파일러



## 참고 코드

 브라우저

```python
import webbrowser

url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
my_keywords=["안동찜닭","순대국밥","불고기크림그라탕","돈가스매운냉면","치즈라면"]
other_keywords=["898b","888b","아이패드","갤럭시 노트10"]
for my_keyword in my_keywords:
    webbrowser.open(url+my_keyword)
```

코스피

```python
import requests
from bs4 import BeautifulSoup

response=requests.get("https://finance.naver.com/sise/").text
soup=BeautifulSoup(response,'html.parser')
kospi=soup.select('#KOSPI_now')
print(kospi)
```

파일명 바꾸기

```python
import os

os.chdir(r"C:\Users\student\startcamp\students")

for filename in os.listdir("."):
    os.rename(filename,filename.replace("SAMSUNG_","SSAFY_"))


# filenames=os.listdir(".")
# for number,filename in enumerate(filenames):
#     idx=filename.find(".txt")-3
#     print(number,filename)
```

환율 - 표 크롤링

``` python
import requests
from bs4 import BeautifulSoup

# response=requests.get(r"https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8").text
# soup=BeautifulSoup(response,'html.parser')
# exchange_rate_first="#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child("

# for i in range(1,21):
#     print(soup.select_one(exchange_rate_first+str(i)+") > th > a > span > em").text)
#     print(soup.select_one(exchange_rate_first+str(i)+") > td:nth-child(2) > span").text)

url = r"https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
tr = soup.select('tbody > tr')	

for r in tr:
    print(r.select_one('.tit').text.strip())
    print(r.select_one('.sale').text)
```

실시간 네이버 - list 크롤링

```python
import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.naver.com/").text
soup=BeautifulSoup(response,'html.parser')

j=5
for i in range(1,21):
    if i>10:
        j=6
    ranking=soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child("+str(j)+") > li:nth-child("+str(i)+") > a.ah_a > span.ah_k")
    print(ranking.text)
```

크롤링한것

```html
#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(1) > th > a > span > em
#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(2) > th > a > span > em
	서로 다른 부분을 찾아서 코드를 분석하기!
#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(1) > td:nth-child(2) > span
#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(2) > td:nth-child(2) > span
```

