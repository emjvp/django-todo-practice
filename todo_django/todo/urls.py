from django.urls import path
from todo import views

urlpatterns = [    
    path(r'', views.TodoListView.as_view(), name='todo-list'),
    path(r'add/', views.TodoAddView.as_view(), name='todo-add'),
    path(
        r'done/<int:todo_id>/',
        views.TodoDoneView.as_view(),
        name='todo-done'
    ),
    path(
        r'edit/<int:todo_id>/',
        views.TodoEditView.as_view(),
        name='todo-edit'
    ),
    path(
        r'delete/<int:todo_id>/',
        views.TodoDeleteView.as_view(),
        name='todo-delete'
    )
]