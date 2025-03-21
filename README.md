# Board

1. 가상환경 활성화
2. .gitignore
3. Django 설치
---
4. `django-admin startproject board .`
---
5. `django-admin startapp articles`
6. `settings.py`에서 앱폴더 등록
---
7. 앱폴더 `articles`폴더에도 urls.py 만들어서 중복되는 함수 최소화(이중구조)
---
8. 앱폴더에 urls.py 추가하고 아래 문장 기재
```py
urlpatterns = [
    path('', views.index),
]
```
9. 번역작업
```shell
python manage.py makemigrations
python manage.py migrate
```
10. admin superuser
```shell
python manage.py createsuperuser
```
11. run server
```shell
python manage.py runserver
```
12. 베이스 html 만들기
- 최상단에 templates 폴더 만들기
- `settings.py`에서 templates 경로 추가
- 최상단 경로 templates에 base.html 만들고 뼈대 추가하기
```html
<body>
    <h1>여기는 base</h1>
    {% block body %}
    {% endblock %}
</body>
```