from django.contrib.auth.views import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='register'),
    path('login', views.login_view, name='login'),
    path('index/', views.index_users, name='index'),
    #path('index_projects/', views.index_projects, name='index_projects'),
    path('index_services/', views.index_users, name='index_services'),
    path('register_ticket/', views.register_user, name='register_project'),
    #path('project_details/<int:pid>/', views.project_details, name='project_details'),
    #path('services/', views.services_view, name='services'),
    #path('my_projects/', views.error404, name='myprojects'),
    #path('my_services/', views.my_services, name='myservices'),
    #path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    path('delete_service/<int:pk>', views.delete_user, name='delete_service'),
    #path('edit_project/<int:pk>', views.edit_project, name='edit_project'),
    path('edit_service/<int:pk>', views.edit_user, name='edit_service'),
    #path('send_message/<int:receiver>/<int:sender>/', views.send_message, name='send_message'),
    #path('messages/', views.message_list, name='message_list'),
    #path('delete_message/<int:pk>', views.delete_message, name='delete_message'),
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
