from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.SnippetList.as_view()),
    path('api/<uuid:pk>/', views.BuyerDetail.as_view()),
]