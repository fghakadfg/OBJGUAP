from django.urls import path
from . import views



urlpatterns = [

    path('', views.video, name='video'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>', views.get_video, name='video'),
]

