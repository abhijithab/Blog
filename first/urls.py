from django.urls import path, include
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.Register, name='Register'),
    path('login/', views.login, name='login'),
    path('insert/', views.insert, name='insert'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('blogpst/<int:id>', views.blogpst, name='blogpst'),
    path('viewblog/', views.viewblog, name='viewblog'),

]
