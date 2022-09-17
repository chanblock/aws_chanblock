
from user import views
from django.urls import include, path


urlpatterns = [
    path('comments', views.comments,name='comments'),
    path('comments_history', views.comments_history,name='comments_history'),
      
]
