# StartCamp-Day3

## 파일 입출력

`f=open("student.txt",'w')` open하기

`f.write("안녕하세요")` 파일 쓰기

`f.close()` open을 쓰면 반드시 `close()`를 해줘야한다.

위에서 보완해서 `close()`를 반드시 안써줘도 되는 것

```python
with open("ssafy.txt",'w') as f:
    f.write("싸피 파이팅!!!")
```

`with open() as f:` 를 이용하면 따로 close() 해주지 않아도 된다.

`'w'`	write의 약자로 덮어쓰기가 된다.

`'r'`	read의 약자로 읽기만 된다.

`'a'`	 append의 약자로 원래 있던 항목에 추가가 된다.



## CSV

표형태로 엑셀처럼 열게 해주는 프로그램

`import csv` 	csv를 쓰려면 import 필요

```python
with open("exchange.csv",'w',encoding='utf-8',newline="") as f:	
    #encoding='utf-8'로 한글을 사용가능 newline은 없으면 뒤에 한칸이 늘어나는 버그있음(window한정)
    csv_writer = csv.writer(f)	#csv.writer가 csv에 얘들을 적어주는 write 역할을 수행한다.
    for r in tr:
        print(r.select_one('.tit').text.strip())
        print(r.select_one('.sale').text)
        row=[r.select_one('.tit').text.strip(), r.select_one('.sale').text]
        csv_writer.writerow(row)	#csv.writer에게 wirterow  -> 한 줄만 써줘 를 실행함
```



## HTML

Hyper Text Markup Language

태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름> -> 모든 html의 형식 속성

h tab : head 머리글자

a tab : anchor link 시켜주는 것

href : hyper reference

ol : ordered list

```html
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        필수코드들!
    </body>
</html>
```

`<link rel="stylesheet" href="./intro.css">`  : head에 넣어서 원하는 곳과 연결해주는 코드

`id`와 `class` 모두 특정한 효과를 줄 수 있는데 우선순위는 `id`에 있다.

한 html문서에 `id`이름은 한개씩만 존재할 수 있다.



## CSS

```css
/* 여기는 CSS파일입니다!!! */
h1 {
    background-color:red;
}
a {
    color:brown;
}
.blue {
    background-color:blue;
    font-stretch:expanded;
    box-shadow: 5px 10px #888888;
}
#git {
    background-color:rgb(78, 116, 71);
    font-size: 150%
}

```



## 내 블로그 사이트 생성

https://vxda7.github.io/index.html





## 정렬



## 코드

첫 html

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="./intro.css">
    </head>
    <body>
        <h1>HTML</h1>
        <h1 class="blue">CSS</h1>
        <h2 class="blue">Hyper Text Markup Language</h2>
        <a href="https://naver.com/">네이버</a>
        
        <!-- <태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름> -->
        
        <h3 class="blue">우리가 공부한 것 <strong>ssafy</strong></h3>
        <ol>
            <li><strong><i>파이썬</i></strong></li>
            <li>HTML</li>
            <li id="git" class="blue">Git</li>
        </ol>
    </body>
</html>
```

