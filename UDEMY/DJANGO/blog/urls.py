from blog import views
from django.urls import path

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.Blog, name='home'),
    path('<int:post_id>/', views.Post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]