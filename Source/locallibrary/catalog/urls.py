from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bikes/', views.BikeListView.as_view(), name='bikes'),
    path('bike/<int:pk>', views.BikeDetailView.as_view(), name='bike-detail'),
    path('mybikes/', views.LoanedBikesByUserListView.as_view(), name='my-borrowed'),
]