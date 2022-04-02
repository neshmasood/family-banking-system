from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing_Page.as_view(), name="landing_page"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('tasks/', views.Task_List.as_view(), name="task_list"),

]