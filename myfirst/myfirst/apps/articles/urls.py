from django.urls import path

from. import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
    # path('test/', views.test, name = 'test'),
  
]

# /articles/
# /articles/1/leave_comment
# /articles/13/
# /articles/1231/