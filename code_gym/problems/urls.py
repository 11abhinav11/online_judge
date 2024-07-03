from django.urls import path
from . import views

urlpatterns = [
    path('', views.problems, name='problems'),
    path('/dashboard', views.dashboard, name='dashboard'),
    path('/add', views.add_problem, name='add problem'),
    path('/test/<int:id>', views.add_test, name='add test case'),
    path('/<int:id>', views.solve, name='solve question'),
]
