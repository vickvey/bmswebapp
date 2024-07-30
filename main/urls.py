from django.urls import path
from main import views

urlpatterns = [
    path('why/', views.why, name='why'),
    path('help/', views.help, name='help'),
    path('careers/', views.careers, name='careers'),
    path('about_us/', views.about_us, name='about_us'),
    
    path('addaccount/', views.addaccount, name='addaccount'),
    path('login/', views.login, name='login'),
    
    path('', views.index, name='index')
]
