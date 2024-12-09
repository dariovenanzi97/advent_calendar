from django.urls import path
from . import views

app_name = 'calendario'
urlpatterns = [
    path('', views.calendar_view, name='home'),
    path('open/<int:box_id>/', views.open_box, name='open_box'),
]