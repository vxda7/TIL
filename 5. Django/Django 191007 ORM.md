# Django 191007 ORM

### 게시물 불러오기

````python
In [12]: question = Question.objects.get(id=1)
In [13]: question
Out[13]: <Question: Question object (1)>

        
In [24]: question
Out[24]: <Question: Question object (1)>

In [25]: answer.question = question

In [26]: answer.question
Out[26]: <Question: Question object (1)>
        
In [28]: answer
Out[28]: <Answer: Answer object (None)>

In [29]: answer.save()

In [30]: answer
Out[30]: <Answer: Answer object (1)>

In [31]: answer.content
Out[31]: '이것이 바로 댓글임'

In [32]: answer.question
Out[32]: <Question: Question object (1)>   
        
In [35]: Answer.objects.create(content="두번째", question=question)
Out[35]: <Answer: Answer object (2)>

In [36]: answer.content
Out[36]: '이것이 바로 댓글임'
````



### 댓글 정보

```python
In [44]: answer.question.content
Out[44]: '날 돌려보내줘'

In [45]: answer.question_id
Out[45]: 1

In [46]: answer.content
Out[46]: '이것이 바로 댓글임'

In [47]: answer.id
Out[47]: 1

In [48]: answer.pk
Out[48]: 1

In [49]: answer.question_id
Out[49]: 1

In [50]: answer.question.id
Out[50]: 1
```



### 1:N

* Question(1) => Answer(N): `answer_set`

```python
In [58]: question.answer_set.all()
Out[58]: <QuerySet [<Answer: Answer object (1)>, <Answer: Answer object (2)>]>
```

* `question.answer` 로는 가져올 수 없다.

Answer(N) => Question(1): `question`

```python
In [59]: answer.question
Out[59]: <Question: Question object (1)>
```

