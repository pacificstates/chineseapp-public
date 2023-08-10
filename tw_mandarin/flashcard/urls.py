from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index",),
    path('lesson/<int:book>/<int:lesson>', views.Lesson, name="Lesson"),
    path("create/", views.create, name="create"),
    path('booknum-<int:id>/', views.BookNum, name="booknum"),
    path('next-card/', views.next_card, name='next_card'),
]
