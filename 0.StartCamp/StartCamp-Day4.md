# StartCamp-Day4

## FLASK

#### 플라스크를 이용해서 Hello world 서버에 올리기!

``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")		# 최상단을 의미하는 하나의 '/'
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "안녕하세요!!!"
```

- 플라스크 Framework

매우 가볍고 심플한 Framework 를 지향한다!

수정하고 나면 한번 서버를 껏다가 켜야 수정된 부분이 적용됨

`pip install flask` -> 플라스크는 서랍안에 없음

`FLASK_APP=app.py flask run` -> 서버 구동!  product 모드!

```python
if __name__ == '__main__':
    app.run(debug=True)
```

위 줄을 추가하고 열면 `python app.py` De-bug 모드!



#### flask와 html을 연결시켜주는 방법!

```python
from flask import Flask, render_template	#render_temlpate을 서랍에서 꺼내주기!



@app.route("/html_file")

def html_file():

​    return render_template('index.html')	#"templates" 폴더안의 index.html과 연결시켜줌
```



##### 다른 url에 다른 결과를 보여주는 방법! 

##### 변수전달!

```python
import flask import Flask, render_teplate
app = Flask(__name__)

@app.route("/greeting/<string:name>")
def greeting(name):
    return f"안녕하세요 {name}님!!"

@app.route("/cube/<int:num>")			#변수값을 주소창으로 받을 수도 있다!!!
def cube(num):
    return "%d의 세제곱은 %d입니다." %(num,num**3)

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)
# 요렇게 html로 넘겨줌
```

```html
<strong>{{num_html}}</strong>의 세제곱은 <i>{{cube_num_html}}</i>입니다.
```

요렇게 html에서 받아줌 ----> html 문법이 아닌 `render_template`를 활용한 문법 {{}} 넘겨받기!



## python technic

```python
@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1> 
    <h2>반갑습니다</h2>
    """
```

""" 이렇게 세개를 쓰면 줄을 바꿔도 하나의 공간으로 넣어줄 수 있다.



## HTML technic

! tab이면 기본으로 적어야할

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

가 적어진다.



#### HTML에서 if 문 쓰는 법

```html
<body>
    {% if name=="승연" %}
        <p style="color:fuchsia">{{name}}</p>야 안녕!!!
    {% else %}
        <p style="color:fuchsia">{{name}}</p>님 안녕하세요!!!
    {% endif %}
</body>
```



#### HTML web

`http://127.0.0.1:5000/ping?test=wow`

주소창에서 ? 뒤의 주소는 파라미터

```html
<form action="">
    <input type="text" name="test">		#http://127.0.0.1:5000/ping?test=wow
    <input type="submit">
    <input type="text">
</form>
```



##### HTML ping pong

```python
@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    user_input=request.args.get("test")
    return render_template("pong.html",user_input=user_input)

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def goolge():
    return render_template("google.html")
```



ping

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 핑입니다.</h1>
    <form action="/pong">
        <input type="text" name="test">
        <input type="submit">
        <input type="text">
    </form>
</body>
</html>
```



pong

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 퐁입니다.</h1>
    사용자가 방금 입력한 데이터는
    <p>{{user_input}}</p>
    입니다.
</body>
</html>
```



google 검색기능

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="https://www.google.com/search"> 
        <input type="text" name="q">	#구글에서 뒤에 검색하는 부분을 q로 나타내서 적어준다.
        <input type="text" name="hihi">
        <input type="submit">
    </form>
</body>
</html>
```



아스키 코드 아트 -> 특정 주소의 기능을 활용하는 방법

```python
@app.route("/result")
def result():
    raw_text = request.args.get('raw')
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url+raw_text).text
    return render_template("result.html",res=res)
```



```python
@app.route("/lotto_result")
def lotto_result():
    # 사용자가 입력한 정보를 가져오기
    numbers = request.args.get('numbers').split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))

    # user_number = [1,2,3,4,5,6]
    # 로또 홈페이지에서 정보를 가져오기
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()
    
    winning_numbers = []
    for i in range(1,7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonus_number = lotto_numbers['bnusNo']
    
    result = "1등"

    intersection = len(set(user_numbers) & set(winning_numbers))
    
    bo = len(set(user_numbers) & {bonus_number})
    
    if intersection == 6:
        result = "1등"
    elif intersection == 5:
        if bo == 1:
            result = "2등"
        else:
            result = "3등"
        pass
    elif intersection == 4:
        result = "4등"
    elif intersection == 3:
        result = "5등"
    else:
        result = "꽝"


    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, r=result, b=bonus_number)

```

집합과 교집합을 활용하여 서로 중복되는 부분이 얼마나 많은지 확인하는 코드.

하나의 숫자를 집합화 할때는 `set()` 함수를 쓰지 않고 {} 중괄호에 싸준다.



## Ngrok

다른 사람들에게 서버를 공유해주는 프로그램

git bash를 통해서 만든 웹사이트를 공유해주고 Ngrok을 실행시키면 다른 사람들에게 공유해 줄 수 있다.



## JSON - WIKI

**JSON**(**제이슨**[[1\]](https://ko.wikipedia.org/wiki/JSON#cite_note-Pronunciation-1), JavaScript Object Notation)은 [속성-값 쌍](https://ko.wikipedia.org/w/index.php?title=속성-값_쌍&action=edit&redlink=1)( attribute–value pairs and array data types (or any other serializable value)) 또는 "키-값 쌍"으로 이루어진 데이터 오브젝트를 전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 [개방형 표준](https://ko.wikipedia.org/wiki/개방형_표준) 포맷이다. 비동기 브라우저/서버 통신 ([AJAX](https://ko.wikipedia.org/wiki/Ajax))을 위해, 넓게는 [XML](https://ko.wikipedia.org/wiki/XML)([AJAX](https://ko.wikipedia.org/wiki/Ajax)가 사용)을 대체하는 주요 데이터 포맷이다. 특히, [인터넷](https://ko.wikipedia.org/wiki/인터넷)에서 자료를 주고 받을 때 그 자료를 표현하는 방법으로 알려져 있다. 자료의 종류에 큰 제한은 없으며, 특히 [컴퓨터 프로그램](https://ko.wikipedia.org/wiki/컴퓨터_프로그램)의 [변수](https://ko.wikipedia.org/wiki/변수)값을 표현하는 데 적합하다.

본래는 [자바스크립트](https://ko.wikipedia.org/wiki/자바스크립트) 언어로부터 파생되어 [자바스크립트](https://ko.wikipedia.org/wiki/자바스크립트)의 구문 형식을 따르지만 언어 독립형 데이터 포맷이다. 즉, [프로그래밍 언어](https://ko.wikipedia.org/wiki/프로그래밍_언어)나 [플랫폼](https://ko.wikipedia.org/wiki/컴퓨팅_플랫폼)에 독립적이므로, [구문 분석](https://ko.wikipedia.org/wiki/구문_분석) 및 JSON 데이터 생성을 위한 코드는 [C](https://ko.wikipedia.org/wiki/C_(프로그래밍_언어)), [C++](https://ko.wikipedia.org/wiki/C%2B%2B), [C#](https://ko.wikipedia.org/wiki/C_샤프), [자바](https://ko.wikipedia.org/wiki/자바_(프로그래밍_언어)), [자바스크립트](https://ko.wikipedia.org/wiki/자바스크립트), [펄](https://ko.wikipedia.org/wiki/펄), [파이썬](https://ko.wikipedia.org/wiki/파이썬) 등 수많은 [프로그래밍 언어](https://ko.wikipedia.org/wiki/프로그래밍_언어)에서 쉽게 이용할 수 있다.

JSON 포맷은 본래 [더글라스 크록포드](https://ko.wikipedia.org/w/index.php?title=더글라스_크록포드&action=edit&redlink=1)가 규정하였다. RFC 7159와 ECMA-404라는 두 개의 경쟁 표준에 의해 기술되고 있다. ECMA 표준은 문법만 정의할 정도로 최소한으로만 정의되어 있는 반면 RFC는 시맨틱, 보안적 고려 사항을 일부 제공하기도 한다.[[2\]](https://ko.wikipedia.org/wiki/JSON#cite_note-2) JSON의 공식 인터넷 미디어 타입은 `application/json`이며, JSON의 파일 확장자는 `.json`이다.

파일 전송 포맷!



## 코드

#### app.py

```python
from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/hi")
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1> 
    <h2>반갑습니다</h2>
    """
import datetime
@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    endday = datetime.datetime(2019,11,29)
    d = endday - today
    return f"1학기 종료까지 {d.days}일 남음!!"

@app.route("/html_file")
def html_file():
    return render_template('index.html')

@app.route("/greeting/<string:name>")
def greeting(name):
    return f"안녕하세요 {name}님!!"

@app.route("/cube/<int:num>")
def cube(num):
    cube_num = num**3
    return "%d의 세제곱은 %d입니다." %(num, cube_num)

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)

@app.route("/greeting_html/<string:name>")
def greeting_html(name):
    return render_template("greeting.html",name=name)


@app.route("/lunch")
def lunch():
    menu={
        "짜장면" : "https://dispatch.cdnser.be/wp-content/uploads/2017/04/20170427213340_1q1q.jpg",
        "미트볼 스파게티" : "http://recipe1.ezmember.co.kr/cache/recipe/2015/06/08/a2464362f70de9c32b802926d178cb5a.jpg",
        "뼈해장국" : "https://t1.daumcdn.net/cfile/tistory/180714404D6CF4BC10"
    }

    menu_list = list(menu.keys()) # ["짜짱면","짬뽕","스파게티"]
    pick = random.choice(menu_list)
    image = menu[pick]

    return render_template("lunch.html", pick=pick, image=image)

@app.route("/movies")
def movies():
    movie_list = ['존윅3', '기생충', '토이스토리', '알라딘', '스파이더맨 : 파프롬홈']
    return render_template("movies.html", movie_list=movie_list)

@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    user_input=request.args.get("test")
    return render_template("pong.html",user_input=user_input)

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def goolge():
    return render_template("google.html")

@app.route("/text")
def text():
    return render_template("text.html")

@app.route("/result")
def result():
    raw_text = request.args.get('raw')
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url+raw_text).text
    return render_template("result.html",res=res)

@app.route('/randomgame')
def randomgame():
    return render_template("randomgame.html")


@app.route("/lotto")
def lotto():
    return render_template("lotto.html")

@app.route("/lotto_result")
def lotto_result():
    # 사용자가 입력한 정보를 가져오기
    numbers = request.args.get('numbers').split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))

    # user_number = [1,2,3,4,5,6]
    # 로또 홈페이지에서 정보를 가져오기
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()
    
    winning_numbers = []
    for i in range(1,7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonus_number = lotto_numbers['bnusNo']
    
    result = "1등"

    intersection = len(set(user_numbers) & set(winning_numbers))
    
    bo = len(set(user_numbers) & {bonus_number})
    
    if intersection == 6:
        result = "1등"
    elif intersection == 5:
        if bo == 1:
            result = "2등"
        else:
            result = "3등"
        pass
    elif intersection == 4:
        result = "4등"
    elif intersection == 3:
        result = "5등"
    else:
        result = "꽝"


    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, r=result, b=bonus_number)


if __name__ == '__main__':
    app.run(debug=True)
```





