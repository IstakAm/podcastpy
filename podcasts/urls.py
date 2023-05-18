from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.IndexPage.as_view(), name="index page"),
    path('user/<str:creator>/', views.CreatorPage.as_view(), name="creator-page"),
    path('user/<str:creator>/<int:id>/', views.SinglePost.as_view(), name="single-post"),

]