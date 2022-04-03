from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing_Page.as_view(), name="landing_page"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('tasks/', views.Task_List.as_view(), name="task_list"),
    path('tasks/new/', views.Task_Create.as_view(), name="task_create"),
    path('tasks/<int:pk>/', views.Task_Detail.as_view(), name="task_detail"),
    path('tasks/<int:pk>/update', views.Task_Update.as_view(), name="task_update"),
    path('tasks/<int:pk>/delete', views.Task_Delete.as_view(), name="task_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('transactions/', views.transactions_index, name='transactions_index'),
    path('transactions/<int:transaction_id>', views.transactions_show, name='transactions_show'),


]