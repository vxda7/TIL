# StartCamp-Day2

## Session4 : Python 심화

### CLI

#### 명령어

`ls` : list 보여주기

`cd` : change directory 폴더이동

`mkdir` : 디렉토리 생성

`echo` : 문자열 나열

`rm` : 지우기	# rm -r	: 폴더지우기 recursive 재귀

`exit` : 터미널 종료

`clear` : 터미널 청소

`pwd` : present working directory

`touch` 파일을 만드는 명령어

`code` 컴파일러 열기

### 정보 스크랩

```web-idl
queary=	#뒤에서 원하는 검색어의 결과물을 보여준다.
```



```bash
pip  install requests	#원하는 것을 사오는 코드
```

`import requests` 웹에 무언가를 요구하는 코드 웹에서 응답(response)을 준다.

`from bs4 import BeautifulSoup` bs4라는 큰 툴안에 있는 `BeautifulSoup`라는 도구를 꺼내옴.

`soup=BeautilfulSoup(response,'html.parser')` html을 나눠서 python이 읽기쉽게 만들어 soup에 저장.

`soup.select('')` 웹브라우저에서 원하는 부분을 `selector`를 통해서 가져옴.

`.text` 원하는 html 가져온 부분에서 <>와 <>사이에 있는 것을 가져옴

## 새로운 키워드

환경변수

CLI  :  Command Line Interface 명령 줄 인터페이스

## Gitub 사용하기

```bash
git add . 	# 현재 폴더 추가!

git commit -m "add README.md"	# commit는 
```

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

환율

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

실시간 네이버

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

