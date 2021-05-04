from django.urls import path
from .views import EmployeeView, EmployeeUpdate

urlpatterns = [
    path('employee', EmployeeView.as_view()),
    path('employee/<str:pk>', EmployeeUpdate.as_view()),
]