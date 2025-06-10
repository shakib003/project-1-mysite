from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),  # 127.0.0.1:8000/food/"" --> landing page of food page
    path("item/", views.item, name="item"), # there is a "item" button on food page, which takes to "127.0.0.1:8000/food/item/" page
]  