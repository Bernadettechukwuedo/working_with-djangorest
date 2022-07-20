from django.urls import path
from .import views
app_name = "notes"


urlpatterns = [
    path("create/", views.TextCreateAPIView.as_view(), name="api_create"),
    path("update/<int:pk>", views.TextUpdateAPIView.as_view(), name="api_update"),
    path("delete/<int:pk>", views.TextDeleteAPIView.as_view(), name="api_delete"),
    path("", views.TextListAPIView.as_view(), name="api_list"),
    path("retrieve/<int:pk>", views.TextDetailAPIView.as_view(), name="api_retrieve"),

]
