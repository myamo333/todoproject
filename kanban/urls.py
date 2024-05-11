# kanban/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),  # 追加する行
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),  # URLパターンを修正
]
