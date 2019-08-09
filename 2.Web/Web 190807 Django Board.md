# Web 190807 Django Board

models.py!

```git
python manage.py makemigrations
python manage.py migrate
```



슈퍼유저 생성!

`python manage.py createsuperuser`

```git
Username (leave blank to use 'student'): admin
Email address:
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv)
```



같은코드!

```
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()
```

```
    todo = Todo(title=title, content=content, due_date=due_date)
    todo.save()
```



`name=` : url 에 넘겨주고 싶을 때

`value=` : 실제값을 주고싶을 때

`placeholder=` : 예제값을 보여주고 싶을 때



함수가 돌아간 이후에 다른 함수에게 넘겨주기!

지금까지

```
return render(request, 'create.html', context)
```

바뀔것 `from django.shortcuts import render, redirect ` 추가해줘야함

```
return redirect()
```



원하는 데이터를 기준으로 정렬 - 거꾸로 하고싶으면 - 붙이기

`todos = Todo.objects.order_by('-due_date').all()`

