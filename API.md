# API

```bash
pip install djangorestframwork
```

settings/

```python
 installed_app = [
	'rest_framework',	
	'drf_yasg',
]
```

json 파일로 만들어주기 위해서

```bash
python manage.py dumpdata --indent 2 musics > my_dumpdata.json
```

만들어진 파일 > musics 안으로 이동

만들어진 데이터 덮어쓰기

```bash
python manage.py loaddata musics/my muscis/my_dumpdata.json
```



`app의 urls에 추가`

```python
path('api/v1/', include('musics.urls')),
```



`app 에 serializers.py 생성`

```python
from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_id']
```



`views 에 rest_framework 및 serializers 사용`

```python
from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, id):
    music = get_object_or_404(Music, id=id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
```



`pip install drf-yasg`

백엔드와 프론트엔드간에 url 구조를 확인하기 위해서 확인할 수 있게 해주는 프로그램

urls로 연결

````python
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Music_API",
      default_version='v1',
   ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('musics.urls')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('swagger/', schema_view.with_ui('swagger')),
]
````



```python
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
from django http import JsonResponse
json_musics = {}
for music in musics:
	json_music[music.id] = music.title
return JsonResponse(json_musics)
```

딕셔너리를 제이슨 형태로 넘겨주는 방식





#### Comment

##### serializers.py

```python
from rest_framework import serializers
from .models import Music, Artist, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')
```



##### views.py

```python
@api_view(['POST'])
def comment_create(request, id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(music_id=id)
    return Response(serializer.data)


# GET, POST, PUT/PATCH, DELETE
# READ, Create, Update, Delete
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, id):
    comment  = get_object_or_404(Comment, id=id)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)
            # return Response({'message':'업데이트!!!'})
    else:
        comment.delete()
        return Response({'message':'삭제되었습니다.'})
```







##### serializers.py

```python
class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(source='music_set', many=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics')
```

![image-20191028140302903](assets/image-20191028140302903.png)

