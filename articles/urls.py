from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name='index'),

    # Create (이번엔 new와 create를 이 create 하나에 다 넣었음)
    path('create/', views.create, name='create'),
    
]