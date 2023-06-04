from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('registration/', register, name='registration'),
    path('logout/', logout, name='logout'),
    path('lessons/', lesson_list, name='lesson_list'),
    path('masters/', master_list, name='master_list'),
    path('cards/', cards_view, name='card_list'),
    path('master_lessons/<slug:username>/', lessons_for_current_master, name='master_lessons'),
    path('master_personal_students/<slug:username>/', students_for_current_master, name='master_students'),
    path('clients/', client_list, name='clients'),
    path('groups/', group_list, name='groups'),
    path('post/<int:client_id>/', show_post, name='post_client'),
    path('test/', api_test2, name='api_test'),
    path('lessons/', lesson_list, name='lesson_list'),
    path('masters/', master_list, name='master_list'),
    path('cards/', cards_view, name='card_list'),
path('master_lessons/<slug:username>/', lessons_for_current_master, name='master_lessons')
]