

# StartCamp-Day5

오늘은

telegram flask 서버를 연동해서 뭔가 만들 예정!

## TELEGRAM

카카오톡 플러스 친구처럼 사용자의 말에 따라서 움직이는 프로그램



## 보안 decouple 사용

변수를 숨기기위해서 밖에서 decouple 을 `pip install decouple`을 구매해온다.

같은 폴더내에 `.env` 파일로 환경변수를 만들어두고 git에 업로드하지 않기 위해서 gitignore을 설치하고 .env와 ignore 사이트에서 긁어온걸로 gitignore파일을 만든다.(확장명없음)

#### gitingore

.env



.

.

.

.

-> gitingore사이트에서 복붙한 것줄들

#### .env

```python
TELEGRAM_TOKEN='텔레그램 토큰을 복붙하세여'
CHAT_ID='당신의 채팅 고유아이디'
```



```python
import requests

token = config("TELEGRAM_TOKEN")		#환경변수는 대문자로 쓰는것이 규칙
url = f"https://api.telegram.org/bot{token}/"
print(url)

user_id = config("CHAT_ID")

send_url = f"{url}sendMessage?chat_id={user_id}&text=헤이요"
requests.get(send_url)
```



#### Web Hook - 챗봇에서 하는 말을 flask 서버로 받아오게 하는 것

test.py

```python
import requests
from decouple import config

token = config("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/"
print(url)

user_id = config("CHAT_ID")

# send_url = f"{url}sendMessage?chat_id={user_id}&text=헤이요"
# requests.get(send_url)
ngrok_url = "https://ee4ca557.ngrok.io"
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"
print(webhook_url)
```



#### 네이버 파파고 API 를 활용하기!!------------------------------------------------↓

https://developers.naver.com/docs/nmt/reference/													↓

네이버 개발 - > Application -> my application -> 원하는 API 추가해서 사용!				↓

![1562920210132](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562920210132.png)

​																																				↓

#### 사진파일을 받았을 때 반응하게 하기!------------------------------------------↓	import생략

![1562920163923](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562920163923.png)



```python
api_url  = "https://api.telegram.org"
token=config("TELEGRAM_TOKEN")
chat_id=config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config('NAVER_SECRET')

#챗봇에서 사용자가 하는 말을 읽어내고 다시 그 말을 돌려주는 것
@app.route(f"/{token}", methods=['POST'])	#토큰으로 쓰는 이유는 그게 
def telegram():
    data = request.get_json()
    #print(json.dumps(data, indent=4))
    user_id = data.get('message').get('from').get('id')
    user_msg = data.get('message').get('text')
    
    if data.get('message').get('photo') is None:
        
        if user_msg == "점심메뉴":						#사용자가 치틑 채팅에 따라 작동
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            lotto_list=list(range(1,46))
            luck=sorted(random.sample(lotto_list,6))	#샘플을 이용해서 45개 중 랜덤6개를뽑음
            result = luck
        elif user_msg[0:2] == "번역" :
            # 번역 안녕하세요 저는 누구입니다.
            raw_text = user_msg[3:]
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"	#네이버개발에서 찾아옴
            data = {
                "source":"ko", 
                "target":"en",
                "text":raw_text
            }
            headers = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
            res = requests.post(papago_url,data=data, headers=headers)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result

        elif user_msg == "실검":
            html=requests.get('https://www.naver.com/').text
            soup=BeautifulSoup(html,'html.parser')

            result=soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
            naver=""
            for idx, title in enumerate(result, 1):
                print(idx,title.text)
                title=title.text
                naver +=str(idx)+" "+str(title)
                naver +="\n"
            result = naver

        elif user_msg == "키워드":
            result="""
            다음과 같은 키워드가 있습니다 : 점심메뉴 로또 실검 박스오피스
            번역 안녕하세요 -> Hello.
            사진 -> 닮은 연예인 찾기
            """
        
        elif user_msg == "박스오피스":
            html=requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4').text
            soup=BeautifulSoup(html,'html.parser')
            result=soup.select('.scm_ellipsis_text')	#네이버의 박스오피스 클래스
            boxoffice=""						#박스오피스를 빈글자로 만들어두고
            for idx, title in enumerate(result, 1):
                print(idx,title.text)
                title=title.text
                boxoffice +=str(idx)+" "+str(title)	#여기서 값들을 전부 하나의 str으로만듬
                boxoffice +="\n"
            result = boxoffice

        else:
            result = user_msg		#올바른 글자가 없으면 사용자의 말을 메아리친다.

    else:
        # 사용자가 보낸 사진을 찾는 과정
        result="asdf"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        
        # 사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clover_url = "https://openapi.naver.com/v1/vision/celebrity"
        headers = {
            'X-Naver-Client-Id':naver_id,
            'X-Naver-Client-Secret':naver_secret
        }
        clova_res = requests.post(clover_url, headers=headers, files={'image':res.raw.read()})
        
        if clova_res.json().get('info').get('faceCount'):
            # 누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100:0.2f}%입니다."
        else:
            # 사람이 없음
            result = "사람이 없습니다."
```

박스오피스 반응

![1562920257793](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562920257793.png)









#### 오늘의 코딩

app.py

```python
from flask import Flask, escape, request, render_template
from decouple import config
import requests
import json
import random
from bs4 import BeautifulSoup

app = Flask(__name__)

api_url  = "https://api.telegram.org"
token=config("TELEGRAM_TOKEN")
chat_id=config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config('NAVER_SECRET')


#사용자가 적어준 문구를 send로 보내줌
@app.route("/write")
def write():
    return render_template("write.html")

#챗봇으로 url을 실행하도록 요구
@app.route("/send")
def send():
    msg = request.args.get('msg')
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    return render_template("send.html",msg=msg)

#챗봇에서 사용자가 하는 말을 읽어내고 다시 그 말을 돌려주는 것
@app.route(f"/{token}", methods=['POST'])
def telegram():
    data = request.get_json()
    #print(json.dumps(data, indent=4))
    user_id = data.get('message').get('from').get('id')
    user_msg = data.get('message').get('text')
    
    if data.get('message').get('photo') is None:
        
        if user_msg == "점심메뉴":
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            lotto_list=list(range(1,46))
            luck=sorted(random.sample(lotto_list,6))
            result = luck
        elif user_msg[0:2] == "번역" :
            # 번역 안녕하세요 저는 누구입니다.
            raw_text = user_msg[3:]
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko", 
                "target":"en",
                "text":raw_text
            }
            headers = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
            res = requests.post(papago_url,data=data, headers=headers)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result

        elif user_msg == "실검":
            html=requests.get('https://www.naver.com/').text
            soup=BeautifulSoup(html,'html.parser')

            result=soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
            naver=""
            for idx, title in enumerate(result, 1):
                print(idx,title.text)
                title=title.text
                naver +=str(idx)+" "+str(title)
                naver +="\n"
            result = naver

        elif user_msg == "키워드":
            result="""
            다음과 같은 키워드가 있습니다 : 점심메뉴 로또 실검 박스오피스
            번역 안녕하세요 -> Hello.
            사진 -> 닮은 연예인 찾기
            """
        
        elif user_msg == "박스오피스":
            html=requests.get('https://www.google.com/search?rlz=1C1PRFI_enKR855KR855&ei=DjkoXYMnqYavvA_p77_oAQ&q=%EC%98%81%ED%99%94&oq=%EC%98%81%ED%99%94&gs_l=psy-ab.3..0i67j0i131j0i67j0i131j0i67l4j0i131l2.2334.3136..3250...2.0..0.108.816.2j6......0....1..gws-wiz.....10..0i71j0j35i39.xUd6xghV2WM').text
            #네이버용 https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4
            soup=BeautifulSoup(html,'html.parser')
            result=soup.select('kltat')
            #네이버용 .scm_ellipsis_text
            boxoffice=""
            for idx, title in enumerate(result, 1):
                print(idx,title.text)
                title=title.text
                boxoffice +=str(idx)+" "+str(title)
                boxoffice +="\n"
            result = boxoffice

        else:
            result = user_msg

    else:
        # 사용자가 보낸 사진을 찾는 과정
        result="asdf"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        
        # 사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clover_url = "https://openapi.naver.com/v1/vision/celebrity"
        headers = {
            'X-Naver-Client-Id':naver_id,
            'X-Naver-Client-Secret':naver_secret
        }
        clova_res = requests.post(clover_url, headers=headers, files={'image':res.raw.read()})
        
        if clova_res.json().get('info').get('faceCount'):
            # 누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100:0.2f}%입니다."
        else:
            # 사람이 없음
            result = "사람이 없습니다."


    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)

    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
```

