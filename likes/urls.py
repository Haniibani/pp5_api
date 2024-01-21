from django.urls import path

from likes import views

urlpatterns = [
    path("likes/", views.LikeList.as_view(), name="like-list"),
    path("likes/<int:pk>/", views.LikeDetail.as_view(), name="like-detail"),
]
