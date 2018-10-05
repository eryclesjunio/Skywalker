from django.contrib.auth.views import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='register'),
    path('login', views.login_view, name='login'),
    path('index/', views.index_users, name='index'),
    path('index_services/', views.index_users, name='index_services'),
    path('register_ticket/', views.register_user, name='register_project'),
    path('delete_service/<int:pk>', views.delete_user, name='delete_service'),
    path('edit_service/<int:pk>', views.edit_user, name='edit_service'),
    path('register_service/', views.register_user, name='register_service'),
    path('register_team/', views.register_team, name='register_team'),
    path('people_list/<int:pk>', views.index_people, name='index_people'),
    path('add_person/<int:id>/<int:codigo>/', views.add_person, name='add_person'),
    path('index_teams/', views.index_teams, name='index_teams'),
    path('edit_team/<int:pk>', views.edit_team, name='edit_team'),
    path('delete_team/<int:pk>', views.delete_team, name='delete_team'),
    path('delete_subscriber/<int:id>/<int:codigo>/', views.delete_subscriber, name='delete_subscriber'),
    path('logout/', views.logout_view, name='logout'),
]
