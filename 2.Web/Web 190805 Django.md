# Web 190805 Django

MTV

Model :데이터를 관리

Template : 사용자가 보는 화면

View : 중간관리자



view 가 응답받기

model에 명령

model이 view에게 정보주기

view가 template에게 보내기

화면을 사용자에게 보내기



f1 -> select interpreter -> venv 있는 파이썬 클릭 -> 터미널 휴지통! -> 터미널 다시켜기!



`django-admin startproject .` : 프로젝트 생성

`python manage.py runserver` : 서버실행

`django-admin startapp pages` : 페이지 생성



project의 settings에 installed_apps에 pages 추가



프로젝트의 urls  ->  pages의 views.py -> templates의 연결되는 html파일


여러개의 인자받기

urls.py

```html
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('greeting/<str:name>/', views.greeting),
    path('cube/<int:num>/', views.cube),
    path('mul/<int:first>/<int:second>', views.mul),
]
```

views.py

```html
def mul(request, first, second):
    res = first * second
    context={
        'res': res,
        'first': first,
        'second': second,
    }
    return render(request, 'mul.html', context)
```

mul.html

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
  <h1>{{first}} X {{second}} = {{res}}</h1>
</body>
</html>
```



workshop 폴더로 이동

`mkdir 13workshop`

`cd 13workshop`

`python -m venv venv`

`pip install django`

`django-admin startproject classroom .` 

`python manage.py runserver`

`django-admin startapp pages`

