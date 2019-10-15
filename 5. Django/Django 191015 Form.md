# Django 191015 Form Change

## index

```python
def index(request):
    movies = Movie.objects.all().order_by('-id')
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)
```

sql에서 배웠떤 objects.all() 뒤에 order_by를 활용해서 -id의 내림차순을 해준다. 그러면 최신글이 가장 먼저 나온다.



```html
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  {% bootstrap_css %}
</head>
<body>
  <a href="{% url 'movies:index' %}">홈</a>
  <a href="{% url 'movies:create' %}">글쓰기</a>
  <a href="{% url 'movies:create_model_form' %}">글쓰기(모델폼)</a>
  <div class="container">
    {% block body %}
    {% endblock %}
  </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>
```

bootstrap4를 `pip install bootstrap4` 해서 활용하는 방법 자동으로 꾸며준다.



## detail

```python
def detail(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    comment_form = CommentModelForm()
    context = {
        'movie': movie,
        'comment_form': comment_form,
    }
    return render(request, 'detail.html', context)
```

`movie = get_object_or_404(Movie, id=id)` 



## Create_model_form

views.py

```python
def create_model_form(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.id)
    else:
        form = MovieModelForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context)
```

POST 방식으로 값을 받아와서 유효한 값이면  form형태를 저장해주고 (옳은 값 등록)

유효하지 않으면 입력한 만큼 form 화면으로 다시 돌려준다.	(잘못된 값 등록)

POST방식이 아니라면 비어있는 값을 다시 form화면에 돌려준다. (처음에 접속시 폼보여주기)



forms.py

```python
class MovieModelForm(forms.ModelForm):
    open_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Movie
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
```

모든 형태를 자동으로 만드려면 fields 를 `'__all__'` 로 넣어주고 일부분이면 tuple의 형태로 넣어준다.



```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block body %}
  {% if request.resolver_match.url_name == "create_model_form"%}
    <h1>create</h1>
  {% else %}
    <h1>update</h1>
  {% endif %}
  <form action="{% url 'movies:comment_create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit="제출"%}{% endbuttons %}
  </form>
{% endblock %}
```

`{{form.as_p}}`   bootstrap 없이 적는 법 1

`{{form.as_table}}` bootstrap 없이 적는 법2 테이블태그로 감싸줘야 함

`{% bootstrap_form form %}` bootstrap4로 활용



## Update

```python
def update_model_form(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', id)
    else:
        form = MovieModelForm(instance = movie)
    context = {
        'form': form
    }
    return render(request, 'form.html', context)
```

movie에 값이 올바르지 않으면 에러404발생 아니라면 form을 instance를 movie의 형태로 불러와서 

유효하면 저장하고 돌려보내고

아니라면 비어있는 값을 보낸다.





## Comment

```python
def comment_create(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', id)
        else:
            pass
    else:
        pass
```

movie에서 에러404인지 아닌지 받아오고

POST형태로 등록되면 html에서 받아온 form 형태로 저장하지만 어떤 movie인지 정해지지 않았으므로

commit = False를 활용해서 잠시 멈추고

`comment.movie = movie` 로 값을 저장해서 디테일 페이지로 넘겨준다.





## SQL

```html
  <form action="{% url 'movies:comment_create' movie.id %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form %}
    {% buttons submit="제출"%}{% endbuttons %}
  </form>
  {% if movie.comment_set.all %}
    {% for comment in movie.comment_set.all %}
      <h6>{{comment.author}}</h6>
      <h2>{{comment.content}}</h3>
    {% endfor %}
  {% else %}
    <h5>댓글이 없습니다.</h5>
  {% endif %}

```

댓글다는 부분의 html인데 `movie.comment_set.all` 으로 movie와 comment의 종속관계를 활용해서 movie에서 comment를 불러내서 사용한다.