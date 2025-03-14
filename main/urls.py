from django.urls import path, URLPattern
from main import views
from main.views import AddNewPostView

app_name = 'main'
urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]

urlpatterns += [
    # path("addNewPost/", views.add_new_post, name="add_new_post"),
    path('add-new-post/', AddNewPostView.as_view(), name='add-new-post'),
]
