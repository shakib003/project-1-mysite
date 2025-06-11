from . import views
from django.urls import path

# Namespacing
app_name = "food"

urlpatterns = [

    # food/
    # 127.0.0.1:8000/food/"" --> landing page of food page
    path("", views.index, name="index"),

    # /food/1
    path("<int:item_id>/", views.detail, name="detail"),

    # food/item/
    # there is a "item" button on food page, which takes to "127.0.0.1:8000/food/item/" page
    path("item/", views.item, name="item"),


]
