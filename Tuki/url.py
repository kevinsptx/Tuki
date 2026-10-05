from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('vistas/',views.vistas,name='vistas'),
    path('register_vista/',views.register_vista,name='register_vista'),
    path('delete_vista/<int:id>/',views.delete_vista,name='delete_vista'),
    path('update_vista/<int:id>/',views.update_vista,name='update_vista')
]