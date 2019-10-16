# Django 191016

### Form 사용 법

form.py

```python
from django import forms
from .models import Questions, Choice

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    choices = [(1, '왼쪽'), (2, '오른쪽')]
    pick = forms.ChoiceField(choices=choices , widget=forms.RadioSelect)
    class Meta:
        model = Choice
        fields = ('pick', 'comment',)
```

class Meta 위에 적으면 원하는 데이터를 덮어씌울 수 있다.

fields 에는 모두 적고 싶으면 `'__all__'`을 적고 원하는 col만 적고 싶으면 튜플형태로 항목을 넣어준다.



views.py 에 추가

`from .forms import MovieForm, MovieModelForm, CommentModelForm`



```python
@login_required
@require_POST
def choice_create(request, id):
    question = get_object_or_404(Questions, id=id)
    choice_form = ChoiceForm(request.POST)
    if choice_form.is_valid:
        choice = choice_form.save(commit=False)
        choice.question = question
        choice.save()
    return redirect('questions:detail', id)
```

form.py 에서 가져온 데이터를 request.POST 에서 받은 값으로 변수에 넣고 유효한지 확인해서

추가로 넣어야 할 값이 있따면 save에 commit=False를 이용 model에 원하는 값을 직접넣고

model을 저장한다.





```python
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
```

위에서 쓴것 처럼 이런 항목들을 불러와서 @require_POST를 써주면 기본적으로 POST로 들어오지 않으면 에러가 발생하고 login_required는 login을 안하면 로그인창으로 보내준다.