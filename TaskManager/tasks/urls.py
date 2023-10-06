from django.urls import path
from . import views, apis
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', apis.ListTaskAPI.as_view(), name='list-task'),
    path('addTask/', apis.AddTaskAPI.as_view(), name='add-task'),
    path('viewTask/<int:pk>/', apis.DetailTaskAPI.as_view(), name='view-task'),
    path('search/', apis.TaskSearchAPI.as_view(), name='search'),
    # path('updateTask/<int:pk>/', apis.UpdateTaskAPI.as_view(), name='update-task'),
    # path('deleteTask/<int:pk>/', apis.DeleteTaskAPI.as_view(), name='delete-task'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add/', views.add_task_form, name='add'),
    path('updateTask/<int:pk>/', views.Edit_Info, name='update-task'),
    path('deleteTask/<int:pk>/', views.Delete_Info, name='delete-task'),
]