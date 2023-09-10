from django.urls import path
from .views import CuboidBoxCreateView,CuboidBoxUpdateView,CuboidBoxListView,CuboidBoxDeleteView,UserBoxListView

urlpatterns = [
    path('boxes/create/', CuboidBoxCreateView.as_view(), name='create-box'),
    path('boxes/update/<int:pk>/', CuboidBoxUpdateView.as_view(), name='update-box'),
    path('boxes/delete/<int:pk>/', CuboidBoxDeleteView.as_view(), name='delete-box'),
    path('boxes/list/', CuboidBoxListView.as_view(), name='list-boxes'),
    path('api/my_boxes/', UserBoxListView.as_view(), name='user-box-list')
  
    ]

