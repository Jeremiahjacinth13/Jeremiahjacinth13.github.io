from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('new/', views.new_project, name = 'new_project'),
    path('contact/', views.contact, name = 'contact'),
    path('<str:project>/', views.project, name = 'project')
]


