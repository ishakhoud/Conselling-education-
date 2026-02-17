from . import views
from django.urls import path

urlpatterns = [
   path('' , views.index , name = 'index'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('career/', views.career , name = 'career'),
   path('sports/' , views.sports , name = 'sports'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('signup/' , views.signup , name = 'signup'),
   path('result/' , views.sports_result , name = 'sports_result'),
   path('result_career/' , views.career_result , name = 'career_result'),
]
